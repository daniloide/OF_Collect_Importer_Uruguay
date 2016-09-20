#!/usr/bin/env python
# -*- coding: utf-8 -*-s
import csv
import logging
import os
import random
import string

from src.model import class_lib
from src.model import code_lists
from src.utils import tools_lib


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def import_flora_soto_2015(survey,infile):
    """
    Function to import_modules the flora soto records into the survey

    :param survey: An instance of base class Survey
    :param infile: The file path to the input file
    """

    with open(infile, 'rb') as csvfile:
        datareader = csv.DictReader(csvfile, delimiter=',')
        counter=[]
        for row in datareader:
            # Here we should replace all empty string with None in the dictonary row
            ID = row['nombre_pm']
            if ID in survey.plots.keys():
                if row['name'] == 'Flora':
                    flora_soto_tipo = tools_lib.import_variable(row, 'tipoSotobosque', 'code', ID, code_lists.flora_suelo_tipo)
                    if flora_soto_tipo:
                        floraSotoA = class_lib.FloraSoto(ID, flora_soto_tipo)
                        floraSotoA.flora_soto_altura = tools_lib.import_variable(row, 'alturaSotobosque', 'float', ID)
                        floraSotoA.flora_soto_altura_unit_name = "metros"
                        survey.plots[ID].flora_soto[id_generator()]= floraSotoA
                        survey.plots[ID].flora_soto_flora_soto_presencia = 1
                        if ID not in counter:
                            counter.append(ID)
    info_msg = "Updated the flora soto table for {nplots} plots from the file: {file}" \
        .format(nplots=counter.__len__(), file=os.path.basename(infile))
    print(info_msg)
    logging.info(info_msg)