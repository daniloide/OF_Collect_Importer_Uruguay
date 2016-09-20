#!/usr/bin/env python
# -*- coding: utf-8 -*-s
"""
The information will become visible in the "Fauna" tab in OF Collect. Four groups of vertebrates are imported:
 "*Mamiferos*","*Aves*","*Anfibios*" and "*Reptiles*". For each of the four group a separate species list is required.
"""
import argparse
import csv
import datetime
import logging
import os
import sys
import time

from src.data_mapping_2010 import import_fauna_2010
from src.data_mapping_2015 import import_fauna_2015
from src.model import class_lib
from src.utils import tools_lib


def import_fauna(survey, species_list, infile, format, verbose=None):
    """
    Function to import_modules the forest plant records into the survey

    :param survey:  A survey object into which the plot information will be added
    :param species_list:  A list with forest plant species names as exported from the Collect species lists
    :param infile:  The file path to the plot data
    :param format:  The data format either \"2010 \" or \"2015\"
    :type survey:  :class:`~model.class_lib.Survey`
    :type species_list: A dictionary with instances of :class:`~model.class_lib.Species`
    :type infile: file path
    :type format: string
    :return: If executed as script a file with the distance information that can be imported in to OF Collect.
     Otherwise an updated survey object
    :rtype: :class:`~model.class_lib.Survey` / CSV File

    - **Example**  how to use as script::

        :Example usage:
        python import_forest_flora.py Datos_generales_2010.csv flora_suelo_2010.csv 2010
    """
    start = time.time()
    now = datetime.datetime.now()
    info_msg = ' Started the import_modules of fauna information {date}'. \
        format(date=now.strftime("%Y-%m-%d %H:%M"))
    logging.info(info_msg)
    try:
        version = tools_lib.get_git_tag().strip()
    except:
        version = ''
    info_msg = ' ForestEye Collect Importer {version}'.format(version=version)
    logging.info(info_msg)

    if format == '2010':
        import_fauna_2010.import_fauna_2010(survey, species_list, infile)
    elif format == '2015':
        import_fauna_2015.import_fauna_2015(survey, species_list, infile)
    else:
        warn_message = "The file format {format} is not supported".format(format=format)
        logging.warn(warn_message)

    info_msg = "The import_modules took {time:.2} seconds".format(time=time.time() - start)
    logging.info(info_msg)
    now = datetime.datetime.now()
    info_msg = ' Finished the import_modules of fauna information dataset {date}'. \
        format(date=now.strftime("%Y-%m-%d %H:%M"))
    logging.info(info_msg)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Function to create a csv of the fauna records from the 2010 data format')

    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument('InFileNameFauna', type=str, help="Input csv file with 2010 fauna records")
    parser.add_argument("InFileNameSpeciesBirds", type=str,
                        help="Input csv file with bird species in the Collect format")
    parser.add_argument("InFileNameSpeciesMammals", type=str,
                        help="Input csv file with mammal species in the Collect format")
    parser.add_argument("InFileNameSpeciesReptiles", type=str,
                        help="Input csv file with reptile species in the Collect format")
    parser.add_argument("InFileNameSpeciesAmphibians", type=str,
                        help="Input csv file with amphibian species in the Collect format")
    parser.add_argument("OutDirName", type=str, help="Output directory name")
    parser.add_argument("-np","--NamePrefix",type =str,
                        help="A prefix that should be used for the file names of the different groups")
    parser.add_argument("-f", "--format", choices=['2010', '2015'], help="The data format either \"2010\" or \"2015\"")
    parser.add_argument("-log", "--LogFileName", type=str, help="Filepath for the logfile")

    args = parser.parse_args()
    InFileNameFauna = os.path.normpath(args.InFileNameFauna)
    InFileNameSpeciesBirds = os.path.normpath(args.InFileNameSpeciesBirds)
    InFileNameSpeciesMammals = os.path.normpath(args.InFileNameSpeciesMammals)
    InFileNameSpeciesReptiles = os.path.normpath(args.InFileNameSpeciesReptiles)
    InFileNameSpeciesAmphibans = os.path.normpath(args.InFileNameSpeciesAmphibians)
    OutDirName = os.path.normpath(args.OutDirName)
    NamePrefix = args.NamePrefix
    format = args.format
    verbose = args.verbose

    if format not in ['2010','2015']:
        error_msg = " The specified format: \"{format}\" is currently not supported".format(format=format)
        print error_msg
        sys.exit(0)

    if args.LogFileName:
        logfile=args.LogFileName
    else:
        logfile = os.path.normpath(OutDirName+'/fauna.log')
    try:
        os.remove(logfile)
    except OSError:
        pass
    if args.verbose:
        logging.basicConfig(format='%(levelname)s: %(message)s', filename=logfile, level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(levelname)s: %(message)s', filename=logfile, level=logging.INFO)

    if format == '2010':
        survey = tools_lib.import_survey(InFileNameFauna, 'p_muestreo_pl', 1)
    if format == '2015':
        survey = tools_lib.import_survey(InFileNameFauna, 'nombre_pm', 1)

    # Import the different fauna species list
    species_list = {}
    for i in [InFileNameSpeciesBirds, InFileNameSpeciesMammals, InFileNameSpeciesReptiles, InFileNameSpeciesAmphibans]:
        with open(i, 'rb') as csvfile:
            datareader = csv.DictReader(csvfile, delimiter=',')
            for row in datareader:
                species = class_lib.Species(row['no'], row['code'], row['scientific_name'])
                species.common_name = row['synonyms']
                species_list[species.species_id] = species

    import_fauna(survey, species_list, InFileNameFauna, format,verbose)
    survey.export_fauna_files(OutDirName,NamePrefix)

