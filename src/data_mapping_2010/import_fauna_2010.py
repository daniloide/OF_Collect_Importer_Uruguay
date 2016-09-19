#!/usr/bin/env python
# -*- coding: utf-8 -*-s
"""This module provides the functionality to import_modules the flauna records in to 2010 data format. The information will
will become visible in the "Fauna" tab in OF Collect. Four groups of vertebrates are imported: "*Mamiferos*","*Aves*","*Anfibios*" and
"*Reptiles*". For each of the four group a separate species list is required.
"""
import csv
import logging
import os

from model import class_lib
from utils import tools_lib


def import_fauna_2010(survey,species_list,infile):
    """
    Function to import_modules the fauna records in the 2010 data format

    :param survey:  A survey object into which the plot information will be added
    :param species_list: A list with the species names of all four vertebrate groups exported from the OF Collect species list
    :param infile:  File path to the 2010 fauna data
    :type survey: An instance of :class:`~model.class_lib.Survey`
    :type infile: A file path
    :type species_list: A dictionary with instances of :class:`~model.class_lib.Species`
    :return: If executed as script a file with the soil flora records that can be imported in to OF Collect.
     Otherwise an updated survey object
    :rtype: :class:`~model.class_lib.Survey` / CSV File

    - **Example**  how to use as script::

        :Example usage:
        python import_fauna_2010.py fauna_2010.csv fauna_aves_especie.csv fauna_mamiferos_especie.csv
                fauna_reptiles_especie.csv fauna_anfibios_especie.csv  out
    """

    with open(infile, 'rb') as csvfile:
        datareader = csv.DictReader(csvfile, delimiter=',')
        plot_counter=[]
        for row in datareader:
            ID = row['p_muestreo_pl']
            if ID in survey.plots.keys():
                if ID not in plot_counter:
                    plot_counter.append(ID)
                if row['Fauna cientif'] not in ['',' ']:
                    index = tools_lib.find_species_scientific(species_list, row['Fauna cientif'])
                    if index.__len__()>0:
                        for i in index:
                            faunaA = class_lib.Fauna(ID, species_list[i].species_code)
                            faunaA.position = 1
                            faunaA.fauna_cant = row['frecuencia']
                            faunaA.fauna_especie_scientific_name = species_list[i].scientific_name
                            faunaA.fauna_especie_vernacular_name = species_list[i].common_name
                            #The variable tipo observacopm is not exiting in the 2010 dataset
                            faunaA.fauna_tipo_observacion = '-'
                            tipo = row['tipo']
                            if tipo == 'Ave':
                                survey.plots[ID].fauna_aves[faunaA.fauna_especies_code] = faunaA
                            elif tipo == 'Mamifero':
                                survey.plots[ID].fauna_mamiferos[faunaA.fauna_especies_code] = faunaA
                            elif tipo == 'Reptil':
                                survey.plots[ID].fauna_reptiles[faunaA.fauna_especies_code] = faunaA
                            elif tipo == 'Anfibio':
                                survey.plots[ID].fauna_anfibios[faunaA.fauna_especies_code] = faunaA
                            else:
                                warnin_msg = 'Cannot find the species type {tipo} does not belong to the four vertebrate' \
                                             ' groups for plot {plotid}' \
                                    .format(tipo= row['tipo'], plotid=ID)
                                logging.warn(warnin_msg)

                    else:
                        warnin_msg = 'Cannot find species {species} in the species list for plot {plotid}' \
                            .format(species=row['Fauna cientif'],plotid=ID)
                        logging.warn(warnin_msg)

                else:
                    warnin_msg = 'Found empty string for variable "Fauna cientif" on plot {plotid}'\
                    .format(plotid=ID)
                    logging.warn(warnin_msg)

    info_msg = "Updated the fauna tables for {nplots} plots from the file: {file}" \
        .format(nplots=plot_counter.__len__(), file=os.path.basename(infile))
    logging.info(info_msg)
    print(info_msg)