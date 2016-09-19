#!/usr/bin/env python
# -*- coding: utf-8 -*-s
"""
This script provides the functionality to import_modules the foto information from the DGF. After import_modules the
distance records will become visible in the tab "Distancia" in OF Collect. This type of information is currently only
available in the 2015 data format.
"""

import argparse
import datetime
import logging
import os
import sys
import time

from data_mapping_2015 import import_fotos_2015
from utils import tools_lib


def import_fotos(survey, infile, format, verbose=None):
    """
    Function to import_modules the foto  records into the survey

    :param survey:  A survey object into which the plot information will be added
    :param infile:  The file path to the plot data
    :param format:  The data format either \"2010 \" or \"2015\"
    :type survey:  :class:`~model.class_lib.Survey`
    :type infile: file path
    :type format: string
    :return: If executed as script a file with the equioment information that can be imported in to OF Collect.
     Otherwise an updated survey object
    :rtype: :class:`~model.class_lib.Survey` / CSV File

    - **Example**  how to use as script::

        :Example usage:
        python import_fotos.py -v UNIFICADA_NATIVO_PIKE_corregido_DGF_9-10-15.csv  fotos_2015.csv 2015
        -log fotos_2015.log

    .. note:: Currently this function is only available for the 2015 data format
    """

    start = time.time()
    now = datetime.datetime.now()
    info_msg = ' Started the import_modules of foto information {date}'. \
        format(date=now.strftime("%Y-%m-%d %H:%M"))
    logging.info(info_msg)
    try:
        version = tools_lib.get_git_tag().strip()
    except:
        version = ''
    info_msg = ' ForestEye Collect Importer {version}'.format(version=version)
    logging.info(info_msg)

    if format == '2015':
        import_fotos_2015.import_fotos_2015(survey, infile)
    elif format == '2010':
        error_msg = "The import_modules of the foto data is not supported for 2010 file format"
        logging.error(error_msg)
        print(error_msg)
        sys.exit(0)
    else:
        warn_message = "The file format {format} is not supported".format(format=format)
        logging.warn(warn_message)

    info_msg = "The import_modules took {time:.2} seconds".format(time=time.time() - start)
    logging.info(info_msg)
    now = datetime.datetime.now()
    info_msg = ' Finished the import_modules of foto information dataset {date}'. \
        format(date=now.strftime("%Y-%m-%d %H:%M"))
    logging.info(info_msg)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Function to create csv of the foto recordings')
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument('InFileNamePlots', type=str, help="Input csv file with plot data")
    parser.add_argument("OutFileName", type=str, help="Outputfile Name")
    parser.add_argument("-f", "--format", choices=['2015'], help="The data format either \"2010\" or \"2015\"")
    parser.add_argument("-log", "--LogFileName", type=str,help="Filepath for the logfile")
    args = parser.parse_args()
    InFileNamePlots = os.path.normpath(args.InFileNamePlots)
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
    now = datetime.datetime.now()
    if args.verbose:
        logging.basicConfig(format='%(levelname)s: %(message)s', filename=logfile, level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(levelname)s: %(message)s', filename=logfile, level=logging.INFO)

    survey = tools_lib.import_survey(InFileNamePlots, 'nombre_pm', 1)
    import_fotos(survey, InFileNamePlots, format, verbose)
    survey.export_fotos(OutFileName)