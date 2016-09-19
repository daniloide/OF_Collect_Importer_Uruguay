#!/usr/bin/env python
# -*- coding: utf-8 -*-s

import csv
import logging
import os

from model import class_lib
from model import code_lists
from utils import tools_lib


def import_equipo_2015(survey,infile):
    """ Function to import_modules equipment records from plots in the 2015 file format

    :param survey:  An instance of the survey class
    :param infile:  The file path to the import_modules file
    """
    with open(infile, 'rb') as data:
        datareader = csv.DictReader(data, delimiter=',')
        counter = []
        for row in datareader:
            ID = row['nombre_pm']
            if ID in survey.plots.keys():
                if row['name'] == 'EquipoTrabajo':
                    if row.has_key('Nomb._equ. Trab.') and row['Nomb._equ. Trab.'] not in ['',' ']:
                        nom = tools_lib.import_variable(row, 'Nomb._equ. Trab.', 'string', ID)
                    elif row.has_key('nom._eq.tra') and row['nom._eq.tra'] not in ['',' ']:
                        nom = tools_lib.import_variable(row, 'nom._eq.tra', 'string', ID)

                    if nom not in ['']:
                        equipoA = class_lib.Equipo(nom)
                        equipoA.equipo_cargo = \
                            tools_lib.import_variable(row, 'cargo', 'code', ID, code_lists.equipo_cargo)
                        equipoA.equipo_emp = \
                            tools_lib.import_variable(row, 'empresa', 'string', ID)
                        equipoA.equipo_app = '-'
                        survey.plots[ID].equipo[equipoA.equipo_nom] = equipoA
                        if ID not in counter:
                            counter.append(ID)

    info_msg = "Updated the equipo table for {nplots} plots from the file: {file}" \
        .format(nplots=counter.__len__(), file=os.path.basename(infile))
    print(info_msg)
    logging.info(info_msg)