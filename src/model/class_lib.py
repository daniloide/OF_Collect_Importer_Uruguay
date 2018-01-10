#!/usr/bin/env python
# -*- coding: utf-8 -*-s
"""
Module that contains the base classes
"""

import csv
import os


class Species:
    """
    A class to store the information of Taxa
    """

    def __init__(self, species_id, species_code, scientific_name):
        self.species_id = species_id
        self.species_code = species_code
        self.scientific_name = scientific_name
        self.common_name = None
        self.alternatives = [scientific_name]
        self.tipo =None
        self.cant = None

    def __str__(self):
        return 'Species: {species_id} with scientific name {scientific_name}' \
            .format(species_id=self.species_id, scientific_name=self.scientific_name)


class Survey:
    """
    The base container class which holds all information of a survey including the plot, tree and fauna information.
    The class also provides the exports functions to create the csv files in the required format.
    """

    def __init__(self, survey_id):
        self.survey_id = survey_id
        self.plot_list = []
        self.plots = {}

    def __str__(self):
        return 'Survey ID: {survey_id} with {plots} plots' \
            .format(survey_id=self.survey_id, plots=self.plots.__len__())

    def plot_count(self):
        """
        Function to count the number of plots stored in the survey

        :return: integer with the number of plots in the survey
        """

        return self.plots.__len__()

    def update_arbol_position(self):
        """
        Function to update the position column of the tree table

        :return: Integer with the number of stems
        """

        for p in self.plots:
            stem_count = 1
            for t in self.plots[p].trees:
                # stem_count += self.trees[t].stems.__len__()
                for s in self.plots[p].trees[t].stems:
                    self.plots[p].trees[t].stems[s].arbol_position = stem_count
                    stem_count += 1
        return stem_count

    def add_plot(self, plot_id, censo_id):
        """
        Function to add a new plot to the survey

        :param plot_id: The unique plot ID
        :param censo_id: The censo ID
        :return: A message string
        """
        self.plots[plot_id] = Plot(name=plot_id, plot_id=plot_id)
        self.plots[plot_id].pm_cenos = censo_id
        self.plot_list.append(plot_id)
        return "Adding plot: {}".format(plot_id)

    def export_arbol_file(self, outfile):
        """
        Function to create the csv file with the single tree information from the survey

        :param outfile: File path to the output file
        :return:
        """
        self.update_arbol_position()
        outfile = open(outfile, 'wb')
        # Define Header
        header = ["parcela_parcela_id", "parcela_pm_censo", "_arbol_position", "arbol_parcela", "arbol_id",
                  "arbol_fuste_id",  "arbol_especie_code", "arbol_especie_scientific_name",
                  "arbol_especie_vernacular_name",
                  "arbol_dap1", "arbol_dap1_unit_name", "arbol_dap2", "arbol_dap2_unit_name", "arbol_ht", "arbol_ht_unit_name", "arbol_estrato"]

        writer = csv.writer(outfile, dialect='excel')
        writer.writerow(header)
        for p in self.plots:
            tmp = self.plots[p].export_trees()
            for s in tmp:
                outfile.write(s + '\n')
        outfile.close()

    def export_parcela_file(self, outfile):
        """
        Function to create the csv file with the  plot information from the survey

        :param: outfile: File path to the output file
        """
        outfile = open(outfile, 'wb')
        # Define header of export file
        header = ["parcela_id", "pm_censo", 
                  "pm_departamento", "pm_subcuenca", 
                  "general_datos_parcela_bosque_tipo",
                  "general_datos_parcela_subbosque_tipo", "general_datos_parcela_fecha_relev_year",
                  "general_datos_parcela_fecha_relev_month", "general_datos_parcela_fecha_relev_day",
                  "parcela_coordenadas_parcela_gps_coord_srs",
                  "parcela_coordenadas_parcela_gps_coord_x", "parcela_coordenadas_parcela_gps_coord_y"
              ]

        writer = csv.writer(outfile, dialect='excel')
        writer.writerow(header)
        for p in self.plots:
            outfile.write(self.plots[p].export_parcela() + '\n')
        outfile.close()

