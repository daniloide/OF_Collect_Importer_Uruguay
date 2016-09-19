#!/usr/bin/env python
# -*- coding: utf-8 -*-s
import csv
import logging
import os

from model import class_lib
from model import code_lists
from utils import tools_lib


def import_flora_suelo_2015(survey,species_list, infile):
    """
    Function to import_modules the flora suelo records into the survey

    :param survey: An instance of base class Survey
    :param species_list: A dictonary with all species
    :param infile: The file path to the input file
    """

    with open(infile, 'rb') as csvfile:
        datareader = csv.DictReader(csvfile, delimiter=',')
        plot_counter=[]
        for row in datareader:
            ID = row['nombre_pm']
            if ID in survey.plots.keys():
                if row['name'] == 'FloraDelSuelo':
                    species = ''
                    if row.has_key('nombreCientifico_FloraDelSuelo') and row['nombreCientifico_FloraDelSuelo'] not in ['',' ']:
                        species = row['nombreCientifico_FloraDelSuelo'].strip()
                    if row.has_key('nombreCientifico_floraDelSuelo') and row['nombreCientifico_floraDelSuelo'] not in ['', ' ']:
                        species = row['nombreCientifico_floraDelSuelo'].strip()
                    index = tools_lib.find_species_scientific(species_list, species)
                    if index.__len__() > 0:
                        floraSueloA = class_lib.FloraSuelo(ID, species_list[index[0]].species_code)
                        floraSueloA.flora_suelo_especie_scientific_name = species_list[index[0]].scientific_name
                        floraSueloA.flora_suelo_especie_vernacular_name = species_list[index[0]].common_name
                        if row.has_key('Frecuencia_FloraDelSuelo'):
                            floraSueloA.flora_suelo_freq = tools_lib.import_variable(row, 'Frecuencia_FloraDelSuelo',
                                                                                          'code', ID,
                                                                                     code_lists.flora_suelo_freq)
                        if row.has_key('frecuencia_floraDelSuelo'):
                            floraSueloA.flora_suelo_freq = tools_lib.import_variable(row,
                                                                                          'frecuencia_floraDelSuelo',
                                                                                          'code', ID,
                                                                                     code_lists.flora_suelo_freq)
                        survey.plots[ID].flora_suelo[floraSueloA.flora_suelo_especies_code] = floraSueloA
                        survey.plots[ID].flora_soto_flora_soto_presencia = 1
                        if ID not in plot_counter:
                            plot_counter.append(ID)
                    else:
                        warn_msg = 'Flora suelo species "{species}" on plot {plotid} is not in the flora suelo species list in plot {plotid}'\
                                    .format(species=species,plotid=ID)
                        logging.warn(warn_msg)
    info_msg = "Updated the flora suelo table for {nplots} plots from the file: {file}" \
        .format(nplots=plot_counter.__len__(), file=os.path.basename(infile))
    print(info_msg)
    logging.info(info_msg)
