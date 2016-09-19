#!/usr/bin/env python
# -*- coding: utf-8 -*-s

import csv
import logging
import os

from model import class_lib
from model import code_lists
from utils import tools_lib


def import_invasoras_2015(survey,species_list,infile):
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
                if row['name'] == 'EspeciesInvasoras':
                    if row.has_key('nombreCientifico_EspeciesInvasoras') and row['nombreCientifico_EspeciesInvasoras'] not in ['',' ']:
                        species = row['nombreCientifico_EspeciesInvasoras'].strip()
                        index = tools_lib.find_species_scientific(species_list, species)
                        if index.__len__() > 0:
                            invasoraA = class_lib.Invasora(ID, species_list[index[0]].species_code)
                            invasoraA.invasora_especie_scientific_name = species_list[index[0]].scientific_name
                            invasoraA.invasora_especie_vernacular_name = species_list[index[0]].common_name
                            invasoraA.invasora_categoria = \
                                tools_lib.import_variable(row, 'Categoría_EspeciesInvasoras', 'code',
                                                          ID, code_lists.invasora_categoria)
                            invasoraA.invasora_severidad = \
                                tools_lib.import_variable(row, 'severidad_invasora', 'code', ID,
                                                          code_lists.invasora_severidad)
                            survey.plots[ID].invasoras[invasoraA.invasora_especie_code] = invasoraA
                            if ID not in counter:
                                counter.append(ID)

    info_msg = "Updated the invasores table for {nplots} plots from the file: {file}" \
        .format(nplots=counter.__len__(), file=os.path.basename(infile))
    print(info_msg)
    logging.info(info_msg)