class Plot:
    """
    Base class for all plot level information
    """

    def __init__(self, name, plot_id):
        self.name = name
        self.parcela_id = plot_id
        self.pm_censo = 1
        self.pm_departamento = None
        self.pm_subcuenca = None
        self.general_datos_parcela_bosque_tipo = None
        self.general_datos_parcela_bosque_sub_tipo = None
        self.general_datos_parcela_fecha_observation_year = None
        self.general_datos_parcela_fecha_observation_month = None
        self.general_datos_parcela_fecha_observation_day = None
        self.parcela_coordenadas_gps_coord_srs = None
        self.parcela_coordenadas_gps_coord_x = None
        self.parcela_coordenadas_gps_coord_y = None
        self.trees = {}
 
    def add_tree(self, arbol_unico_id):
        """
        Function to add a new tree to the plot

        :param arbol_unico id: tree id
        """
        if arbol_unico_id not in self.trees.keys():
            self.trees[arbol_unico_id] = Tree(arbol_unico_id=arbol_unico_id)
            print "Adding tree: {}".format(arbol_unico_id)
        else:
            raise ValueError("Tree with TreeID {treeid} already exits in plot {plotid}".format(treeid=arbol_unico_id,
                                                                                               plotid=self.parcela_id))
    def __str__(self):
        return ' I am a plot'

    def export_parcela(self):
        """
        Function to create the csv file with the plot level information

        :param outfile: File path to the output file
        :return:
        """
        out = '{parcela_id},' \
              '{parcela_censo},' \
              '{pm_departamento},' \
              '{parcela_subcuenca},' \
              '{parcela_general_bosque_tipo},' \
              '{parcela_general_bosque_sub_tipo},' \
              '{parcela_fecha_relev_year},' \
              '{parcela_fecha_relev_month},' \
              '{parcela_fecha_relev_day},' \
              '{parcela_coordinados_gps_coord_SRS},' \
              '{parcela_coordinados_gps_coord_x},' \
              '{parcela_coordinados_gps_coord_y},' \
            .format(parcela_id=self.parcela_id,
                    parcela_censo=self.pm_censo,
                    pm_departamento=self.pm_departamento,
                    parcela_subcuenca=self.pm_subcuenca,
                    parcela_general_bosque_tipo=self.general_datos_parcela_bosque_tipo,
                    parcela_general_bosque_sub_tipo=self.general_datos_parcela_bosque_sub_tipo,
                    parcela_fecha_relev_year=self.general_datos_parcela_fecha_observation_year,
                    parcela_fecha_relev_month=self.general_datos_parcela_fecha_observation_month,
                    parcela_fecha_relev_day=self.general_datos_parcela_fecha_observation_day,
                    parcela_coordinados_gps_coord_SRS=self.parcela_coordenadas_gps_coord_srs,
                    parcela_coordinados_gps_coord_x=self.parcela_coordenadas_gps_coord_x,
                    parcela_coordinados_gps_coord_y=self.parcela_coordenadas_gps_coord_y
                    )
        out = str.replace(out, 'None', '')
        return out

    def export_trees(self):
        """
        Function to create the strings required for the tree list file from the plot class
        :return: List with a string for each stem in the plot
        """
        out = []
        for key in self.trees:
            for j in self.trees[key].stems:
                string = '"{parcela_parcela_id}",' \
                         '"{parcela_pm_censo}",' \
                         '"{_arbol_position}",' \
                         '"{arbol_parcela}",' \
                         '"{arbol_id}",' \
                         '"{arbol_fuste_id}",' \
                         '"{arbol_especie_code}",' \
                         '"{arbol_especie_scientific_name}",' \
                         '"{arbol_especie_vernacular_name}",' \
                         '"{arbol_dap1}",' \
                         '"{arbol_dap1_unit_name}",' \
                         '"{arbol_dap2}",' \
                         '"{arbol_dap2_unit_name}",' \
                         '"{arbol_ht}",' \
                         '"{arbol_ht_unit_name}",' \
                         '"{arbol_estrato}",' \
                    .format(parcela_parcela_id=self.parcela_id,
                            parcela_pm_censo=self.pm_censo,
                            _arbol_position=self.trees[key].stems[j].arbol_position,
                            arbol_parcela=self.trees[key].arbol_parcela,
                            arbol_id=self.trees[key].arbol_id,
                            arbol_fuste_id=self.trees[key].stems[j].stem_id,
                            arbol_especie_code=self.trees[key].arbol_especie_code,
                            arbol_especie_scientific_name=self.trees[key].arbol_especie_scientific_name,
                            arbol_especie_vernacular_name=self.trees[key].arbol_especie_vernacular_name,
                            arbol_dap1=self.trees[key].stems[j].dap1,
                            arbol_dap1_unit_name=self.trees[key].stems[j].dap1_unit_name,
                            arbol_dap2=self.trees[key].stems[j].dap2,
                            arbol_dap2_unit_name=self.trees[key].stems[j].dap2_unit_name,
                            arbol_ht=self.trees[key].stems[j].ht,
                            arbol_ht_unit_name=self.trees[key].stems[j].ht_unit_name,
                            arbol_estrato=self.trees[key].stems[j].estrado)
                # print string
                out.append(string)
        result = []
        for i in out:
            result.append(i) #str.replace(i, 'None', ''))
        return result

    def tree_count(self):
        """
        Function to calculate the number of trees in plot
        :return: Integer number of trees on plot
        """
        # print 'Number of trees in plot {tree_count}'.format(tree_count=self.trees.__len__())
        return self.trees.__len__()

