#!/usr/bin/env python
# -*- coding: utf-8 -*-s
import csv
import logging
import os

from model import class_lib
from utils import tools_lib


def import_fauna_2015(survey,species_list,infile):
    """
    Function to import_modules the fauna records into the survey

    :param survey: An instance of base class Survey
    :param species_list: A dictonary with all fauna species
    :param infile: The file path to the input file
    """

    with open(infile, 'rb') as csvfile:
        datareader = csv.DictReader(csvfile, delimiter=',')
        counter=[]
        for row in datareader:
            ID = row['nombre_pm']
            if ID in survey.plots.keys():
                if row['name'] == 'Fauna':
                    species =''
                    if row.has_key('especie_fauna_cientif') and row['especie_fauna_cientif'] not in ['',' ']:
                        species = row['especie_fauna_cientif'].strip()
                    if row.has_key('especie_fauna') and row['especie_fauna'] not in ['',' ']:
                        species = row['especie_fauna'].strip()
                    if row.has_key('especie_fauna_nombrecientif') and row['especie_fauna_nombrecientif'] not in ['',' ']:
                        species = row['especie_fauna_nombrecientif'].strip()
                    index = tools_lib.find_species_scientific(species_list, species)
                    if index.__len__()>0:
                        faunaA = class_lib.Fauna(ID, species_list[index[0]].species_code)
                        faunaA.fauna_especie_scientific_name = species_list[index[0]].scientific_name
                        faunaA.fauna_especie_vernacular_name = species_list[index[0]].common_name
                        faunaA.fauna_cant = tools_lib.import_variable(row, 'frec', 'float', ID)
                        faunaA.fauna_tipo_observacion = '-'

                        if 'AV' in faunaA.fauna_especies_code:
                            survey.plots[ID].fauna_aves[faunaA.fauna_especies_code] = faunaA
                            if ID not in counter:
                                counter.append(ID)
                        if 'MA' in faunaA.fauna_especies_code:
                            survey.plots[ID].fauna_mamiferos[faunaA.fauna_especies_code] = faunaA
                            if ID not in counter:
                                counter.append(ID)
                        if 'RE' in faunaA.fauna_especies_code:
                            survey.plots[ID].fauna_reptiles[faunaA.fauna_especies_code] = faunaA
                            if ID not in counter:
                                counter.append(ID)
                        if 'AN' in faunaA.fauna_especies_code:
                            survey.plots[ID].fauna_anfibios[faunaA.fauna_especies_code] = faunaA
                            if ID not in counter:
                                counter.append(ID)
                    else:
                        warnin_msg = 'Variable \"especie_fauna_cientif\" with value: \"{value}\" could not be found in the fauna species lists on plot {plotid}'\
                        .format(value=species,plotid=ID)
                        logging.warn(warnin_msg)

    info_msg = "Updated the fauna tables for {nplots} plots from the file: {file}" \
        .format(nplots=counter.__len__(), file=os.path.basename(infile))
    print(info_msg)
    logging.info(info_msg)
