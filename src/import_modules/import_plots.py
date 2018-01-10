#!/usr/bin/env python
# -*- coding: utf-8 -*-s
"""
This script provides the functionality to import_modules the  plot information from the DGF data either in the 2015 or
2010 data format. It can be used to import_modules data for natural forest and plantation forest from both of the providers
"Technicos" and "Pike". The script generates a csv file that can be imported into OF Collect using the import_modules function
of the data mangement modul.
"""

from src.data_mapping_2010 import import_plots_2010
from src.data_mapping_2015 import import_plots_2015
from src.data_mapping_test import import_plots_test

def import_plots(survey,species_list,infile,format,verbose=None):
    """ Function to import_modules plot records from natural forest and plantations

        :param survey:  A survey object into which the plot information will be added
        :param species_list:  A list with tree species names as exported from the Collect species list
        :param infile:  The file path to the plot data
        :param format:  The data format either \"2010 \" or \"2015\"
        :type survey: :class:`~model.class_lib.Survey`
        :type species_list: A dictionary with instances of :class:`~model.class_lib.Species`
        :type infile: file path
        :type format: string
        :return: If executed as script a file with the plot information that can be imported in to OF Collect.
         Otherwise an updated survey object
        :rtype: :class:`~model.class_lib.Survey` / CSV File

        - **Example**  how to use as script::

            :Example usage:
            python import_plots.py Datos_generales_2010.csv arbol_especie.csv arboles_nativo_2010.csv 2010

        .. note:: If plots with understory are imported the value of field "Presencia de sotobosque" is set to "Si". However,
                the type of understory and the height is only updated once the csv created using the :mod:`~src.import_modules.import_forest_flora` is uploaded to OF Collect.
        """
    start = time.time()
    now = datetime.datetime.now()
    info_msg = ' Started the import_modules of plot information {date}'. \
        format(date=now.strftime("%Y-%m-%d %H:%M"))
    logging.info(info_msg)
    try:
        version = tools_lib.get_git_tag().strip()
    except:
        version = ''
    info_msg = ' ForestEye Collect Importer {version}'. \
            format(version=version)
    logging.info(info_msg)
    if format == '2010':
        import_plots_2010.import_fni_plots_2010(survey, species_list, infile)
    elif format == '2015':
        import_plots_2015.import_fni_plots_2015(survey, species_list, infile)
    elif format == 'test':
        import_plots_test.import_fni_plots_test(survey, species_list, infile)
    else:
        warn_message = "The file format {format} is not supported".format(format=format)
        logging.warn(warn_message)

    info_msg = "The import_modules took {time:.2} seconds".format(time=time.time() - start)
    logging.info(info_msg)
    now = datetime.datetime.now()
    info_msg = ' Finished the import_modules of single tree information dataset {date}'. \
        format(date=now.strftime("%Y-%m-%d %H:%M"))
    logging.info(info_msg)

if __name__ == "__main__":
    import time
    import datetime
    import argparse
    import logging
    import os
    import sys
    from src.utils import tools_lib

    parser = argparse.ArgumentParser(
        description='Function to create csv of the plot information to import_modules in OF Collect')
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument('InFileNamePlots', type=str, help="Input csv file with plot data")
    parser.add_argument("InFileNameSpecies", type=str,
                        help="Input csv file with tree species in the Collect format")
    parser.add_argument("OutFileName", type=str, help="Outputfile Name")
    parser.add_argument("-f","--format", choices=['2010','2015', 'test'], help="The data format either \"2010\" or \"2015\"")
    parser.add_argument("-log", "--LogFileName", type=str, help="Filepath for the logfile")

    args = parser.parse_args()
    InFileNamePlots = os.path.normpath(args.InFileNamePlots)
    InFileNameSpecies = os.path.normpath(args.InFileNameSpecies)
    verbose = args.verbose
    format = args.format
    OutFileName = os.path.normpath(args.OutFileName)

    if args.LogFileName:
        logfile=args.LogFileName
    else:
        file,ext = os.path.splitext(OutFileName)
        logfile = os.path.normpath(file+'.log')
    try:
        os.remove(logfile)
    except OSError:
        pass

    if verbose:
        logging.basicConfig(format='%(levelname)s: %(message)s', filename=logfile, level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(levelname)s: %(message)s', filename=logfile, level=logging.INFO)

    if format not in ['2010','2015', 'test']:
        error_msg = " The specified format: \"{format}\" is currently not supported".format(format=format)
        print error_msg
        sys.exit(0)

    survey = tools_lib.import_survey(InFileNamePlots, 'nombre_pm', 1)
    species_list = tools_lib.import_species_list(InFileNameSpecies)
    import_plots(survey, species_list, InFileNamePlots, format, verbose)
    survey.export_parcela_file(OutFileName)
