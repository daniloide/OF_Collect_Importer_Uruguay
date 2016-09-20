#!/usr/bin/env python
# -*- coding: utf-8 -*-s
"""This module provides the functionality to import_modules the soil flora records in to 2010 data format. The information will
will become visible in the tab "Relieve/ Suelo" in OF Collect when the csv is imported.
"""
import csv
import logging
import os

from src.model import class_lib
from src.utils import tools_lib


def import_flora_suelo_2010(survey,species_list, infile):
    """
    Function to import_modules the flora suelo records into the survey

    :param survey:  A survey object into which the plot information will be added
    :param species_list: A list with the soil species names as exported from the OF Collect species list
    :param infile:  File path to the 2010 plot data
    :type survey: An instance of :class:`~model.class_lib.Survey`
    :type infile: A file path
    :type species_list: A dictionary with instances of :class:`~model.class_lib.Species`
    :return: If executed as script a file with the soil flora records that can be imported in to OF Collect.
     Otherwise an updated survey object
    :rtype: :class:`~model.class_lib.Survey` / CSV File

    - **Example**  how to use as script::

        :Example usage:
        python import_flora_suelo_2010.py Datos_generales_2010.csv suelo_especie.csv flora_suelo_2010.csv
    """

    with open(infile, 'rb') as csvfile:
        datareader = csv.DictReader(csvfile, delimiter=',')
        plot_counter=[]
        for row in datareader:
            # Here we should replace all empty string with None in the dictonary row
            ID = row['nombre_pm']
            if ID in survey.plots.keys():
                if ID not in plot_counter:
                    plot_counter.append(ID)
                # As many species are in one cell we need to iterate of the cells
                flora_str =str.replace(row['flora_fl'],'y',',')
                flora_str = str.split(flora_str,',')
                if flora_str not in ['',' ']:
                    for i in flora_str:
                        index = tools_lib.find_species_common(species_list, i)
                        if index.__len__() > 0:
                            floraSueloA = class_lib.FloraSuelo(ID, species_list[index].species_code)
                            floraSueloA.flora_suelo_especie_scientific_name = species_list[index].scientific_name
                            survey.plots[ID].flora_suelo[floraSueloA.flora_suelo_especies_code] = floraSueloA
                            #Set the plot variable  soto precencia to 'si'
                            survey.plots[ID].flora_soto_flora_soto_presencia = 1
                        else:
                            warn_msg = 'Species "{species}" on plot {plotid} is not in the flora suelo species list'\
                                .format(species=i,plotid=ID)
                            logging.warn(warn_msg)
                else:
                    warn_msg = 'Found empty string for variable "flora_fl" in plot {plotid}'\
                        .format(plotid=ID)
                    logging.warn(warn_msg)
    info_msg = "Updated the flora suelo table for {nplots} plots from the file: {file}" \
        .format(nplots=plot_counter.__len__(), file=os.path.basename(infile))
    logging.info(info_msg)
    print(info_msg)