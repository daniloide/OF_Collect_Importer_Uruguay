#!/usr/bin/env python
# -*- coding: utf-8 -*-s
import csv
import logging
import os

from model import class_lib
from utils import tools_lib


def import_distanca_2015(survey, infile):
    """
    Function to import_modules the distance records into the survey

    :param survey: An instance of base class Survey
    :param infile: The file path to the input file
    """

    with open(infile, 'rb') as csvfile:
        datareader = csv.DictReader(csvfile, delimiter=',')
        counter=[]
        for row in datareader:
            ID = row['nombre_pm']
            if ID in survey.plots.keys():
                position = 1
                censo = 1
                if row['name'] =='Distancias':
                    # Adding the distance infomation carretera vecinal
                    if row.has_key('carreteraCaminoVecinal') and row['carreteraCaminoVecinal'] not in ['', ' ']:
                        carreteraVecinal = class_lib.Distance(ID)
                        carreteraVecinal.parcela_pm_censo = censo
                        carreteraVecinal.distancia_position = position
                        carreteraVecinal.distancia_kilometros_unit_name = 'kilometros'
                        carreteraVecinal.distancia_categoria = 1
                        carreteraVecinal.distancia_camino_estado = '-'
                        if ID not in counter:
                            counter.append(ID)
                        carreteraVecinal.distancia_kilometros = \
                            tools_lib.import_variable(row, 'carreteraCaminoVecinal', 'float', ID)

                    # Adding the distance infomation camino vecinal
                    if row.has_key('caminoVecinalCaminoAcceso') and row['caminoVecinalCaminoAcceso'] not in ['',' ']:
                        caminoVecinal = class_lib.Distance(ID)
                        caminoVecinal.parcela_pm_censo = censo
                        caminoVecinal.distancia_position = position
                        caminoVecinal.distancia_kilometros_unit_name = 'kilometros'
                        caminoVecinal.distancia_categoria = 2
                        caminoVecinal.distancia_camino_estado = '-'
                        if ID not in counter:
                            counter.append(ID)
                        caminoVecinal.distancia_kilometros =\
                            tools_lib.import_variable(row, 'caminoVecinalCaminoAcceso', 'float', ID)

                   # Adding the distance infomation camino accesso
                    if row.has_key('caminoAccesoPuntoGPS') and row['caminoAccesoPuntoGPS'] not in ['', ' ']:
                        caminoAccesso = class_lib.Distance(ID)
                        caminoAccesso.parcela_pm_censo = censo
                        caminoAccesso.distancia_position = position
                        caminoAccesso.distancia_kilometros_unit_name = 'kilometros'
                        caminoAccesso.distancia_categoria = 3
                        caminoAccesso.distancia_camino_estado = '-'
                        if ID not in counter:
                            counter.append(ID)
                        caminoAccesso.distancia_kilometros = \
                            tools_lib.import_variable(row, 'caminoAccesoPuntoGPS', 'float', ID)

                    # Adding the distance infomation rumboCaminoCentroParcela
                    if row.has_key('rumboCaminoCentroParcela') and row['rumboCaminoCentroParcela'] not in ['',' ']:
                        puntoGPSCentroParcella = class_lib.Distance(ID)
                        puntoGPSCentroParcella.parcela_pm_censo = censo
                        puntoGPSCentroParcella.distancia_position = position
                        puntoGPSCentroParcella.distancia_categoria = 4
                        puntoGPSCentroParcella.distancia_kilometros_unit_name = 'kilometros'
                        puntoGPSCentroParcella.distancia_camino_estado = '-'
                        if ID not in counter:
                            counter.append(ID)
                        puntoGPSCentroParcella.rumbo_punto_gps_centro = \
                            tools_lib.import_variable(row, 'rumboCaminoCentroParcela', 'int', ID)

                    # Adding the distance infomation PuntoGPSCentroParcella
                    if row.has_key('puntoGPSCentroParcela') and row['puntoGPSCentroParcela'] not in ['',' ']:
                        puntoGPSCentroParcella.distancia_kilometros =\
                            tools_lib.import_variable(row, 'puntoGPSCentroParcela', 'float', ID)

                    # Adding the distance instances to the survey
                    try:
                        survey.plots[ID].distances['1'] = carreteraVecinal
                    except:
                        warn_msg = 'Could not find information on distance "carreteraVecinal" on plot: {plotid}.' \
                                    .format(plotid=ID)
                        logging.warning(warn_msg)
                    try:
                        survey.plots[ID].distances['2'] = caminoVecinal
                    except:
                        warn_msg = 'Could not find information on distance "caminoVecinal" on plot: {plotid}.' \
                                    .format(plotid=ID)
                        logging.warning(warn_msg)
                    try:
                        survey.plots[ID].distances['3'] = caminoAccesso
                    except:
                        warn_msg = 'Could not find information on distance "caminoAcceso" on plot: {plotid}.' \
                                  .format(plotid=ID)
                        logging.warning(warn_msg)
                    try:
                        survey.plots[ID].distances['4'] = puntoGPSCentroParcella
                    except:
                         warn_msg = 'Could not find information on distance "puntoGPSCentroParcella" on plot: {plotid}.' \
                                  .format(plotid=ID)
                         logging.warning(warn_msg)

    info_msg = "Updated the distance table for {nplots} plots from the file: {file}" \
                  .format(nplots=counter.__len__(), file=os.path.basename(infile))
    print(info_msg)
    logging.info(info_msg)
