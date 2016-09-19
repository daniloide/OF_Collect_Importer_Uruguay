#!/usr/bin/env python
# -*- coding: utf-8 -*-s
import csv
import logging
import os

from model import class_lib
from utils import tools_lib


def import_sanidad_2015(survey,infile):
    """ Function to import_modules sanidad records from plots in the 2015 file format

    :param survey:  An instance of the survey class
    :param infile:  The file path to the import_modules file
    """
    #TODO This function is only a template and will not work in the current version as it is unclear how the sanidad files should be imported
    with open(infile, 'rb') as data:
        datareader = csv.DictReader(data, delimiter=',')
        counter = []
        for row in datareader:
            ID = row['nombre']
            if ID in survey.plots.keys():
                try:
                    numbarb = row['numarb_sanp']
                    sanidadA= class_lib.Sanidad(numbarb)
                except ValueError:
                    warnin_msg = 'Could not use the variable \"numarb_sanp\" with with value: \"{value}\" as id for sanidad of plot {plotid}'\
                        .format(value=row['numarb_sanp'], plotid=ID)
                    logging.warn(warnin_msg)

                if sanidadA:
                    sanidadA.san_dap = tools_lib.import_variable(row, 'dap_sanp', 'float')
                    sanidadA.san_categoria = tools_lib.import_variable(row, 'categoria_sanp', 'int')
                    sanidadA.san_tipo_fuste = tools_lib.import_variable(row, 'tipofuste_sanp', 'int')
                    sanidadA.san_porcopa = tools_lib.import_variable(row, 'porccopa_sanp', 'int')
                    sanidadA.san_porcopa = tools_lib.import_variable(row, 'porccopa_sanp', 'int')

    info_msg = "Updated the equipo table for {nplots} plots from the file: {file}"\
                    .format(nplots=counter.__len__(),file=os.path.basename(infile))
    print(info_msg)
    logging.info(info_msg)
