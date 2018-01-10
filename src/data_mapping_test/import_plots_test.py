#!/usr/bin/env python
# -*- coding: utf-8 -*-s

import csv
import logging
import os
import sys

from src.model import class_lib
from src.model import code_lists
from src.utils import tools_lib


def import_fni_plots_test(survey,species_list,infile):
    """Function to import_modules plot data in the 2015 file format

       :param survey: An instance of class survey
       :param infile: The file path to the tetst plot data
       """

    # Check if survey is of class survey
    try:
        isinstance(survey, class_lib.Survey)
        print "Using survey {}".format(survey.survey_id)
    except:
        print "Survey is not of class Survey"
        sys.exit(0)

    # Check if files exits and readable
    try:
        f = open(infile, 'r')
    except IOError:
        print "Input file {} is missing or is not readable".format(infile)
        sys.exit(0)

    with open(infile, 'rb') as csvfile:
        datareader = csv.DictReader(csvfile, delimiter=',')
        counter = []
        for row in datareader:
            ID = row['nombre_pm']
            if ID in survey.plots.keys():
                if ID not in counter:
                    counter.append(ID)

                #if row['name'] == 'DatosGenerales':
                survey.plots[ID].general_datos_parcela_bosque_tipo =\
                    tools_lib.import_variable(row, 'tipoDeBosq', 'code', ID, code_lists.bosque_tipo)

                survey.plots[ID].general_datos_parcela_bosque_sub_tipo =\
                    tools_lib.import_variable(row, 'subbosque', 'code', ID, code_lists.subbosque_tipo)
                print(row['subbosque'])
                print(tools_lib.import_variable(row, 'subbosque', 'code', ID, code_lists.subbosque_tipo))

                survey.plots[ID].pm_departamento = \
                    tools_lib.import_variable(row, 'departament', 'code', ID, code_lists.departamento)

                date = str.split(row['fecha'], '/')
                try:
                    date.__len__() == 3
                    survey.plots[ID].general_datos_parcela_fecha_observation_year = date[2]
                    survey.plots[ID].general_datos_parcela_fecha_observation_month = date[1]
                    survey.plots[ID].general_datos_parcela_fecha_observation_day = date[0]
                except ValueError:
                    warn_msg = 'Cannot convert the variable fecha wit value :\"{date}\" into a date \
                                for plot {plotid}'.format(date=row['fecha'], plotid=ID)
                    logging.warn(warn_msg)
 

                #if row['name'] == 'CoordenadasParcela':
                survey.plots[ID].parcela_coordenadas_gps_coord_x = tools_lib.import_variable(row, 'oeste', 'float', ID)
                survey.plots[ID].parcela_coordenadas_gps_coord_y = tools_lib.import_variable(row, 'sur', 'float', ID)
                survey.plots[ID].parcela_coordenadas_gps_coord_srs = 'EPSG:4326'
                
                survey.plots[ID].pm_subcuenca = row ['SubCuenca']

    info_msg = "Updated the plot information for {nplots} plots from the file: {file}"\
                    .format(nplots=counter.__len__(),file=os.path.basename(infile))
    print(info_msg)
    logging.info(info_msg)
