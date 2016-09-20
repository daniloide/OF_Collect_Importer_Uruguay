#!/usr/bin/env python
# -*- coding: utf-8 -*-s
import csv
import logging
import os

from src.model import code_lists
from src.utils import tools_lib


def import_fni_trees_2015(survey, species_list, infile):
    """ Function to import_modules single tree data in the 2015 file format

    :param survey:  An instance of the survey class
    :param species_list:  An instance of class species
    :param infile:  The file path to the import_modules file
    """

    with open(infile, 'rb') as planilla_bn:
        datareader = csv.DictReader(planilla_bn, delimiter=',')
        counter = []
        for row in datareader:
            ID = row['nombre_pm']
            if ID in survey.plots.keys():
                #print 'Processing PlotID:{:}'.format(ID)
                if ID not in counter:
                    counter.append(ID)
                #TODO Check client favor solution for missin tree ids is

                if row['name'] in ['ParcelasBosqueNatural','ParcelasBosquePlantado']:
                    try:
                        arbol_id = "%d"%float(row['numArbol'])
                    except ValueError:
                        error_msg = " Cannot create a tree id from \"{numArbol}\" for plot {plotid}"\
                                .format(numArbol=row['numArbol'],plotid=ID)
                        logging.error(error_msg)

                    # We add only a tree if it is not in the tree list otherwise we assume that this is a stem of the same tree
                    if arbol_id not in survey.plots[ID].trees.keys():
                        survey.plots[ID].add_tree(arbol_id)

                    # We create artifical stem ids by incrementing the ID for each stem
                    stem_id = survey.plots[ID].trees[arbol_id].stem_count() + 1

                    if row.has_key('radio') and row['radio'] not in ['',' ']:
                        try:
                            radius=float(row['radio'].replace(',','.'))
                            survey.plots[ID].trees[arbol_id].arbol_parcela = tools_lib.convert_arbol_radius(radius)
                        except ValueError:
                            warn_msg = 'Cannot convert the variable radio with value \"{val}\" into an integer number for plot {plotid}'\
                                    .format(val=row['radio'],plotid=ID)
                            logging.warn(warn_msg)
                    else:
                        survey.plots[ID].trees[arbol_id].arbol_parcela = 5


                    # Add stems to the tree
                    dap1 = tools_lib.import_variable(row, 'dap1', 'float', ID)
                    if dap1 is not None:
                        dap1 = dap1 *100

                    dap2 = tools_lib.import_variable(row, 'dap2', 'float', ID)
                    if dap2 is not None:
                        dap2 = dap2*100

                    ht = tools_lib.import_variable(row, 'ht', 'float', ID, treeid=arbol_id)
                    survey.plots[ID].trees[arbol_id].add_stem(stem_id=stem_id, dap1=dap1, dap2=dap2, ht=ht)

                    print 'Stem count:{:}'.format(survey.plots[ID].trees[arbol_id].stem_count())

                    if row.has_key('observaciones2') and row['observaciones2'] not in ['',' ']:
                        survey.plots[ID].trees[arbol_id].stems[stem_id].observacion = \
                            tools_lib.import_variable(row, 'observaciones2', 'string', ID, treeid=arbol_id)

                    if row.has_key('observaciones')and row['observaciones'] not in ['',' ']:
                        survey.plots[ID].trees[arbol_id].stems[stem_id].observacion = \
                            tools_lib.import_variable(row, 'observaciones', 'string', ID, treeid=arbol_id)

                    #Import the attributes for natural forest
                    if row['tipoDeBosque']== "Bosque Nativo":
                        # Check Species Name for natural forests
                        if row.has_key('nombreCientifico_FloraNativa'):
                            index = tools_lib.find_species_scientific(species_list, row['nombreCientifico_FloraNativa'])
                            warn_msg = "Cannot find the tree species \"{species}\" in the species list for tree {treeid} on plot {plotid}". \
                                format(species=row['nombreCientifico_FloraNativa'], treeid=arbol_id, plotid=ID)
                            try:
                                if index.__len__() > 0:
                                    survey.plots[ID].trees[arbol_id].arbol_especie_code = \
                                        species_list[index[0]].species_code
                                    survey.plots[ID].trees[arbol_id].arbol_especie_scientific_name = \
                                        species_list[index[0]].scientific_name
                                    survey.plots[ID].trees[arbol_id].arbol_especie_vernacular_name = \
                                        species_list[index[0]].common_name
                                else:
                                    survey.plots[ID].trees[arbol_id].arbol_especie_code = '-'
                                    logging.warn(warn_msg)
                            except ValueError:
                                logging.warn(warn_msg)

                        survey.plots[ID].trees[arbol_id].stems[stem_id].estrado = \
                                tools_lib.import_variable(row, 'estrato', 'code', ID,
                                                          codelist=code_lists.arbol_estrato,
                                                          treeid=arbol_id)
                        survey.plots[ID].trees[arbol_id].stems[stem_id].rango_edad = \
                                tools_lib.import_variable(row, 'rangoEdad', 'code', ID,
                                                          codelist=code_lists.arbol_rango_edad, treeid=arbol_id)
                    #Import the attribute for plantaciones
                    if row['tipoDeBosque'] == "Plantación":
                        #Get the species name
                        plant_especies = row['genero'] + ' ' + row['especie_plantacion']
                        index = tools_lib.find_species_scientific(species_list, plant_especies)
                        warn_msg = "Could not find the species \"{species}\" in the species code list for plot: {plotid}" \
                            .format(species=plant_especies, plotid=ID)
                        if index is not None and index.__len__() > 0:
                            survey.plots[ID].trees[arbol_id].arbol_especie_code = \
                                species_list[index[0]].species_code
                            survey.plots[ID].trees[arbol_id].arbol_especie_scientific_name = \
                                species_list[index[0]].scientific_name
                            survey.plots[ID].trees[arbol_id].arbol_especie_vernacular_name = \
                                species_list[index[0]].common_name
                        else:
                            survey.plots[ID].trees[arbol_id].arbol_especie_code = '-'
                            logging.warn(warn_msg)

                        survey.plots[ID].trees[arbol_id].stems[stem_id].distancia =\
                                    tools_lib.import_variable(row, 'distancia_arbolCentroParcela', 'float', ID,
                                                              treeid=arbol_id)
                        survey.plots[ID].trees[arbol_id].stems[stem_id].rumbo = \
                                tools_lib.import_variable(row, 'direccionRumbo', 'int', ID, treeid=arbol_id)
                        survey.plots[ID].trees[arbol_id].stems[stem_id].hc = \
                                tools_lib.import_variable(row, 'hc', 'float', ID, treeid=arbol_id)
                        survey.plots[ID].trees[arbol_id].stems[stem_id].hp = \
                                tools_lib.import_variable(row, 'hPoda', 'float', ID, treeid=arbol_id)
                        survey.plots[ID].trees[arbol_id].stems[stem_id].forma = \
                                tools_lib.import_variable(row, 'forma', 'code', ID, codelist=code_lists.arbol_forma,
                                                          treeid=arbol_id)
                        survey.plots[ID].trees[arbol_id].stems[stem_id].corteza_espesor = \
                                tools_lib.import_variable(row, 'espesorCorteza', 'float', ID, treeid=arbol_id)

                    survey.plots[ID].trees[arbol_id].stems[stem_id].dap1_unit_name = 'centimetros'
                    survey.plots[ID].trees[arbol_id].stems[stem_id].dap2_unit_name = 'centimetros'
                    survey.plots[ID].trees[arbol_id].stems[stem_id].dap_unit_name = 'centimetros'
                    survey.plots[ID].trees[arbol_id].stems[stem_id].ht_unit_name = 'metros'
                    survey.plots[ID].trees[arbol_id].stems[stem_id].hp_unit_name = 'metros'
                    survey.plots[ID].trees[arbol_id].stems[stem_id].distancia_unit_name = 'metros'
                    survey.plots[ID].trees[arbol_id].stems[stem_id].hc_unit_name = 'metros'
                    survey.plots[ID].trees[arbol_id].stems[stem_id].corteza_espesor_unit_name = 'centimetros'
                    #survey.plots[ID].trees[arbol_id].stems[stem_id].rumbo_unit_name = 'grados'

    info_msg = "Updated the tree table for {nplots} plots from the file: {file}" \
        .format(nplots=counter.__len__(), file=os.path.basename(infile))
    print(info_msg)
    logging.info(info_msg)
