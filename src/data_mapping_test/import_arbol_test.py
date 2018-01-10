#!/usr/bin/env python
# -*- coding: utf-8 -*-s
import csv
import logging
import os

from src.model import code_lists
from src.utils import tools_lib


def import_fni_trees_test(survey, species_list, infile):
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

                #if row['tipoDeBosq'] in ['Bosque Nativo']:
                try:
                    arbol_id = "%d"%float(row['numArbol'])
                    print(arbol_id)
                except ValueError:
                    error_msg = " Cannot create a tree id from \"{numArbol}\" for plot {plotid}"\
                            .format(numArbol=row['numArbol'],plotid=ID)
                    logging.error(error_msg)

                # We add only a tree if it is not in the tree list otherwise we assume that this is a stem of the same tree
                if arbol_id not in survey.plots[ID].trees.keys():
                    print("not in")
                    survey.plots[ID].add_tree(arbol_id)

                # We get stem id from row
                stem_id = row['No vara']


                # Add stems to the tree
                dap1 = tools_lib.import_variable(row, 'dap1', 'float', ID)

                dap2 = tools_lib.import_variable(row, 'dap2', 'float', ID)

                ht = tools_lib.import_variable(row, 'ht', 'float', ID, treeid=arbol_id)
                survey.plots[ID].trees[arbol_id].add_stem(stem_id=stem_id, dap1=dap1, dap2=dap2, ht=ht)

                print 'Stem count:{:}'.format(survey.plots[ID].trees[arbol_id].stem_count())
                
                survey.plots[ID].trees[arbol_id].arbol_id = arbol_id
                
                #Import the attributes for natural forest
                #if row['tipoDeBosq']== "Bosque Nativo":
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

                #Import the attribute for plantaciones

                survey.plots[ID].trees[arbol_id].stems[stem_id].dap1_unit_name = 'centimetros'
                survey.plots[ID].trees[arbol_id].stems[stem_id].dap2_unit_name = 'centimetros'
                survey.plots[ID].trees[arbol_id].stems[stem_id].dap_unit_name = 'centimetros'
                survey.plots[ID].trees[arbol_id].stems[stem_id].ht_unit_name = 'metros'
                survey.plots[ID].trees[arbol_id].arbol_parcela = 5

    info_msg = "Updated the tree table for {nplots} plots from the file: {file}" \
        .format(nplots=counter.__len__(), file=os.path.basename(infile))
    print(info_msg)
    logging.info(info_msg)
