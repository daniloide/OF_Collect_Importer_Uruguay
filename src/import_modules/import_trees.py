#!/usr/bin/env python
# -*- coding: utf-8 -*-s
"""
This script provides the functionality to import_modules the single tree information from the DGF data either in the 2015 or
2010 data format. It can be used to import_modules data for natural forest and plantation forest from both of the providers
"Technicos" and "Pike". The script generates a csv file that can be imported into OF Collect using the Import function
of the data mangement modul. After import_modules the single tree variables will become visible in the tab "Datos Dasométrics"
in OF Collect. The script can be used as a general python module in a python program are called as a python script from
the console. Furthermore, a Windows binary with the extention .exe is provided if Python is not installed on the system.
The syntaxy for the usage of the program as script or as exe in the Windows console is identical.
"""
from src.data_mapping_2010 import import_arbol_2010
from src.data_mapping_2010 import import_plots_2010
from src.data_mapping_2015 import import_arbol_2015


def import_trees(survey, species_list, infile_plots, infile_trees, format, verbose=None):
    """ Function to import_modules tree data from natural forest and plantations the 2010 file format

        :param survey:  A survey object into which the plot information will be added
        :param species_list:  A list with tree species names as exported from the Collect species list
        :param infile_plots:  The file path to the  plot data
        :param infile_trees:  The file path to the single tree data
        :param format:  The data format either 2010 or 2015
        :type survey: :class:`~model.class_lib.Survey`
        :type species_list: A dictionary with instances of :class:`~model.class_lib.Species`
        :type infile_plots:  file path
        :type infile_trees:  file path
        :type format:  string
        :return: If executed as script a file with the single tree information that can be imported in to OF Collect.
         Otherwise an updated survey object
        :rtype: :class:`~model.class_lib.Survey` / CSV File

        - **Example**  how to use as script::

            :Example usage:
            python import_trees.py Datos_generales_2010.csv Nativo_2010.csv arbol_especie.csv arboles_nativo_2010.csv

        .. note:: For the 2015 format specify the same file plot file for the parameters "*infile_trees*" and
            "*infile_plots"*!

        """

    start = time.time()
    now = datetime.datetime.now()
    info_msg = ' Started the import_modules of single tree information {date}'. \
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
        #For the 2010 plantations the plot information is only available on the plot level!
        import_plots_2010.import_fni_plots_2010(survey, species_list, infile_plots)
        #TODO currently the import_fni_plot function writes into the same logfile
        import_arbol_2010.import_fni_trees_2010(survey, species_list, infile_trees)
    elif format == '2015':
        import_arbol_2015.import_fni_trees_2015(survey, species_list, infile_trees)
    else:
        error_msg ="The file format {format} is unkown.".format(format=format)
        logging.error(error_msg)
        print(error_msg)
        sys.exit(1)

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
    from utils import tools_lib

    parser = argparse.ArgumentParser(
        description='Function to create csv of the single tree information')
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument('InFileNamePlots', type=str, help="Input csv file with 2010 single tree data")
    parser.add_argument('InFileNameTrees', type=str, help="Input csv file with 2010 single tree data")
    parser.add_argument("InFileNameSpecies", type=str,
                        help="Input csv file with tree species in the Collect format")
    parser.add_argument("OutFileName", type=str, help="Outputfile Name")
    parser.add_argument("-f","--format", choices= ['2010','2015'], help="The data format either \"2010\" or \"2015\"")
    parser.add_argument("-log", "--LogFileName", type=str, help="Filepath for the logfile")

    args = parser.parse_args()
    InFileNamePlots = os.path.normpath(args.InFileNamePlots)
    InFileNameTrees = os.path.normpath(args.InFileNameTrees)
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

    if format not in ['2010','2015']:
        error_msg = " The specified format: \"{format}\" is currently not supported".format(format=format)
        print error_msg
        sys.exit(0)

    if format == '2010':
        survey = tools_lib.import_survey(InFileNameTrees, 'p_muestreo_pl', 1)
    if format == '2015':
        survey = tools_lib.import_survey(InFileNameTrees, 'nombre_pm', 1)
    species_list = tools_lib.import_species_list(InFileNameSpecies)
    import_trees(survey, species_list, InFileNamePlots, InFileNameTrees, format, verbose)
    survey.export_arbol_file(OutFileName)
