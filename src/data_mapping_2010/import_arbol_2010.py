#!/usr/bin/env python
# -*- coding: utf-8 -*-s
"""This module provides the functionality to import_modules the single tree information in to 2010 data format. The single tree
variables will become visible in the tab "Datos Dasométrics" in OF Collect. It can be used as a general python module
in a python program are called as a python script from the console.
"""

__docformat__ = 'reStructuredText'
import csv
import logging
import os

from src.model import code_lists
from src.utils import tools_lib


def import_fni_trees_2010(survey, species_list, infile):
    """ Function to import_modules tree data from natural forest and plantations the 2010 file format

    :param survey:  A survey object into which the plot information will be added
    :param species_list:  A list with tree species names as exported from the Collect species list
    :param infile:  he file path to the 2010 single tree data
    :type survey: An instance of :class:`~model.class_lib.Survey`
    :type species_list: A dictionary with instances of :class:`~model.class_lib.Species`
    :type infile: A file path
    :return: If executed as script a file with the single tree information that can be imported in to OF Collect.
     Otherwise an updated survey object
    :rtype: :class:`~model.class_lib.Survey` / CSV File

    - **Example**  how to use as script::

        :Example usage:
        python import_arbol_2010.py Nativo_2010.csv arbol_especie.csv arboles_nativo_2010.csv
    """

    with open(infile, 'rb') as planilla_bn:
        datareader = csv.DictReader(planilla_bn, delimiter=',')
        plot_counter = []
        for row in datareader:
            id = row['p_muestreo_pl']
            if id in survey.plots.keys():
                print 'Processing PlotID:{:}'.format(id)
                if id not in plot_counter:
                    plot_counter.append(id)
                #TODO Check client favor solution for missing tree ids is
                no_tree_id=False
                if row['arbol'] in['' , ' ']:
                    # Set a artifical id
                    arbol_id = survey.plots[id].trees.__len__() + 1
                    no_tree_id = True
                    warn_msg = "No Tree id found for plot: {plotid} creating a new Tree id: {arbol_id}"\
                        .format(plotid=id,arbol_id=arbol_id)
                    logging.warn(warn_msg)

                else:
                    arbol_id = tools_lib.import_variable(row, 'arbol', 'int', id)
                    stem_id = tools_lib.import_variable(row, 'No vara', 'int', id)

                dap1 = tools_lib.import_variable(row, 'd1', 'int', id)
                dap2 = tools_lib.import_variable(row, 'd2', 'int', id)
                ht = tools_lib.import_variable(row, 'ht', 'int', id)

                if row.has_key('diametro'):
                    parcela = tools_lib.convert_arbol_diametro(row['diametro'])
                else:
                    parcela = 5
                arbol_unico_id = str(parcela) + '_' + str(arbol_id) + '_' + str(stem_id)

                # We add only a tree if it is not in the tree list
                if arbol_unico_id not in survey.plots[id].trees.keys():
                    survey.plots[id].add_tree(arbol_unico_id)

                survey.plots[id].trees[arbol_unico_id].arbol_id = arbol_id
                survey.plots[id].trees[arbol_unico_id].parcela = parcela
                # For bosque nativo the species is observed on the single tree level and recorded in the tree table
                if row.has_key('genero') and row.has_key('Especie'):
                    species_name = row['genero'] + ' ' + row['Especie']
                    index = tools_lib.find_species_scientific(species_list, species_name)
                    if index.__len__() > 0:
                        survey.plots[id].trees[arbol_unico_id].arbol_especie_code = \
                            species_list[index[0]].species_code
                        survey.plots[id].trees[arbol_unico_id].arbol_especie_scientific_name = \
                            species_list[index[0]].scientific_name
                        survey.plots[id].trees[arbol_unico_id].arbol_especie_vernacular_name = \
                            species_list[index[0]].common_name
                    else:
                        error_msg = "Cannot find the tree species \"{species}\" in the species list for tree {treeid} "\
                                   "on plot {plotid}". \
                            format(species=species_name, treeid=arbol_id, plotid=id)
                        logging.error(error_msg)

                # For plantations the species is a plot variable and similar for all trees
                else:
                    species_code = survey.plots[id].plantacion_plant_especie_code
                    if species_code is not None:
                        index = tools_lib.find_species_code(species_list, species_code)
                        if index.__len__() > 0:
                            survey.plots[id].trees[arbol_unico_id].arbol_especie_code = \
                                species_list[index].species_code
                            survey.plots[id].trees[arbol_unico_id].arbol_especie_scientific_name = \
                                species_list[index].scientific_name
                            survey.plots[id].trees[arbol_unico_id].arbol_especie_vernacular_name = \
                                species_list[index].common_name
                    else:
                        warn_msg = "Species code not set for tree {treeid} on plot {plotid}"\
                                .format(treeid=arbol_id, plotid=id)
                        logging.warn(warn_msg)

                #Adding the stem to the tree
                survey.plots[id].trees[arbol_unico_id].add_stem(stem_id=stem_id,dap1=dap1, dap2=dap2, ht=ht)

                #Adding the comments field
                if row.has_key('d_obser'):
                    ostr = 'd_obser'
                if row.has_key('d_observ'):
                    ostr = 'd_observ'
                if row[ostr] in ['', ' ']:
                    survey.plots[id].trees[arbol_unico_id].stems[stem_id].observacion = '-'
                else:
                    survey.plots[id].trees[arbol_unico_id].stems[stem_id].observacion = \
                        tools_lib.import_variable(row, ostr, 'string', id)
                if no_tree_id is True:
                    #Adding a comment if the tree id was generated by the script
                    survey.plots[id].trees[arbol_unico_id].stems[stem_id].observacion = \
                        survey.plots[id].trees[arbol_unico_id].stems[stem_id].observacion + 'No tree id found in the data'

                survey.plots[id].trees[arbol_unico_id].stems[stem_id].dap1_unit_name = 'centimetros'
                survey.plots[id].trees[arbol_unico_id].stems[stem_id].dap2_unit_name = 'centimetros'
                survey.plots[id].trees[arbol_unico_id].stems[stem_id].dap_unit_name = 'centimetros'
                survey.plots[id].trees[arbol_unico_id].stems[stem_id].ht_unit_name = 'metros'
                survey.plots[id].trees[arbol_unico_id].stems[stem_id].hp_unit_name = 'metros'
                survey.plots[id].trees[arbol_unico_id].stems[stem_id].corteza_espesor_unit_name = ''
                survey.plots[id].trees[arbol_unico_id].stems[stem_id].rumbo_unit_name = None
                survey.plots[id].trees[arbol_unico_id].stems[stem_id].distancia_unit_name = 'metros'
                survey.plots[id].trees[arbol_unico_id].stems[stem_id].hc_unit_name = 'metros'

                # Single tree attribute only relevant for nature forest
                if row.has_key('diametro'):
                    bosque_nativo = False
                else:
                    bosque_nativo = True

                if bosque_nativo:
                    # TODO Estrato needs to be updated once the information how the mapping should be done is available
                    survey.plots[id].trees[arbol_unico_id].stems[stem_id].estrado = tools_lib.\
                                import_variable(row,'estrato_v','code', id, codelist=code_lists.arbol_estrato)
                    # TODO Needs to be updated once the information is available
                    #survey.plots[id].trees[arbol_unico_id].stems[stem_id].rango_edad = \
                    #    tools_lib.import_variable(row,'rango_edad','int',id)
                    survey.plots[id].trees[arbol_unico_id].stems[stem_id].rango_edad = '-'
                else:
                    #for plantations only
                    survey.plots[id].trees[arbol_unico_id].stems[stem_id].distancia = \
                        tools_lib.import_variable(row, 'dist', 'float', id)
                    survey.plots[id].trees[arbol_unico_id].stems[stem_id].rumbo = \
                        tools_lib.import_variable(row, 'rumbo', 'int', id)
                    survey.plots[id].trees[arbol_unico_id].stems[stem_id].hc = \
                        tools_lib.import_variable(row, 'hc', 'float', id)
                    survey.plots[id].trees[arbol_unico_id].stems[stem_id].hp = \
                        tools_lib.import_variable(row, 'h_poda', 'float', id)

                    if row.has_key('forma') and  row['forma'] not in ['',' ']:
                        forma_str =str.replace(row['forma'],',','.')
                        #TODO Only one form variable can be stored in OF. We are using the first only!
                        forma = str.split(forma_str,'.')[0]
                        if forma in ['1','2','3','4','5','6']:
                                survey.plots[id].trees[arbol_unico_id].stems[stem_id].forma= forma
                        else:
                            warn_msg = 'Cannot convert the forma variable "{forma}" to a class between 1:5 for tree"' \
                                       '{treeid} on plot {plotid}'.format(forma=row['forma'],treeid=arbol_id,plotid=id)
                            logging.warning(warn_msg)

                    survey.plots[id].trees[arbol_unico_id].stems[stem_id].corteza_espesor = tools_lib.import_variable(row, 'espesor', 'float', id)

    info_msg = "Updated the tree table for {nplots} plots from the file: {file}"\
                    .format(nplots=plot_counter.__len__(),file=os.path.basename(infile))
    logging.info(info_msg)
    print(info_msg)