class Tree:
    """
    Basic class for all tree level information
    """

    def __init__(self, arbol_unico_id):
        # self.parcela_position = None
        self.parcela = None
        self.arbol_id = None
        # self.stem_id = 0
        self.arbol_unico_id = arbol_unico_id
        self.arbol_especie_code = None
        self.arbol_especie_scientific_name = None
        self.arbol_especie_vernacular_name = None
        self.arbol_especie_language_code = None
        self.arbol_especie_language_variety = None
        self.stems = {}

    def add_stem(self,stem_id, dap1, dap2, ht):
        """Function to add a new stem to a tree

        :param dap1: First diameter measurment
        :param dap2: Second diameter measurment
        :param ht:  Tree Height
        :return: A message string
        """
        stem_id = stem_id
        #stem_id = self.stems.__len__() + 1
        self.stems[stem_id] = Stem(stem_id, dap1, dap2, ht)
        # self.stems[stem_id].arbol_position=self.stems[stem_id].arbol_position+1
        self.stems[stem_id].arbol_position = self.stems.__len__()
        print "Adding stem {} to tree {}".format(stem_id, self.arbol_id)

    def stem_count(self):
        """
        Function to extract the number of stems of the tree
        :return: Integer value with the number of trees
        """
        # print 'Number of stems in for tree {stem_count}'.format(stem_count=self.stems.__len__())
        return self.stems.__len__()

    def __str__(self):
        return 'Tree: {tree_id} with {stem_cnt} stems'.format(tree_id=self.arbol_id, stem_cnt=len(self.stems))
        # return {self.dbh}

class Stem:
    """
    Basic class for all single stem related information
    """
    def __init__(self, stem_id, dap1, dap2, ht):
        self.stem_id = stem_id
        self.arbol_position = 0
        self.dap1 = dap1
        self.dap1_unit_name = None
        self.dap2 = dap2
        self.dap2_unit_name = None
        self.dap = None
        self.dap_unit_name = None
        self.ht = ht
        self.ht_unit_name = None
        self.estrado = None
   
    def __str__(self):
        return "I am a stem"
