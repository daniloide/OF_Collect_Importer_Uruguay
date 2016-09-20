#!/usr/bin/env python
# -*- coding: utf-8 -*-s
"""
This script provides the functionality to import_modules the information on regeneration. After import_modules the
regeneration records will become visible in the tab "Regeneracion" in OF Collect. This type of information is only
available in the 2015 data format and only for natural forest.
"""
import argparse
import datetime
import logging
import os
import sys
import time

from src.data_mapping_2015 import import_regeneracion_2015
from src.utils import tools_lib


def import_regeneration(survey,species_list, infile, format, verbose=None):
    """
    Function to import_modules the invasive species records into the survey

    :param survey:  A survey object into which the plot information will be added
    :param species_list:  A list with tree species names as exported from the Collect species lists
    :param infile:  The file path to the plot data
    :param format:  The data format either \"2010 \" or \"2015\"
    :type survey:  :class:`~model.class_lib.Survey`
    :type species_list: A dictionary with instances of :class:`~model.class_lib.Species`
    :type infile: file path
    :type format: string
    :return: If executed as script a file with the equioment information that can be imported in to OF Collect.
     Otherwise an updated survey object
    :rtype: :class:`~model.class_lib.Survey` / CSV File

    - **Example**  how to use as script::

        :Example usage:
        python import_regeneration.py -v UNIFICADA_NATIVO_PIKE_corregido_DGF_9-10-15.csv arbol_especie.csv regeneration_2015.csv 2015
        -log regeneration_2015.log

    .. note: This function is currently only available for the 2015 data format
    """
    start = time.time()
    now = datetime.datetime.now()
    info_msg = ' Started the import_modules of regeneration information {date}'. \
        format(date=now.strftime("%Y-%m-%d %H:%M"))
    logging.info(info_msg)
    try:
        version = tools_lib.get_git_tag().strip()
    except:
        version = ''
    info_msg = ' ForestEye Collect Importer {version}'.format(version=version)
    logging.info(info_msg)

    if format == '2015':
        import_regeneracion_2015.import_regeneracion_2015(survey, species_list, infile)
    elif format == '2010':
        error_msg = "The import_modules of regeneration is not supported for 2010 file format"
        logging.error(error_msg)
        print(error_msg)
        sys.exit(1)
    else:
        error_msg = "The file format {format} is not supported".format(format=format)
        logging.error(error_msg)
        print(error_msg)
        sys.exit(1)

    info_msg = "The import_modules took {time:.2} seconds".format(time=time.time() - start)
    logging.info(info_msg)
    now = datetime.datetime.now()
    info_msg = ' Finished the import_modules of regeneration information from dataset {date}'. \
        format(date=now.strftime("%Y-%m-%d %H:%M"))
    logging.info(info_msg)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Function to create csv of the  regeneration recordings')
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument('InFileNamePlots', type=str,
                        help="Input csv file with plot data")
    parser.add_argument("InFileNameSpecies", type=str,
                        help="Input csv file with tree species names in the Collect format")
    parser.add_argument("OutFileName", type=str,
                        help="Outputfile Name")
    parser.add_argument("-f", "--format", choices=['2015'], help="The data format either \"2010\" or \"2015\"")
    parser.add_argument("-log", "--LogFileName", type=str,
                        help="Filepath for the logfile")
    args = parser.parse_args()
    InFileNamePlots = os.path.normpath(args.InFileNamePlots)
    InFileNameSpecies = os.path.normpath(args.InFileNameSpecies)
    OutFileName = os.path.normpath(args.OutFileName)
    format = args.format
    verbose = args.verbose

    if format not in ['2015']:
        error_msg = " The specified format: \"{format}\" is currently not supported".format(format=format)
        print error_msg
        sys.exit(0)

    if args.LogFileName:
        logfile=args.LogFileName
    else:
        file,ext = os.path.splitext(OutFileName)
        logfile = os.path.normpath(file+'.log')

    try:
        os.remove(logfile)
    except OSError:
        pass

    if args.verbose:
        logging.basicConfig(format='%(levelname)s: %(message)s', filename=logfile, level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(levelname)s: %(message)s', filename=logfile, level=logging.INFO)

    survey = tools_lib.import_survey(InFileNamePlots, 'nombre_pm', 1)
    species_list = tools_lib.import_species_list(InFileNameSpecies)
    import_regeneration(survey, species_list,InFileNamePlots, format, verbose)
    survey.export_regeneracion(OutFileName)