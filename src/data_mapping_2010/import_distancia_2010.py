#!/usr/bin/env python
# -*- coding: utf-8 -*-s
"""This module provides the functionality to import_modules the distance records in to 2010 data format. The information will
will become visible in the tab "Distancía" in OF Collect. It can be used as a general python module
in a python program are called as a python script from the console.
"""
import csv
import logging
import os

from model import class_lib
from utils import tools_lib


def import_distancia_2010(survey, infile):
    """
    Function to import_modules the distance records in the 2010 data format into the survey

    :param survey:  A survey object into which the plot information will be added
    :param infile:  he file path to the 2010 single tree data
    :type survey: An instance of :class:`~model.class_lib.Survey`
    :type infile: A file path
    :return: If executed as script a file with the distance information that can be imported in to OF Collect.
     Otherwise an updated survey object
    :rtype: :class:`~model.class_lib.Survey` / CSV File
    """

    with open(infile, 'rb') as csvfile:
        datareader = csv.DictReader(csvfile, delimiter=',')
        plot_counter=[]
        for row in datareader:
            ID = row['nombre_pm']
            if ID in survey.plots.keys():
                if ID not in plot_counter:
                    plot_counter.append(ID)
                position = 1
                censo = 1

                # Adding the distance infomation carretera vecinal
                if row.has_key('carreteraCaminoVecinal') and row['carreteraCaminoVecinal'] not in ['', ' ']:
                    carreteraVecinal = class_lib.Distance(ID)
                    carreteraVecinal.parcela_pm_censo = censo
                    carreteraVecinal.distancia_position = position
                    carreteraVecinal.distancia_kilometros_unit_name = 'kilometros'
                    carreteraVecinal.distancia_categoria = 1
                    carreteraVecinal.distancia_camino_estado = '-'
                    carreteraVecinal.distancia_kilometros = \
                        tools_lib.import_variable(row, 'carreteraCaminoVecinal', 'int', ID)

                # Adding the distance infomation camino vecinal
                if row.has_key('caminoVecinalCaminoAcceso') and row['caminoVecinalCaminoAcceso'] not in ['', ' ']:
                    caminoVecinal = class_lib.Distance(ID)
                    caminoVecinal.parcela_pm_censo = censo
                    caminoVecinal.distancia_position = position
                    caminoVecinal.distancia_kilometros_unit_name = 'kilometros'
                    caminoVecinal.distancia_categoria = 2
                    caminoVecinal.distancia_camino_estado = '-'
                    caminoVecinal.distancia_kilometros =\
                        tools_lib.import_variable(row, 'caminoVecinalCaminoAcceso', 'int', ID)

                # Adding the distance infomation camino accesso
                if row.has_key('caminoAccesoPuntoGPS') and row['caminoAccesoPuntoGPS'] not in ['', ' ']:
                    caminoAccesso = class_lib.Distance(ID)
                    caminoAccesso.parcela_pm_censo = censo
                    caminoAccesso.distancia_position = position
                    caminoAccesso.distancia_kilometros_unit_name = 'kilometros'
                    caminoAccesso.distancia_categoria = 3
                    caminoAccesso.distancia_camino_estado = '-'
                    caminoAccesso.distancia_kilometros = \
                        tools_lib.import_variable(row, 'caminoAccesoPuntoGPS', 'int', ID)

                # Adding the distance infomation PuntoGPSCentroParcella
                if row.has_key('rumboCaminoCentroParcela') and row['rumboCaminoCentroParcela'] not in ['', ' ']:
                    puntoGPSCentroParcella = class_lib.Distance(ID)
                    puntoGPSCentroParcella.parcela_pm_censo = censo
                    puntoGPSCentroParcella.distancia_position = position
                    puntoGPSCentroParcella.distancia_categoria = 4
                    puntoGPSCentroParcella.distancia_kilometros_unit_name = 'kilometros'
                    puntoGPSCentroParcella.distancia_camino_estado = '-'
                    puntoGPSCentroParcella.rumbo_punto_gps_centro =\
                        tools_lib.import_variable(row, 'rumboCaminoCentroParcela', 'int', ID)

                    if row.has_key('puntoGPSCentroParcela') and row['puntoGPSCentroParcela'] not in ['', ' ']:
                            puntoGPSCentroParcella.distancia_kilometros = \
                                tools_lib.import_variable(row, 'puntoGPSCentroParcela', 'int', ID)

                #Adding the distance instances to the survey
                try:
                    survey.plots[ID].distances['1'] = carreteraVecinal
                except:
                    warn_msg = 'Could not find information on distance "carreteraVecinal" on plot: {plotid}.' \
                        .format( plotid=ID)
                    logging.warning(warn_msg)
                try:
                    survey.plots[ID].distances['2'] = caminoVecinal
                except:
                    warn_msg = 'Could not find information on distance "caminoVecinal" on plot: {plotid}.' \
                        .format( plotid=ID)
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
                        .format( plotid=ID)
                    logging.warning(warn_msg)

        info_msg = "Updated the distance table for {nplots} plots from the file: {file}" \
            .format(nplots=plot_counter.__len__(), file=os.path.basename(infile))
        logging.info(info_msg)
        print(info_msg)