#!/usr/bin/env python
# -*- coding: utf-8 -*-s

import csv
import logging
import os

from model import class_lib
from utils import tools_lib


def import_regeneracion_2015(survey,species_list,infile):
    """ Function to import_modules invasores records from plots in the 2015 file format

    :param survey:  An instance of the survey class
    :param species_list: Dictonary with the invasora species
    :param infile:  The file path to the import_modules file
    """
    with open(infile, 'rb') as data:
        datareader = csv.DictReader(data, delimiter=',')
        counter = []
        for row in datareader:
            ID = row['nombre_pm']
            if ID in survey.plots.keys():
                if row['name'] == 'Regeneracion Natural':
                    if row.has_key('nombrecient_regnat') and row['nombrecient_regnat'] not in ['',' ']:
                        species = row['nombrecient_regnat'].strip()
                        index = tools_lib.find_species_scientific(species_list, species)
                        if index.__len__() > 0:
                            regeneracionA = class_lib.Regeneracion(ID, species_list[index[0]].species_code)
                            regeneracionA.regen_especie_scientific_name = species_list[index[0]].scientific_name
                            regeneracionA.regen_especie_vernacular_name = species_list[index[0]].common_name
                            if ID not in counter:
                                counter.append(ID)
                            regeneracionA.regen_subparcela_id = tools_lib.import_variable(row, 'subparcela_regnat',
                                                                                               'int', ID)
                            if row.has_key('Rumbo_regnat'):
                                regeneracionA.regen_rumbo = tools_lib.import_variable(row, 'Rumbo_regnat',
                                                                                               'int', ID)
                            if row.has_key('Rumbo'):
                                regeneracionA.regen_rumbo = tools_lib.import_variable(row, 'Rumbo',
                                                                                               'int', ID)
                            if row.has_key('Distancia_regnat'):
                                regeneracionA.regen_distancia = tools_lib.import_variable(row, 'Distancia_regnat',
                                                                                               'float', ID)
                            if row.has_key('Distancia'):
                                regeneracionA.regen_distancia = tools_lib.import_variable(row, 'Distancia',
                                                                                               'float', ID)
                            regeneracionA.regen_frec = tools_lib.import_variable(row, 'cant_regnat',
                                                                                               'int', ID)

                            regeneracionA.regen_distancia_unit_name = 'metros'
                            regeneracionA.regen_rumbo_unit_name = 'grados'
                            survey.plots[ID].regeneracion[regeneracionA.regen_especie_code] = regeneracionA
    info_msg = "Updated the regeneration table for {nplots} plots from the file: {file}"\
                    .format(nplots=counter.__len__(),file=os.path.basename(infile))
    print(info_msg)
    logging.info(info_msg)
