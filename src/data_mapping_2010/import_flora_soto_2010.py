#!/usr/bin/env python
# -*- coding: utf-8 -*-s
"""This module provides the functionality to import_modules the flora records for soto bosque in to 2010 data format. The information will
will become visible in the tab "Cobertura / Flora" in OF Collect. It can be used as a regurlar python module
in a python program or directly called as a python script from the console.
"""
import csv
import logging
import os
import random
import string

from model import class_lib
from model import code_lists
from utils import tools_lib


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def import_flora_soto_2010(survey,infile):
    """
    Function to import_modules the flora soto records into the survey

    :param survey:  A survey object into which the plot information will be added
    :param infile:  File path to the 2010 plot data
    :type survey: An instance of :class:`~model.class_lib.Survey`
    :type infile: A file path
    :return: If executed as script a file with the flora soto bosque information that can be imported in to OF Collect.
     Otherwise an updated survey object
    :rtype: :class:`~model.class_lib.Survey` / CSV File

    - **Example**  how to use as script::

        :Example usage:
        python import_flora_soto_2010.py Datos_generales_2010.csv flora_soto_caracter.csv
    """

    with open(infile, 'rb') as csvfile:
        datareader = csv.DictReader(csvfile, delimiter=',')
        plot_counter=[]
        for row in datareader:
            # Here we should replace all empty string with None in the dictonary row
            ID = row['nombre_pm']
            if ID in survey.plots.keys():
                # As many species are in one cell we need to iterate of the cells
                flora_soto_tipo = row['tipoSotobosque']
                if flora_soto_tipo == '':
                    flora_soto_tipo = None
                else:
                    flora_soto_tipo= tools_lib.find_key(code_lists.flora_suelo_tipo, flora_soto_tipo)
                if flora_soto_tipo:
                    if ID not in plot_counter:
                        plot_counter.append(ID)
                    floraSotoA = class_lib.FloraSoto(ID, flora_soto_tipo)
                    floraSotoA.flora_soto_altura = tools_lib.import_variable(row, 'alturaSotobosque (m)', 'float', ID)
                    floraSotoA.flora_soto_altura_unit_name = "metros"
                    survey.plots[ID].flora_soto[id_generator()]= floraSotoA
                    survey.plots[ID].flora_soto_flora_soto_presencia = 1
    info_msg = "Updated the flora soto table for {nplots} plots from the file: {file}" \
        .format(nplots=plot_counter.__len__(), file=os.path.basename(infile))
    logging.info(info_msg)
    print(info_msg)