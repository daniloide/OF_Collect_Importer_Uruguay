#!/usr/bin/env python
# -*- coding: utf-8 -*-s

import csv
import logging
import os

from model import code_lists
from utils import tools_lib


def import_fotos_2015(survey, infile):
    """ Function to import_modules foto data from plots in the 2015 file format

    :param survey:  An instance of the survey class
    :param infile:  The file path to the import_modules file
    """

    with open(infile, 'rb') as data:
        datareader = csv.DictReader(data, delimiter=',')
        counter = []
        for row in datareader:
            ID = row['nombre_pm']
            if ID in survey.plots.keys():
                if row['name'] == 'Fotos':
                    foto_id = row['foto']
                    # We add only a foto if it is not in the foto list of this plot
                    if foto_id not in survey.plots[ID].fotos.keys():
                        survey.plots[ID].add_foto(foto_id)
                        if ID not in counter:
                            counter.append(ID)
                    survey.plots[ID].fotos[foto_id].foto_position = 1
                    survey.plots[ID].fotos[foto_id].foto_tipo = \
                        tools_lib.import_variable(row, 'tipoFoto', 'code', ID, code_lists.foto_tipo)
                    survey.plots[ID].fotos[foto_id].foto_desc = tools_lib.import_variable(row, 'descr', 'string', ID)
                    survey.plots[ID].fotos[foto_id].foto_archivo = foto_id
                    if row.has_key('lat_foto'):
                        survey.plots[ID].fotos[foto_id].foto_lat = \
                            tools_lib.import_variable(row, 'lat_foto', 'float', ID)
                    elif row.has_key('Lat_foto'):
                        survey.plots[ID].fotos[foto_id].foto_lat = \
                            tools_lib.import_variable(row, 'Lat_foto', 'float', ID)
                    if row.has_key('lon_foto'):
                        survey.plots[ID].fotos[foto_id].foto_lon = \
                            tools_lib.import_variable(row, 'lon_foto', 'float', ID)
                    elif row.has_key('Lon_foto'):
                        survey.plots[ID].fotos[foto_id].foto_lon = \
                            tools_lib.import_variable(row, 'Lon_foto', 'float', ID)
                    survey.plots[ID].fotos[foto_id].foto_systema_referencia = 'EPSG:4326'
    info_msg = "Updated the foto table for {nplots} plots from the file: {file}" \
        .format(nplots=counter.__len__(), file=os.path.basename(infile))
    print(info_msg)
    logging.info(info_msg)
