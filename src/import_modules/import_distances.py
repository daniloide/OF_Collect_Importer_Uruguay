#!/usr/bin/env python
# -*- coding: utf-8 -*-s
"""
This script provides the functionality to import_modules the distance information from the DGF data either in the 2015 or
2010 data format. It can be used to import_modules data for natural forest and plantation forest from both of the providers
"Technicos" and "Pike". The script generates a csv file that can be imported into OF Collect using the import_modules function
of the data management modul. After import_modules the distance records will become visible in the tab "Distancia" in OF Collect.
"""
import argparse
import datetime
import logging
import os
import sys
import time

from src.data_mapping_2010 import import_distancia_2010
from src.data_mapping_2015 import import_distancia_2015
from src.utils import tools_lib


def import_distances(survey, infile,format,verbose=None):
    """
    Function to import_modules the distance records into the survey

    :param survey:  A survey object into which the plot information will be added
    :param infile:  The file path to the plot data
    :param format:  The data format either \"2010 \" or \"2015\"
    :type survey:  :class:`~model.class_lib.Survey`
    :type infile: file path
    :type format: string
    :return: If executed as script a file with the distance information that can be imported in to OF Collect.
     Otherwise an updated survey object
    :rtype: :class:`~model.class_lib.Survey` / CSV File

    - **Example**  how to use as script::

        :Example usage:
        python import_distances.py Datos_generales_2010.csv distancias_2010.csv 2010
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
        import_distancia_2010.import_distancia_2010(survey, infile)
    elif format == '2015':
        import_distancia_2015.import_distanca_2015(survey, infile)
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
    start = time.time()
    parser = argparse.ArgumentParser(
        description='Function to create csv of the distance recordings')

    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument('InFileNamePlots', type=str, help="Input csv file with 2010 plot data")
    parser.add_argument("OutFileName", type=str, help="Outputfile Name")
    parser.add_argument("-f","--format", choices= ['2010','2015'], help="The data format either \"2010\" or \"2015\"")
    parser.add_argument("-log", "--LogFileName", type=str, help="Filepath for the logfile")

    args = parser.parse_args()
    InFileNamePlots = os.path.normpath(args.InFileNamePlots)
    OutFileName = os.path.normpath(args.OutFileName)
    format = args.format
    verbose = args.verbose

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


    if format not in ['2010','2015']:
        error_msg = " The specified format: \"{format}\" is currently not supported".format(format=format)
        print error_msg
        sys.exit(0)

    survey = tools_lib.import_survey(InFileNamePlots, 'nombre_pm', 1)
    import_distances(survey, InFileNamePlots,format,verbose)
    survey.export_distance_file(OutFileName)