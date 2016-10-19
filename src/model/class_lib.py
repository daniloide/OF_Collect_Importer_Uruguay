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


    def update_fauna_position(self):
        """
        Function to update the position column of the fauna aves table

        :return: Message string
        """

        for p in self.plots:
            fauna_aves_count = 1
            for f in self.plots[p].fauna_aves:
                self.plots[p].fauna_aves[f].position = fauna_aves_count
                fauna_aves_count += 1

            fauna_mamifero_count = 1
            for f in self.plots[p].fauna_mamiferos:
                self.plots[p].fauna_mamiferos[f].position = fauna_mamifero_count
                fauna_mamifero_count += 1

            fauna_reptil_count = 1
            for f in self.plots[p].fauna_reptiles:
                self.plots[p].fauna_reptiles[f].position = fauna_reptil_count
                fauna_reptil_count += 1

            fauna_anfibios_count = 1
            for f in self.plots[p].fauna_anfibios:
                self.plots[p].fauna_anfibios[f].position = fauna_anfibios_count
                fauna_anfibios_count += 1

        return "Fauna position colums are updated"

    def update_flora_suelo_position(self):
        """
        Function to update the position column of the flora_suelo table

        :return: integer with the number of fauna entries in the plot
        """

        for p in self.plots:
            count = 1
            for f in self.plots[p].flora_suelo:
                self.plots[p].flora_suelo[f].position = count
                count += 1
        return "Flora suelo position colums are updated"

    def update_flora_soto_position(self):
        """
        Function to update the position column of the flora_soto table

        :return: integer with the number of fauna entries in the plot
        """

        for p in self.plots:
            count = 1
            for f in self.plots[p].flora_soto:
                self.plots[p].flora_soto[f].position = count
                count += 1
        return "Flora soto position colums are updated"

    def update_foto_position(self):
        """
        Function to update the position column of the foto table
        :return:  A message string
        """

        for p in self.plots:
            count = 1
            for f in self.plots[p].fotos:
                self.plots[p].fotos[f].foto_position = count
                count += 1
        return "Foto position colums are updated"


    def update_distance_position(self):
        """
        Function to update the position column of the distance table

        :return: A message string
        """

        for p in self.plots:
            count = 1
            for f in self.plots[p].distances:
                self.plots[p].distances[f].distancia_position = count
                count += 1
        return "Distance position colums are updated"

    def update_invasora_position(self):
        """
        Function to update the position column of the invasoras table

        :return: A message string
        """

        for p in self.plots:
            count = 1
            for f in self.plots[p].invasoras:
                self.plots[p].invasoras[f].invasora_position = count
                count += 1
        return "Invasoras position colums are updated"

    def update_regeneracion_position(self):
        """
        Function to update the position column of the regeneration table

        :return: A message string
        """

        for p in self.plots:
            count = 1
            for f in self.plots[p].regeneracion:
                self.plots[p].regeneracion[f].regen_position = count
                count += 1
        return "Regeneration position colums are updated"

    def update_equipo_position(self):
        """
        Function to update the position column of the equipo table

        :return: A message string
        """

        for p in self.plots:
            count = 1
            for f in self.plots[p].equipo:
                self.plots[p].equipo[f].equipo_position = count
                count += 1
        return "Equipo position colums are updated"

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
                  "arbol_fuste_id", "arbol_unico_id", "arbol_especie_code", "arbol_especie_scientific_name",
                  "arbol_especie_vernacular_name", "arbol_especie_language_code", "arbol_especie_language_variety",
                  "arbol_dap1", "arbol_dap1_unit_name", "arbol_dap2", "arbol_dap2_unit_name", "arbol_dap",
                  "arbol_dap_unit_name","arbol_corteza_espesor", "arbol_corteza_espesor_unit_name", "arbol_distancia",
                  "arbol_distancia_unit_name","arbol_rumbo", "arbol_rumbo_unit", "arbol_ht", "arbol_ht_unit_name",
                  "arbol_hc", "arbol_hc_unit_name", "arbol_hp", "arbol_hp_unit_name", "arbol_estrato",
                  "arbol_rango_edad", "arbol_forma","arbol_observacion"]

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
        header = ["parcela_id", "pm_censo", "pm_coord_srs", "pm_coord_x", "pm_coord_y", "pm_altitude",
                  "pm_altitude_unit_name",
                  "pm_departamento", "pm_cuenca", "pm_subcuenca", "pm_censal", "general_datos_parcela_estado_nivel1",
                  "general_datos_parcela_estado_nivel2","general_datos_parcela_estado_nivel3", "general_datos_parcela_com",
                  "general_datos_parcela_bosque_tipo",
                  "general_datos_parcela_subbosque_tipo", "general_datos_parcela_fecha_relev_year",
                  "general_datos_parcela_fecha_relev_month", "general_datos_parcela_fecha_relev_day",
                  "general_datos_parcela_accesibilidad", "general_datos_parcela_propietario",
                  "general_datos_parcela_predio", "parcela_coordenadas_parcela_gps_coord_srs",
                  "parcela_coordenadas_parcela_gps_coord_x", "parcela_coordenadas_parcela_gps_coord_y",
                  "parcela_coordenadas_parcela_gps_altitud", "parcela_coordenadas_parcela_gps_altitud_unit_name",
                  "track_archivo", "track_fichero", "relieve_relieve_ubicacion", "relieve_relieve_exposicion",
                  "relieve_relieve_pendiente", "relieve_relieve_pendiente_forma", "suelo_suelo_coneat",
                  "suelo_suelo_uso_tierra",
                  "suelo_suelo_uso_previo", "suelo_suelo_labranza", "suelo_suelo_erosion_grado",
                  "suelo_suelo_erosion_tipo",
                  "suelo_suelo_profundidad_horizonte", "suelo_suelo_profundidad_mantillo",
                  "suelo_suelo_profundidad_humus",
                  "suelo_suelo_color", "suelo_suelo_textura", "suelo_suelo_estructura", "suelo_suelo_drenaje",
                  "suelo_suelo_infiltracion", "suelo_suelo_impedimento", "suelo_suelo_olor", "suelo_suelo_humedad",
                  "suelo_suelo_pedregosidad", "suelo_suelo_pedregosidad_unit_name", "suelo_suelo_rocosidad",
                  "suelo_suelo_rocosidad_unit_name", "suelo_suelo_micorrizas", "suelo_suelo_fauna",
                  "suelo_suelo_raices",
                  "cobertura_vegetal_cobertura_copas", "cobertura_vegetal_cobertura_sotobosque",
                  "cobertura_vegetal_cobertura_herbacea", "cobertura_vegetal_cobertura_residuos_plantas",
                  "cobertura_vegetal_cobertura_residuos_cultivos", "flora_soto_flora_soto_presencia",
                  "agua_agua_presencia",
                  "agua_agua_caudal", "agua_agua_distancia", "agua_agua_distancia_unit_name", "agua_agua_nombre",
                  "agua_agua_manejo",
                  "agua_agua_frec", "agua_agua_acuicultura", "agua_agua_contaminacion",
                  "ambiental_ambiental_potabilidad",
                  "ambiental_ambiental_polucion", "ambiental_ambiental_fertalidad", "ambiental_ambiental_invasion",
                  "ambiental_ambiental_pesticida", "fuego_fuego_evidencia", "fuego_fuego_tipo", "fuego_fuego_proposito",
                  "plantacion_plant_especie_code", "plantacion_plant_especie_scientific_name",
                  "plantacion_plant_especie_vernacular_name", "plantacion_plant_especie_language_code",
                  "plantacion_plant_especie_language_variety", "plantacion_plant_edad", "plantacion_plant_raleo",
                  "plantacion_plant_poda", "plantacion_plant_poda_altura", "plantacion_plant_poda_altura_unit_name",
                  "plantacion_plant_regular", "plantacion_plant_dist_fila", "plantacion_plant_dist_fila_unit_name",
                  "plantacion_plant_dist_entrefila", "plantacion_plant_dist_entrefila_unit_name",
                  "plantacion_plant_fila_cantidad",
                  "plantacion_plant_dist_silvopast", "plantacion_plant_dist_silvopast_unit_name",
                  "plantacion_plant_adaptacion",
                  "plantacion_plant_regimen", "plantacion_plant_estado", "forestacion_forest_origen",
                  "forestacion_forest_estructura", "forestacion_forest_propiedad", "forestacion_forest_plan_manejo",
                  "forestacion_forest_intervencion", "forestacion_forest_madera_destino[1]",
                  "forestacion_forest_madera_destino[2]","forestacion_forest_madera_destino[3]",
                  "forestacion_forest_madera_destino[4]","forestacion_forest_madera_destino[5]",
                  "forestacion_forest_madera_destino[6]","forestacion_forest_silvicultura",
                  "forestacion_forest_tecnologia", "ntfp_ntfp_ganado_tipo[1]", "ntfp_ntfp_ganado_tipo[2]",
                  "ntfp_ntfp_ganado_tipo[3]", "ntfp_ntfp_ganado_tipo[4]", "ntfp_ntfp_ganado_tipo[5]",
                  "ntfp_ntfp_pastoreo_intens", "ntfp_ntfp_prod_cultivo", "ntfp_ntfp_prod_apicola", "ntfp_ntfp_semillas",
                  "ntfp_ntfp_sombra", "ntfp_ntfp_caza_pesca", "ntfp_ntfp_rompe_vientos", "ntfp_ntfp_recreacion",
                  "ntfp_ntfp_hongos", "ntfp_ntfp_cientificos", "ntfp_ntfp_aceites", "ntfp_ntfp_carbono", "pm_padron",
                  "san_rumbo", "san_rumbo_unit_name"]

        writer = csv.writer(outfile, dialect='excel')
        writer.writerow(header)
        for p in self.plots:
            outfile.write(self.plots[p].export_parcela() + '\n')
        outfile.close()

    def export_distance_file(self, outfile):
        """Function to export the csv file with the distance information from the survey

        :param outfile: File path to the output file
        :return:
        """
        self.update_distance_position()
        outfile = open(outfile, 'wb')

        header = ["parcela_parcela_id", "parcela_pm_censo", "_distancia_position", "distancia_categoria",
                  "distancia_kilometros",
                  "distancia_kilometros_unit_name", "rumbo_punto_gps_centro", "rumbo_punto_gps_centro_unit_name",
                  "distancia_camino_estado"]

        writer = csv.writer(outfile, dialect='excel')
        writer.writerow(header)
        for p in self.plots:
            tmp = self.plots[p].export_distances()
            for s in tmp:
                outfile.write(s + '\n')
        outfile.close()


    def export_fauna_files(self, outdir, prefix=None):
        """
        Functions to create the csv files for: birds, mammals, reptiles and amphibians.

        :param outdir: The directory where the output files will be saved
        :param prefix: A name prefix that should be used for the output file names
        :return:
        """
        self.update_fauna_position()

        if prefix:
            aves_csv = os.path.join(outdir,(prefix + '_fauna_aves.csv'))
            mamifero_csv = os.path.join(outdir,(prefix + '_fauna_mamiferos.csv'))
            reptil_csv = os.path.join(outdir, (prefix + '_fauna_reptiles.csv'))
            anfibio_csv = os.path.join(outdir, (prefix + '_fauna_anfibios.csv'))
        else:
            aves_csv = os.path.join(outdir,'fauna_aves.csv')
            mamifero_csv = os.path.join(outdir, 'fauna_mamiferos.csv')
            reptil_csv = os.path.join(outdir, 'fauna_reptiles.csv')
            anfibio_csv = os.path.join(outdir, 'fauna_anfibios.csv')
        
        header = ["parcela_parcela_id","parcela_pm_censo","_fauna_XX_position","fauna_XX_especie_code",
                  "fauna_XX_especie_scientific_name","fauna_XX_especie_vernacular_name",
                  "fauna_XX_especie_language_code","fauna_XX_especie_language_variety",
                  "fauna_XX_tipo","fauna_XX_cant"]

        #Export Aves file
        outfile = open(aves_csv, 'wb')
        aves_header=[]
        for s in header:
            tmp = str.replace(s,'XX','aves')
            aves_header.append(tmp)

        writer = csv.writer(outfile, dialect='excel')
        writer.writerow(aves_header)
        for p in self.plots:
             tmp = self.plots[p].export_fauna_aves()
             for s in tmp:
                outfile.write(s + '\n')
        outfile.close()

        # Export Mamifero file
        outfile = open(mamifero_csv, 'wb')
        mamifero_header = []
        for s in header:
            tmp = str.replace(s, 'XX', 'mamiferos')
            mamifero_header.append(tmp)

        writer = csv.writer(outfile, dialect='excel')
        writer.writerow(mamifero_header)
        for p in self.plots:
            tmp = self.plots[p].export_fauna_mamiferos()
            for s in tmp:
                outfile.write(s + '\n')
        outfile.close()

        # Export Reptil file
        outfile = open(reptil_csv, 'wb')
        reptil_header = []
        for s in header:
            tmp = str.replace(s, 'XX', 'reptiles')
            reptil_header.append(tmp)

        writer = csv.writer(outfile, dialect='excel')
        writer.writerow(reptil_header)
        for p in self.plots:
            tmp = self.plots[p].export_fauna_reptiles()
            for s in tmp:
                outfile.write(s + '\n')
        outfile.close()

        # Export Anfibio file
        outfile = open(anfibio_csv, 'wb')
        anfibio_header = []
        for s in header:
            tmp = str.replace(s, 'XX', 'anfibios')
            anfibio_header.append(tmp)

        writer = csv.writer(outfile, dialect='excel')
        writer.writerow(anfibio_header)
        for p in self.plots:
            tmp = self.plots[p].export_fauna_anfibios()
            for s in tmp:
                outfile.write(s + '\n')
        outfile.close()

    def export_flora_suelo(self, outfile):
        """Function to create the csv file with the soil flora information

        :param outfile: File path to the output file
        :return:
        """
        self.update_flora_suelo_position()
        outfile = open(outfile, 'wb')

        header = ["parcela_parcela_id","parcela_pm_censo","_flora_suelo_position","flora_suelo_especie_code",
                      "flora_suelo_especie_scientific_name","flora_suelo_especie_vernacular_name",
                      "flora_suelo_especie_language_code","flora_suelo_especie_language_variety","flora_suelo_frec"]

        writer = csv.writer(outfile, dialect='excel')
        writer.writerow(header)
        for p in self.plots:
            tmp = self.plots[p].export_flora_suelo()
            for s in tmp:
                outfile.write(s + '\n')
        outfile.close()

    def export_flora_soto(self, outfile):
        """
        Function to create the csv file with the forest flora information

        :param outfile: File path to the output file
        :return:
        """
        self.update_flora_soto_position()
        outfile = open(outfile, 'wb')

        header = ["parcela_parcela_id","parcela_pm_censo","_flora_soto_caracter_position","flora_soto_tipo",
                      "flora_soto_altura","flora_soto_altura_unit_name"]

        writer = csv.writer(outfile, dialect='excel')
        writer.writerow(header)
        for p in self.plots:
            tmp = self.plots[p].export_flora_soto()
            for s in tmp:
                outfile.write(s + '\n')
        outfile.close()

    def export_fotos(self, outfile):
        """
        Function to create the csv file with the foto information

        :param outfile: File path to the output file
        :return:
        """
        self.update_foto_position()
        outfile = open(outfile, 'wb')

        header = ["parcela_parcela_id","parcela_pm_censo","_foto_position","foto_tipo","foto_coord_srs",
                      "foto_coord_x","foto_coord_y","foto_descr","foto_archivo","foto_fichero"]

        writer = csv.writer(outfile, dialect='excel')
        writer.writerow(header)
        for p in self.plots:
            tmp = self.plots[p].export_fotos()
            for s in tmp:
                #Check if lenght correspont to header
                if str.split(s,',').__len__() == header.__len__():
                    outfile.write(s + '\n')
                else:
                    print "File header length is not equal the number of variables in the foto export"
        outfile.close()

    def export_invasoras(self, outfile):
        """
        Function to create the csv file with the information on invasive species

        :param outfile: File path to the output file
        :return:
        """
        self.update_invasora_position()
        outfile = open(outfile, 'wb')

        header = ["parcela_parcela_id","parcela_pm_censo","_invasora_position","invasora_categoria",
                  "invasora_especie_code","invasora_especie_scientific_name","invasora_especie_vernacular_name",
                  "invasora_especie_language_code","invasora_especie_language_variety","invasora_severidad"]

        writer = csv.writer(outfile, dialect='excel')
        writer.writerow(header)
        for p in self.plots:
            tmp = self.plots[p].export_invasoras()
            for s in tmp:
                #Check if lenght correspont to header
                if str.split(s,',').__len__() == header.__len__():
                    outfile.write(s + '\n')
                else:
                    print "File header length is not equal the number of variables in the  invasoras export"
        outfile.close()

    def export_regeneracion(self, outfile):
        """
        Function to create the csv file with the information on regeneration

        :param outfile: File path to the output file
        :return:
        """
        self.update_regeneracion_position()
        outfile = open(outfile, 'wb')

        header = ["parcela_parcela_id","parcela_pm_censo","_regen_position","regen_subparcela_id","regen_distancia",
                  "regen_distancia_unit_name","regen_rumbo","regen_rumbo_unit_name","regen_especie_code",
                  "regen_especie_scientific_name","regen_especie_vernacular_name","regen_especie_language_code",
                  "regen_especie_language_variety","regen_frec"]

        writer = csv.writer(outfile, dialect='excel')
        writer.writerow(header)
        for p in self.plots:
            tmp = self.plots[p].export_regeneracion()
            for s in tmp:
                #Check if lenght correspont to header
                if str.split(s,',').__len__() == header.__len__():
                    outfile.write(s + '\n')
                else:
                    print "File header length is not equal the number of variables in the regeneration export"
        outfile.close()

    def export_equipo(self, outfile):
        """
        Function to create the csv file with the information on the equipment / team

        :param outfile: File path to the output file
        :return:
        """

        self.update_equipo_position()
        outfile = open(outfile, 'wb')

        header = ["parcela_parcela_id","parcela_pm_censo","_equipo_position","equipo_nom","equipo_app","equipo_cargo",
                  "equipo_emp"]

        writer = csv.writer(outfile, dialect='excel')
        writer.writerow(header)
        for p in self.plots:
            tmp = self.plots[p].export_equipo()
            for s in tmp:
                #Check if lenght correspont to header
                if str.split(s,',').__len__() == header.__len__():
                    outfile.write(s + '\n')
                else:
                    print "File header length is not equal the number of variables in the  equipo export"
        outfile.close()

    def export_sanidad(self, outfile):
        """
        Function to create the csv file with the information on forest health

        :param outfile: File path to the output file
        :return:
        """
        outfile = open(outfile, 'wb')

        header = ["parcela_parcela_id","parcela_pm_censo","san_genero","san_arbol_id","san_dap","san_dap_unit_name",
                  "san_categoria","san_tipo_fuste","san_porcopa","san_enfermedad","san_causa_euca1",
                  "san_causa_euca1_qualifier","san_causa_euca1_estado","san_causa_euca1_estado_qualifier",
                  "san_causa_euca2","san_causa_euca2_qualifier","san_causa_euca2_estado",
                  "san_causa_euca2_estado_qualifier","san_causa_euca3","san_causa_euca3_qualifier",
                  "san_causa_euca3_estado","san_causa_euca3_estado_qualifier","san_causa_euca4",
                  "san_causa_euca4_qualifier","san_causa_euca4_estado","san_causa_euca4_estado_qualifier",
                  "san_causa_pino1","san_causa_pino1_qualifier","san_causa_pino1_estado",
                  "san_causa_pino1_estado_qualifier","san_causa_pino2","san_causa_pino2_qualifier",
                  "san_causa_pino2_estado","san_causa_pino2_estado_qualifier","san_causa_pino3",
                  "san_causa_pino3_qualifier","san_causa_pino3_estado","san_causa_pino3_estado_qualifier",
                  "san_causa_pino4","san_causa_pino4_qualifier","san_causa_pino4_estado",
                  "san_causa_pino4_estado_qualifier"]

        writer = csv.writer(outfile, dialect='excel')
        writer.writerow(header)
        for p in self.plots:
            tmp = self.plots[p].export_sanidad()
            for s in tmp:
                #Check if lenght correspont to header
                if str.split(s,',').__len__() == header.__len__():
                    outfile.write(s + '\n')
                else:
                    print "File header length is not equal the number of variables in the  sanidad export"
        outfile.close()

class Plot:
    """
    Base class for all plot level information
    """

    def __init__(self, name, plot_id):
        self.name = name
        self.parcela_id = plot_id
        self.pm_censo = 1
        self.pm_coord_crs = None
        self.pm_coord_x = None
        self.pm_coord_y = None
        self.pm_altitude = None
        self.pm_altitude_unit_name = None
        self.pm_departamento = None
        self.pm_cuenca = None
        self.pm_subcuenca = None
        self.pm_censal = None
        self.general_datos_parcela_estado_1 = None
        self.general_datos_parcela_estado_2 = None
        self.general_datos_parcela_estado_3 = None
        self.general_datos_parcela_commentario = None
        self.general_datos_parcela_bosque_tipo = None
        self.general_datos_parcela_bosque_sub_tipo = None
        self.general_datos_parcela_fecha_observation_year = None
        self.general_datos_parcela_fecha_observation_month = None
        self.general_datos_parcela_fecha_observation_day = None
        self.general_datos_parcela_accesibilidad = None
        self.general_datos_parcela_propietario = None
        self.general_datos_parcela_predio = None
        self.parcela_coordenadas_gps_coord_srs = None
        self.parcela_coordenadas_gps_coord_x = None
        self.parcela_coordenadas_gps_coord_y = None
        self.parcela_coordenadas_gps_altidud = None
        self.parcela_coordenadas_gps_altiudud_unit = None
        self.track_fichero = None
        self.track_archivo = None
        self.relieve_relieve_ubicacion = None
        self.relieve_relieve_exposicion = None
        self.relieve_relieve_pendiente = None
        self.relieve_relieve_pendiente_forma = None
        self.suelo_suelo_coneat = None
        self.suelo_suelo_uso_tierra = None
        self.suelo_suelo_uso_previo = None
        self.suelo_suelo_labranza = None
        self.suelo_suelo_erosion_grado = None
        self.suelo_suelo_erosion_tipo = None
        self.suelo_suelo_profundidad_horizonte = None
        self.suelo_suelo_profundidad_mantillo = None
        self.suelo_suelo_profundidad_humus = None
        self.suelo_suelo_color = None
        self.suelo_suelo_textura = None
        self.suelo_suelo_estructura = None
        self.suelo_suelo_drenaje = None
        self.suelo_suelo_infiltracion = None
        self.suelo_suelo_impedimento = None
        self.suelo_suelo_olor = None
        self.suelo_suelo_humedad = None
        self.suelo_suelo_pedregosidad = None
        self.suelo_suelo_pedregosidad_unit_name = None
        self.suelo_suelo_rocosidad = None
        self.suelo_suelo_rocosidad_unit_name = None
        self.suelo_suelo_micorrizas = None
        self.suelo_suelo_fauna = None
        self.suelo_suelo_raices = None
        self.cobertura_vegetal_cobertura_copas = None
        self.cobertura_vegetal_cobertura_sotobosque = None
        self.cobertura_vegetal_cobertura_herbacea = None
        self.cobertura_vegetal_cobertura_residuos_plantas = None
        self.cobertura_vegetal_cobertura_residuos_cultivos = None
        self.flora_soto_flora_soto_presencia = None
        self.agua_agua_presencia = None
        self.agua_agua_caudal = None
        self.agua_agua_distancia = None
        self.agua_agua_distancia_unit_name = None
        self.agua_agua_nombre = None
        self.agua_agua_manejo = None
        self.agua_agua_frec = None
        self.agua_agua_acuicultura = None
        self.agua_agua_contaminacion = None
        self.ambiental_ambiental_potabilidad = None
        self.ambiental_ambiental_polucion = None
        self.ambiental_ambiental_fertalidad = None
        self.ambiental_ambiental_invasion = None
        self.ambiental_ambiental_pesticida = None
        self.fuego_fuego_evidencia = None
        self.fuego_fuego_tipo = None
        self.fuego_fuego_proposito = None
        self.rumbo = None
        self.plantacion_plant_especie_code = None
        self.plantacion_plant_especie_scientific_name = None
        self.plantacion_plant_especie_vernacular_name = None
        self.plantacion_plant_especie_language_code = None
        self.plantacion_plant_especie_language_variety = None
        self.plantacion_plant_edad = None
        self.plantacion_plant_raleo = None
        self.plantacion_plant_poda = None
        self.plantacion_plant_poda_altura = None
        self.plantacion_plant_poda_altura_unit_name = None
        self.plantacion_plant_regular = None
        self.plantacion_plant_dist_fila = None
        self.plantacion_plant_dist_fila_unit_name = None
        self.plantacion_plant_dist_entrefila = None
        self.plantacion_plant_dist_entrefila_unit_name = None
        self.plantacion_plant_fila_cantidad = None
        self.plantacion_plant_dist_silvopast = None
        self.plantacion_plant_dist_silvopast_unit_name = None
        self.plantacion_plant_adaptacion = None
        self.plantacion_plant_regimen = None
        self.plantacion_plant_estado = None
        self.forestacion_forest_origen = None
        self.forestacion_forest_estructura = None
        self.forestacion_forest_propiedad = None
        self.forestacion_forest_plan_manejo = None
        self.forestacion_forest_intervencion = None
        self.forestacion_forest_madera_destino_1 = None
        self.forestacion_forest_madera_destino_2 = None
        self.forestacion_forest_madera_destino_3 = None
        self.forestacion_forest_madera_destino_4 = None
        self.forestacion_forest_madera_destino_5 = None
        self.forestacion_forest_madera_destino_6 = None
        self.forestacion_forest_silvicultura = None
        self.forestacion_forest_tecnologia = None
        self.ntfp_ntfp_ganado_tipo_1 = None
        self.ntfp_ntfp_ganado_tipo_2 = None
        self.ntfp_ntfp_ganado_tipo_3 = None
        self.ntfp_ntfp_ganado_tipo_4 = None
        self.ntfp_ntfp_ganado_tipo_5 = None
        self.ntfp_ntfp_pastoreo_intens = None
        self.ntfp_ntfp_prod_cultivo = None
        self.ntfp_ntfp_prod_apicola = None
        self.ntfp_ntfp_semillas = None
        self.ntfp_ntfp_sombra = None
        self.ntfp_ntfp_caza_pesca = None
        self.ntfp_ntfp_rompe_vientos = None
        self.ntfp_ntfp_recreacion = None
        self.ntfp_ntfp_hongos = None
        self.ntfp_ntfp_cientificos = None
        self.ntfp_ntfp_aceites = None
        self.ntfp_ntfp_carbono = None
        self.pm_padron = None
        self.san_rumbo = None
        self.san_rumbo_unit_name = None
        self.trees = {}
        self.distances = {}
        self.fauna_aves = {}
        self.fauna_mamiferos = {}
        self.fauna_reptiles = {}
        self.fauna_anfibios = {}
        self.flora_suelo = {}
        self.flora_soto = {}
        self.fotos = {}
        self.invasoras = {}
        self.regeneracion = {}
        self.equipo = {}
        self.sanidad = {}

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
    def add_foto(self, foto_id):
        """
        Function to add a new foto to the plot

        :param foto_id: The unique name of the foto
        """
        if foto_id not in self.fotos.keys():
            self.fotos[foto_id] = Foto(foto_id=foto_id)
            print "Adding Foto: {}".format(foto_id)
        else:
            raise ValueError("Foto with name {fotoid} already exits in plot {plotid}".format(fotoid=foto_id,
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
              '{parcela_coord_crs},' \
              '{parcela_coord_x},' \
              '{parcela_coord_y},' \
              '{parcela_coord_altitude},' \
              '"{parcela_altitude_unit_name}",' \
              '{pm_departamento},' \
              '{parcela_cuenca},' \
              '{parcela_subcuenca},' \
              '"{parcela_censal}",' \
              '{parcela_general_estados_nivel1},' \
              '{parcela_general_estados_nivel2},' \
              '{parcela_general_estados_nivel3},'\
              '"{parcela_general_commentario}",' \
              '{parcela_general_bosque_tipo},' \
              '{parcela_general_bosque_sub_tipo},' \
              '{parcela_fecha_relev_year},' \
              '{parcela_fecha_relev_month},' \
              '{parcela_fecha_relev_day},' \
              '{parcela_general_accesibilidad},' \
              '"{parcela_general_propietario}",' \
              '"{parcela_general_predio}",' \
              '{parcela_coordinados_gps_coord_SRS},' \
              '{parcela_coordinados_gps_coord_x},' \
              '{parcela_coordinados_gps_coord_y},' \
              '{parcela_coordinados_gps_altidude},' \
              '"{parcela_coordinados_gps_altidude_unit_name}",' \
              '"{parcela_track_archivo}",' \
              '"{parcela_track_fichero}",' \
              '{parcela_relieve_relieve_ubicacion},' \
              '{parcela_relieve_relieve_exposicion},' \
              '{parcela_relieve_relieve_pendiente},' \
              '{parcela_relieve_relieve_pendiente_forma},' \
              '{parcela_suelo_suelo_coneat},' \
              '{parcela_suelo_suelo_uso_tierra},' \
              '{parcela_suelo_suelo_uso_previo},' \
              '{parcela_suelo_suelo_labranza},' \
              '{parcela_suelo_suelo_erosion_grado},' \
              '{parcela_suelo_suelo_erosion_tipo},' \
              '{parcela_suelo_suelo_profundidad_horizonte},' \
              '{parcela_suelo_suelo_profundidad_mantillo},' \
              '{parcela_suelo_suelo_profundidad_humus},' \
              '{parcela_suelo_suelo_color},' \
              '{parcela_suelo_suelo_textura},' \
              '{parcela_suelo_suelo_estructura},' \
              '{parcela_suelo_suelo_drenaje},' \
              '{parcela_suelo_suelo_infiltracion},' \
              '{parcela_suelo_suelo_impedimento},' \
              '{parcela_suelo_suelo_olor},' \
              '{parcela_suelo_suelo_humedad},' \
              '{parcela_suelo_suelo_pedregosidad},' \
              '{parcela_suelo_suelo_pedregosidad_unit_name},' \
              '{suelo_suelo_rocosidad},' \
              '"{suelo_suelo_rocosidad_unit_name}",' \
              '{parcela_suelo_suelo_micorrizas},' \
              '{parcela_suelo_suelo_fauna},' \
              '{suelo_suelo_raices},' \
              '{cobertura_vegetal_cobertura_copas},' \
              '{cobertura_vegetal_cobertura_sotobosque},' \
              '{cobertura_vegetal_cobertura_herbacea},' \
              '{cobertura_vegetal_cobertura_residuos_plantas},' \
              '{cobertura_vegetal_cobertura_residuos_cultivos},' \
              '{flora_soto_flora_soto_presencia},' \
              '{agua_agua_presencia},' \
              '{agua_agua_caudal},' \
              '{agua_agua_distancia},' \
              '"{agua_agua_distancia_unit_name}",' \
              '{agua_agua_nombre},' \
              '{agua_agua_manejo},' \
              '{agua_agua_frec},' \
              '{agua_agua_acuicultura},' \
              '{agua_agua_contaminacion},' \
              '{ambiental_ambiental_potabilidad},' \
              '{ambiental_ambiental_polucion},' \
              '{ambiental_ambiental_fertalidad},' \
              '{ambiental_ambiental_invasion},' \
              '{ambiental_ambiental_pesticida},' \
              '{fuego_fuego_evidencia},' \
              '{fuego_fuego_tipo},' \
              '{fuego_fuego_proposito},' \
              '{plantacion_plant_especie_code},' \
              '"{plantacion_plant_especie_scientific_name}",' \
              '"{plantacion_plant_especie_vernacular_name}",' \
              '{plantacion_plant_especie_language_code},' \
              '{plantacion_plant_especie_language_variety},' \
              '{plantacion_plant_edad},' \
              '{plantacion_plant_raleo},' \
              '{plantacion_plant_poda},' \
              '{plantacion_plant_poda_altura},' \
              '"{plantacion_plant_poda_altura_unit_name}",' \
              '{plantacion_plant_regular},' \
              '{plantacion_plant_dist_fila},' \
              '"{plantacion_plant_dist_fila_unit_name}",' \
              '{plantacion_plant_dist_entrefila},' \
              '"{plantacion_plant_dist_entrefila_unit_name}",' \
              '{plantacion_plant_fila_cantidad},' \
              '{plantacion_plant_dist_silvopast},' \
              '"{plantacion_plant_dist_silvopast_unit_name}",' \
              '{plantacion_plant_adaptacion},' \
              '{plantacion_plant_regimen},' \
              '{plantacion_plant_estado},' \
              '{forestacion_forest_origen},' \
              '{forestacion_forest_estructura},' \
              '{forestacion_forest_propiedad},' \
              '{forestacion_forest_plan_manejo},' \
              '{forestacion_forest_intervencion},' \
              '{forestacion_forest_madera_destino_1},' \
              '{forestacion_forest_madera_destino_2},'\
              '{forestacion_forest_madera_destino_3},' \
              '{forestacion_forest_madera_destino_4},' \
              '{forestacion_forest_madera_destino_5},' \
              '{forestacion_forest_madera_destino_6},' \
              '{forestacion_forest_silvicultura},' \
              '{forestacion_forest_tecnologia},' \
              '{ntfp_ntfp_ganado_tipo_1},' \
              '{ntfp_ntfp_ganado_tipo_2},' \
              '{ntfp_ntfp_ganado_tipo_3},' \
              '{ntfp_ntfp_ganado_tipo_4},' \
              '{ntfp_ntfp_ganado_tipo_5},' \
              '{ntfp_ntfp_pastoreo_intens},' \
              '{ntfp_ntfp_prod_cultivo},' \
              '{ntfp_ntfp_prod_apicola},' \
              '{ntfp_ntfp_semillas},' \
              '{ntfp_ntfp_sombra},' \
              '{ntfp_ntfp_caza_pesca},' \
              '{ntfp_ntfp_rompe_vientos},' \
              '{ntfp_ntfp_recreacion},' \
              '{ntfp_ntfp_hongos},' \
              '{ntfp_ntfp_cientificos},' \
              '{ntfp_ntfp_aceites},' \
              '{ntfp_ntfp_carbono},' \
              '{pm_padron},' \
              '{san_rumbo},' \
              '"{san_rumbo_unit_name}"' \
            .format(parcela_id=self.parcela_id,
                    parcela_censo=self.pm_censo,
                    parcela_coord_crs=self.pm_coord_crs,
                    parcela_coord_x=self.pm_coord_x,
                    parcela_coord_y=self.pm_coord_y,
                    parcela_coord_altitude=self.pm_altitude,
                    parcela_altitude_unit_name=self.pm_altitude_unit_name,
                    pm_departamento=self.pm_departamento,
                    parcela_cuenca=self.pm_cuenca,
                    parcela_subcuenca=self.pm_subcuenca,
                    parcela_censal=self.pm_censal,
                    parcela_general_estados_nivel1=self.general_datos_parcela_estado_1,
                    parcela_general_estados_nivel2=self.general_datos_parcela_estado_2,
                    parcela_general_estados_nivel3=self.general_datos_parcela_estado_3,
                    parcela_general_commentario=self.general_datos_parcela_commentario,
                    parcela_general_bosque_tipo=self.general_datos_parcela_bosque_tipo,
                    parcela_general_bosque_sub_tipo=self.general_datos_parcela_bosque_sub_tipo,
                    parcela_fecha_relev_year=self.general_datos_parcela_fecha_observation_year,
                    parcela_fecha_relev_month=self.general_datos_parcela_fecha_observation_month,
                    parcela_fecha_relev_day=self.general_datos_parcela_fecha_observation_day,
                    parcela_general_accesibilidad=self.general_datos_parcela_accesibilidad,
                    parcela_general_propietario=self.general_datos_parcela_propietario,
                    parcela_general_predio=self.general_datos_parcela_predio,
                    parcela_coordinados_gps_coord_SRS=self.parcela_coordenadas_gps_coord_srs,
                    parcela_coordinados_gps_coord_x=self.parcela_coordenadas_gps_coord_x,
                    parcela_coordinados_gps_coord_y=self.parcela_coordenadas_gps_coord_y,
                    parcela_coordinados_gps_altidude=self.parcela_coordenadas_gps_altidud,
                    parcela_coordinados_gps_altidude_unit_name=self.parcela_coordenadas_gps_altiudud_unit,
                    parcela_track_archivo=self.track_archivo,
                    parcela_track_fichero=self.track_fichero,
                    parcela_relieve_relieve_ubicacion=self.relieve_relieve_ubicacion,
                    parcela_relieve_relieve_exposicion=self.relieve_relieve_exposicion,
                    parcela_relieve_relieve_pendiente=self.relieve_relieve_pendiente,
                    parcela_relieve_relieve_pendiente_forma=self.relieve_relieve_pendiente_forma,
                    parcela_suelo_suelo_coneat=self.suelo_suelo_coneat,
                    parcela_suelo_suelo_uso_tierra=self.suelo_suelo_uso_tierra,
                    parcela_suelo_suelo_uso_previo=self.suelo_suelo_uso_previo,
                    parcela_suelo_suelo_labranza=self.suelo_suelo_labranza,
                    parcela_suelo_suelo_erosion_grado=self.suelo_suelo_erosion_grado,
                    parcela_suelo_suelo_erosion_tipo=self.suelo_suelo_erosion_tipo,
                    parcela_suelo_suelo_profundidad_horizonte=self.suelo_suelo_profundidad_horizonte,
                    parcela_suelo_suelo_profundidad_mantillo=self.suelo_suelo_profundidad_mantillo,
                    parcela_suelo_suelo_profundidad_humus=self.suelo_suelo_profundidad_humus,
                    parcela_suelo_suelo_color=self.suelo_suelo_color,
                    parcela_suelo_suelo_textura=self.suelo_suelo_textura,
                    parcela_suelo_suelo_estructura=self.suelo_suelo_estructura,
                    parcela_suelo_suelo_drenaje=self.suelo_suelo_drenaje,
                    parcela_suelo_suelo_infiltracion=self.suelo_suelo_infiltracion,
                    parcela_suelo_suelo_impedimento=self.suelo_suelo_impedimento,
                    parcela_suelo_suelo_olor=self.suelo_suelo_olor,
                    parcela_suelo_suelo_humedad=self.suelo_suelo_humedad,
                    parcela_suelo_suelo_pedregosidad=self.suelo_suelo_pedregosidad,
                    parcela_suelo_suelo_pedregosidad_unit_name=self.suelo_suelo_pedregosidad_unit_name,
                    suelo_suelo_rocosidad=self.suelo_suelo_rocosidad,
                    suelo_suelo_rocosidad_unit_name=self.suelo_suelo_rocosidad_unit_name,
                    parcela_suelo_suelo_micorrizas=self.suelo_suelo_micorrizas,
                    parcela_suelo_suelo_fauna=self.suelo_suelo_fauna,
                    suelo_suelo_raices=self.suelo_suelo_raices,
                    cobertura_vegetal_cobertura_copas=self.cobertura_vegetal_cobertura_copas,
                    cobertura_vegetal_cobertura_sotobosque=self.cobertura_vegetal_cobertura_sotobosque,
                    cobertura_vegetal_cobertura_herbacea=self.cobertura_vegetal_cobertura_herbacea,
                    cobertura_vegetal_cobertura_residuos_plantas=self.cobertura_vegetal_cobertura_residuos_plantas,
                    cobertura_vegetal_cobertura_residuos_cultivos=self.cobertura_vegetal_cobertura_residuos_cultivos,
                    flora_soto_flora_soto_presencia=self.flora_soto_flora_soto_presencia,
                    agua_agua_presencia=self.agua_agua_presencia,
                    agua_agua_caudal=self.agua_agua_caudal,
                    agua_agua_distancia=self.agua_agua_distancia,
                    agua_agua_distancia_unit_name=self.agua_agua_distancia_unit_name,
                    agua_agua_nombre=self.agua_agua_nombre,
                    agua_agua_manejo=self.agua_agua_manejo,
                    agua_agua_frec=self.agua_agua_frec,
                    agua_agua_acuicultura=self.agua_agua_acuicultura,
                    agua_agua_contaminacion=self.agua_agua_contaminacion,
                    ambiental_ambiental_potabilidad=self.ambiental_ambiental_potabilidad,
                    ambiental_ambiental_polucion=self.ambiental_ambiental_polucion,
                    ambiental_ambiental_fertalidad=self.ambiental_ambiental_fertalidad,
                    ambiental_ambiental_invasion=self.ambiental_ambiental_invasion,
                    ambiental_ambiental_pesticida=self.ambiental_ambiental_pesticida,
                    fuego_fuego_evidencia=self.fuego_fuego_evidencia,
                    fuego_fuego_tipo=self.fuego_fuego_tipo,
                    fuego_fuego_proposito=self.fuego_fuego_proposito,
                    plantacion_plant_especie_code=self.plantacion_plant_especie_code,
                    plantacion_plant_especie_scientific_name=self.plantacion_plant_especie_scientific_name,
                    plantacion_plant_especie_vernacular_name=self.plantacion_plant_especie_vernacular_name,
                    plantacion_plant_especie_language_code=self.plantacion_plant_especie_language_code,
                    plantacion_plant_especie_language_variety=self.plantacion_plant_especie_language_variety,
                    plantacion_plant_edad=self.plantacion_plant_edad,
                    plantacion_plant_raleo=self.plantacion_plant_raleo,
                    plantacion_plant_poda=self.plantacion_plant_poda,
                    plantacion_plant_poda_altura=self.plantacion_plant_poda_altura,
                    plantacion_plant_poda_altura_unit_name=self.plantacion_plant_poda_altura_unit_name,
                    plantacion_plant_regular=self.plantacion_plant_regular,
                    plantacion_plant_dist_fila=self.plantacion_plant_dist_fila,
                    plantacion_plant_dist_fila_unit_name=self.plantacion_plant_dist_fila_unit_name,
                    plantacion_plant_dist_entrefila=self.plantacion_plant_dist_entrefila,
                    plantacion_plant_dist_entrefila_unit_name=self.plantacion_plant_dist_entrefila_unit_name,
                    plantacion_plant_fila_cantidad=self.plantacion_plant_fila_cantidad,
                    plantacion_plant_dist_silvopast=self.plantacion_plant_dist_silvopast,
                    plantacion_plant_dist_silvopast_unit_name=self.plantacion_plant_dist_silvopast_unit_name,
                    plantacion_plant_adaptacion=self.plantacion_plant_adaptacion,
                    plantacion_plant_regimen=self.plantacion_plant_regimen,
                    plantacion_plant_estado=self.plantacion_plant_estado,
                    forestacion_forest_origen=self.forestacion_forest_origen,
                    forestacion_forest_estructura=self.forestacion_forest_estructura,
                    forestacion_forest_propiedad=self.forestacion_forest_propiedad,
                    forestacion_forest_plan_manejo=self.forestacion_forest_plan_manejo,
                    forestacion_forest_intervencion=self.forestacion_forest_intervencion,
                    forestacion_forest_madera_destino_1=self.forestacion_forest_madera_destino_1,
                    forestacion_forest_madera_destino_2=self.forestacion_forest_madera_destino_2,
                    forestacion_forest_madera_destino_3=self.forestacion_forest_madera_destino_3,
                    forestacion_forest_madera_destino_4=self.forestacion_forest_madera_destino_4,
                    forestacion_forest_madera_destino_5=self.forestacion_forest_madera_destino_5,
                    forestacion_forest_madera_destino_6=self.forestacion_forest_madera_destino_6,
                    forestacion_forest_silvicultura=self.forestacion_forest_silvicultura,
                    forestacion_forest_tecnologia=self.forestacion_forest_tecnologia,
                    ntfp_ntfp_ganado_tipo_1=self.ntfp_ntfp_ganado_tipo_1,
                    ntfp_ntfp_ganado_tipo_2=self.ntfp_ntfp_ganado_tipo_2,
                    ntfp_ntfp_ganado_tipo_3=self.ntfp_ntfp_ganado_tipo_3,
                    ntfp_ntfp_ganado_tipo_4=self.ntfp_ntfp_ganado_tipo_4,
                    ntfp_ntfp_ganado_tipo_5=self.ntfp_ntfp_ganado_tipo_5,
                    ntfp_ntfp_pastoreo_intens=self.ntfp_ntfp_pastoreo_intens,
                    ntfp_ntfp_prod_cultivo=self.ntfp_ntfp_prod_cultivo,
                    ntfp_ntfp_prod_apicola=self.ntfp_ntfp_prod_apicola,
                    ntfp_ntfp_semillas=self.ntfp_ntfp_semillas,
                    ntfp_ntfp_sombra=self.ntfp_ntfp_sombra,
                    ntfp_ntfp_caza_pesca=self.ntfp_ntfp_caza_pesca,
                    ntfp_ntfp_rompe_vientos=self.ntfp_ntfp_rompe_vientos,
                    ntfp_ntfp_recreacion=self.ntfp_ntfp_recreacion,
                    ntfp_ntfp_hongos=self.ntfp_ntfp_hongos,
                    ntfp_ntfp_cientificos=self.ntfp_ntfp_cientificos,
                    ntfp_ntfp_aceites=self.ntfp_ntfp_aceites,
                    ntfp_ntfp_carbono=self.ntfp_ntfp_carbono,
                    pm_padron=self.pm_padron,
                    san_rumbo=self.san_rumbo,
                    san_rumbo_unit_name=self.san_rumbo_unit_name
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
                         '"{arbol_unico_id}",' \
                         '"{arbol_especie_code}",' \
                         '"{arbol_especie_scientific_name}",' \
                         '"{arbol_especie_vernacular_name}",' \
                         '"{arbol_especie_language_code}",' \
                         '"{arbol_especie_language_variety}",' \
                         '"{arbol_dap1}",' \
                         '"{arbol_dap1_unit_name}",' \
                         '"{arbol_dap2}",' \
                         '"{arbol_dap2_unit_name}",' \
                         '"{arbol_dap}",' \
                         '"{arbol_dap_unit_name}",' \
                         '"{arbol_corteza_espesor}",' \
                         '"{arbol_corteza_espesor_unit_name}",' \
                         '"{arbol_distancia}",' \
                         '"{arbol_distancia_unit_name}",' \
                         '"{arbol_rumbo}",' \
                         '"{arbol_rumbo_unit_name}",' \
                         '"{arbol_ht}",' \
                         '"{arbol_ht_unit_name}",' \
                         '"{arbol_hc}",' \
                         '"{arbol_hc_unit_name}",' \
                         '"{arbol_hp}",' \
                         '"{arbol_hp_unit_name}",' \
                         '"{arbol_estrato}",' \
                         '"{arbol_rango_edad}",' \
                         '"{arbol_forma}",' \
                         '"{arbol_observacion}"' \
                    .format(parcela_parcela_id=self.parcela_id,
                            parcela_pm_censo=self.pm_censo,
                            _arbol_position=self.trees[key].stems[j].arbol_position,
                            arbol_parcela=self.trees[key].arbol_parcela,
                            arbol_id=self.trees[key].arbol_id,
                            arbol_fuste_id=self.trees[key].stems[j].stem_id,
                            arbol_unico_id=self.trees[key].arbol_unico_id,
                            arbol_especie_code=self.trees[key].arbol_especie_code,
                            arbol_especie_scientific_name=self.trees[key].arbol_especie_scientific_name,
                            arbol_especie_vernacular_name=self.trees[key].arbol_especie_vernacular_name,
                            arbol_especie_language_code=self.trees[key].arbol_especie_language_code,
                            arbol_especie_language_variety=self.trees[key].arbol_especie_language_variety,
                            arbol_dap1=self.trees[key].stems[j].dap1,
                            arbol_dap1_unit_name=self.trees[key].stems[j].dap1_unit_name,
                            arbol_dap2=self.trees[key].stems[j].dap2,
                            arbol_dap2_unit_name=self.trees[key].stems[j].dap2_unit_name,
                            arbol_dap=self.trees[key].stems[j].dap,
                            arbol_dap_unit_name=self.trees[key].stems[j].dap_unit_name,
                            arbol_corteza_espesor=self.trees[key].stems[j].corteza_espesor,
                            arbol_corteza_espesor_unit_name=self.trees[key].stems[j].corteza_espesor_unit_name,
                            arbol_distancia=self.trees[key].stems[j].distancia,
                            arbol_distancia_unit_name=self.trees[key].stems[j].distancia_unit_name,
                            arbol_rumbo=self.trees[key].stems[j].rumbo,
                            arbol_rumbo_unit_name=self.trees[key].stems[j].rumbo_unit_name,
                            arbol_ht=self.trees[key].stems[j].ht,
                            arbol_ht_unit_name=self.trees[key].stems[j].ht_unit_name,
                            arbol_hc=self.trees[key].stems[j].hc,
                            arbol_hc_unit_name=self.trees[key].stems[j].hc_unit_name,
                            arbol_hp=self.trees[key].stems[j].hp,
                            arbol_hp_unit_name=self.trees[key].stems[j].hp_unit_name,
                            arbol_estrato=self.trees[key].stems[j].estrado,
                            arbol_rango_edad=self.trees[key].stems[j].rango_edad,
                            arbol_forma=self.trees[key].stems[j].forma,
                            arbol_observacion=self.trees[key].stems[j].observacion)
                # print string
                out.append(string)
        result = []
        for i in out:
            result.append(str.replace(i, 'None', ''))
        return result

    def export_distances(self):
        """ Function to create the strings for the distance measurements from the plot class

        :return: List of strings of each distance recorded in OF Collect format
        """
        out = []
        for key in self.distances:
            string = '"{parcela_parcela_id}",' \
                     '"{parcela_pm_censo}",' \
                     '"{distancia_position}",' \
                     '"{distancia_categoria}",' \
                     '"{distancia_kilometros}",' \
                     '"{distancia_kilometros_unit_name}",' \
                     '"{rumbo_punto_gps_centro}",' \
                     '"{rumbo_punto_gps_centro_unit_name}",' \
                     '"{distancia_camino_estado}"' \
                .format(parcela_parcela_id=self.parcela_id,
                        parcela_pm_censo=self.pm_censo,
                        distancia_position=self.distances[key].distancia_position,
                        distancia_categoria=self.distances[key].distancia_categoria,
                        distancia_kilometros=self.distances[key].distancia_kilometros,
                        distancia_kilometros_unit_name=self.distances[key].distancia_kilometros_unit_name,
                        rumbo_punto_gps_centro=self.distances[key].rumbo_punto_gps_centro,
                        rumbo_punto_gps_centro_unit_name=self.distances[key].rumbo_punto_gps_centro_unit_name,
                        distancia_camino_estado=self.distances[key].distancia_camino_estado)
            out.append(string)
        result = []
        for i in out:
            result.append(str.replace(i, 'None', ''))
        return result

    def export_fauna_aves(self):
        """ Function to create the strings for the fauna aves observations from the plot class

        :return: List of strings of each fauna recorded in OF Collect format
        """
        out = []
        for key in self.fauna_aves:
            string = '"{parcela_parcela_id}",' \
                     '"{parcela_pm_censo}",' \
                     '"{position}",' \
                     '"{fauna_especies_code}",' \
                     '"{fauna_especie_scientific_name}",' \
                     '"{fauna_especie_vernacular_name}",' \
                     '"{fauna_especie_language_code}",' \
                     '"{aves_especie_language_variety}",' \
                     '"{fauna_tipo_observacion}",' \
                     '"{fauna_cant}"' \
                .format(parcela_parcela_id=self.parcela_id,
                        parcela_pm_censo=self.pm_censo,
                        position=self.fauna_aves[key].position,
                        fauna_especies_code=self.fauna_aves[key].fauna_especies_code,
                        fauna_especie_scientific_name=self.fauna_aves[key].fauna_especie_scientific_name,
                        fauna_especie_vernacular_name=self.fauna_aves[key].fauna_especie_vernacular_name,
                        fauna_especie_language_code=self.fauna_aves[key].fauna_especie_language_code,
                        aves_especie_language_variety=self.fauna_aves[key].fauna_especie_language_variety,
                        fauna_tipo_observacion=self.fauna_aves[key].fauna_tipo_observacion,
                        fauna_cant=self.fauna_aves[key].fauna_cant)
            out.append(string)
        result = []
        for i in out:
            result.append(str.replace(i, 'None', ''))
        return result


    def export_fauna_mamiferos(self):
        """ Function to create the strings for the mammal observations from the plot class

        :return: List of strings of each fauna recorded in OF Collect format
        """
        out = []
        for key in self.fauna_mamiferos:
            string = '"{parcela_parcela_id}",' \
                     '"{parcela_pm_censo}",' \
                     '"{position}",' \
                     '"{fauna_especies_code}",' \
                     '"{fauna_especie_scientific_name}",' \
                     '"{fauna_especie_vernacular_name}",' \
                     '"{fauna_especie_language_code}",' \
                     '"{mamifero_especie_language_variety}",' \
                     '"{fauna_tipo}",' \
                     '"{fauna_cant}"' \
                .format(parcela_parcela_id=self.parcela_id,
                        parcela_pm_censo=self.pm_censo,
                        position=self.fauna_mamiferos[key].position,
                        fauna_especies_code=self.fauna_mamiferos[key].fauna_especies_code,
                        fauna_especie_scientific_name=self.fauna_mamiferos[key].fauna_especie_scientific_name,
                        fauna_especie_vernacular_name=self.fauna_mamiferos[key].fauna_especie_vernacular_name,
                        fauna_especie_language_code=self.fauna_mamiferos[key].fauna_especie_language_code,
                        mamifero_especie_language_variety=self.fauna_mamiferos[key].fauna_especie_language_variety,
                        fauna_tipo=self.fauna_mamiferos[key].fauna_tipo_observacion,
                        fauna_cant=self.fauna_mamiferos[key].fauna_cant)
            out.append(string)
        result = []
        for i in out:
            result.append(str.replace(i, 'None', ''))
        return result

    def export_fauna_reptiles(self):
        """ Function to create the strings for the reptile observations from the plot class

        :return: List of strings of each fauna recorded in OF Collect format
        """
        out = []
        for key in self.fauna_reptiles:
            string = '"{parcela_parcela_id}",' \
                     '"{parcela_pm_censo}",' \
                     '"{position}",' \
                     '"{fauna_especies_code}",' \
                     '"{fauna_especie_scientific_name}",' \
                     '"{fauna_especie_vernacular_name}",' \
                     '"{fauna_especie_language_code}",' \
                     '"{reptil_especie_language_variety}",' \
                     '"{fauna_tipo}",' \
                     '"{fauna_cant}"' \
                .format(parcela_parcela_id=self.parcela_id,
                        parcela_pm_censo=self.pm_censo,
                        position=self.fauna_reptiles[key].position,
                        fauna_especies_code=self.fauna_reptiles[key].fauna_especies_code,
                        fauna_especie_scientific_name=self.fauna_reptiles[key].fauna_especie_scientific_name,
                        fauna_especie_vernacular_name=self.fauna_reptiles[key].fauna_especie_vernacular_name,
                        fauna_especie_language_code=self.fauna_reptiles[key].fauna_especie_language_code,
                        reptil_especie_language_variety=self.fauna_reptiles[key].fauna_especie_language_variety,
                        fauna_tipo=self.fauna_reptiles[key].fauna_tipo_observacion,
                        fauna_cant=self.fauna_reptiles[key].fauna_cant)
            out.append(string)
        result = []
        for i in out:
            result.append(str.replace(i, 'None', ''))
        return result

    def export_fauna_anfibios(self):
        """ Function to create the strings for the amphibians observations

        :return: List of strings of each fauna recorded in OF Collect format
        """
        out = []
        for key in self.fauna_anfibios:
            string = '"{parcela_parcela_id}",' \
                     '"{parcela_pm_censo}",' \
                     '"{position}",' \
                     '"{fauna_especies_code}",' \
                     '"{fauna_especie_scientific_name}",' \
                     '"{fauna_especie_vernacular_name}",' \
                     '"{fauna_especie_language_code}",' \
                     '"{reptil_especie_language_variety}",' \
                     '"{fauna_tipo}",' \
                     '"{fauna_cant}"' \
                .format(parcela_parcela_id=self.parcela_id,
                        parcela_pm_censo=self.pm_censo,
                        position=self.fauna_anfibios[key].position,
                        fauna_especies_code=self.fauna_anfibios[key].fauna_especies_code,
                        fauna_especie_scientific_name=self.fauna_anfibios[key].fauna_especie_scientific_name,
                        fauna_especie_vernacular_name=self.fauna_anfibios[key].fauna_especie_vernacular_name,
                        fauna_especie_language_code=self.fauna_anfibios[key].fauna_especie_language_code,
                        reptil_especie_language_variety=self.fauna_anfibios[key].fauna_especie_language_variety,
                        fauna_tipo=self.fauna_anfibios[key].fauna_tipo_observacion,
                        fauna_cant=self.fauna_anfibios[key].fauna_cant)
            out.append(string)
        result = []
        for i in out:
            result.append(str.replace(i, 'None', ''))
        return result

    def export_flora_suelo(self):
        """ Function to create the strings for the soil flora observations from the plot class

        :return: List of strings of each soil flora recorded
        """
        out = []
        for key in self.flora_suelo:
            string = '"{parcela_parcela_id}",' \
                     '"{parcela_pm_censo}",' \
                     '"{position}",' \
                     '"{flora_suelo_especies_code}",' \
                     '"{flora_suelo_especie_scientific_name}",' \
                     '"{flora_suelo_especie_vernacular_name}",' \
                     '"{flora_suelo_especie_language_code}",' \
                     '"{flora_especie_language_variety}",' \
                     '"{flora_suelo_freq}"' \
                .format(parcela_parcela_id=self.parcela_id,
                        parcela_pm_censo=self.pm_censo,
                        position=self.flora_suelo[key].position,
                        flora_suelo_especies_code=self.flora_suelo[key].flora_suelo_especies_code,
                        flora_suelo_especie_scientific_name=self.flora_suelo[key].flora_suelo_especie_scientific_name,
                        flora_suelo_especie_vernacular_name=self.flora_suelo[key].flora_suelo_especie_vernacular_name,
                        flora_suelo_especie_language_code=self.flora_suelo[key].flora_suelo_especie_language_code,
                        flora_especie_language_variety=self.flora_suelo[key].flora_suelo_especie_language_variety,
                        flora_suelo_freq=self.flora_suelo[key].flora_suelo_freq)
            out.append(string)
        result = []
        for i in out:
            result.append(str.replace(i, 'None', ''))
        return result

    def export_flora_soto(self):
        """ Function to create the strings for the forest flora observations from the plot class

        :return: List of strings of each flora soto recorded in OF Collect format
        """
        out = []
        for key in self.flora_soto:
            string = '"{parcela_parcela_id}",' \
                     '"{parcela_pm_censo}",' \
                     '"{position}",' \
                     '"{flora_soto_tipo}",' \
                     '"{flora_soto_altura}",' \
                     '"{flora_soto_altura_unit_name}"'\
                .format(parcela_parcela_id=self.parcela_id,
                        parcela_pm_censo=self.pm_censo,
                        position=self.flora_soto[key].position,
                        flora_soto_tipo=self.flora_soto[key].flora_soto_tipo,
                        flora_soto_altura=self.flora_soto[key].flora_soto_altura,
                        flora_soto_altura_unit_name=self.flora_soto[key].flora_soto_altura_unit_name)
            out.append(string)
        result = []
        for i in out:
            result.append(str.replace(i, 'None', ''))
        return result

    def export_fotos(self):
        """ Function to create the strings for the foto observations from the plot class

        :return: List of strings of each foto recorded in OF Collect format
        """
        out = []
        for key in self.fotos:
            string = '"{parcela_parcela_id}",' \
                     '"{parcela_pm_censo}",' \
                     '"{position}",' \
                     '"{foto_tipo}",' \
                     '"{foto_coord_srs}",' \
                     '"{foto_coord_y}",' \
                     '"{foto_coord_x}",' \
                     '"{foto_descr}",' \
                     '"{foto_archivo}",' \
                     '"{foto_fichero}"' \
         .format(parcela_parcela_id=self.parcela_id,
                        parcela_pm_censo=self.pm_censo,
                        position=self.fotos[key].foto_position,
                        foto_tipo=self.fotos[key].foto_tipo,
                        foto_coord_srs=self.fotos[key].foto_systema_referencia,
                        foto_coord_y=self.fotos[key].foto_lat,
                        foto_coord_x=self.fotos[key].foto_lon,
                        foto_descr=self.fotos[key].foto_desc,
                        foto_archivo=self.fotos[key].foto_archivo,
                        foto_fichero=self.fotos[key].foto_fichero)
            out.append(string)
        result = []
        for i in out:
            result.append(str.replace(i, 'None', ''))
        return result

    def export_invasoras(self):
        """ Function to create the strings for the invasive species observations from the plot class

        :return: List of strings of each invasive species recorded in OF Collect format
        """
        out = []
        for key in self.invasoras:
            string = '"{parcela_parcela_id}",' \
                     '"{parcela_pm_censo}",' \
                     '"{position}",' \
                     '"{invasora_categoria}",' \
                     '"{invasora_especie_code}",' \
                     '"{invasora_especie_scientific_name}",' \
                     '"{invasora_especie_vernacular_name}",' \
                     '"{invasora_especie_language_code}",' \
                     '"{invasora_especie_language_variety}",' \
                     '"{invasora_severidad}"' \
         .format(parcela_parcela_id=self.parcela_id,
                        parcela_pm_censo=self.pm_censo,
                        position=self.invasoras[key].invasora_position,
                        invasora_categoria=self.invasoras[key].invasora_categoria,
                        invasora_especie_code=self.invasoras[key].invasora_especie_code,
                        invasora_especie_scientific_name=self.invasoras[key].invasora_especie_scientific_name,
                        invasora_especie_vernacular_name=self.invasoras[key].invasora_especie_vernacular_name,
                        invasora_especie_language_code=self.invasoras[key].invasora_especie_language_code,
                        invasora_especie_language_variety=self.invasoras[key].invasora_especie_language_variety,
                        invasora_severidad=self.invasoras[key].invasora_severidad)
            out.append(string)
        result = []
        for i in out:
            result.append(str.replace(i, 'None', ''))
        return result

    def export_regeneracion(self):
        """ Function to create the strings for the regeneration observations from the plot class

        :return: List of strings of each regerneration record in OF Collect format
        """
        out = []
        for key in self.regeneracion:
            string = '"{parcela_parcela_id}",' \
                     '"{parcela_pm_censo}",' \
                     '"{position}",' \
                     '"{regen_subparcela_id}",' \
                     '"{regen_distancia}",' \
                     '"{regen_distancia_unit_name}",'\
                     '"{regen_rumbo}",'\
                     '"{regen_rumbo_unit_name}",'\
                     '"{regen_especie_code}",' \
                     '"{regen_especie_scientific_name}",' \
                     '"{regen_especie_vernacular_name}",' \
                     '"{regen_especie_language_code}",' \
                     '"{regen_especie_language_variety}",' \
                     '"{regen_frec}"' \
         .format(parcela_parcela_id=self.parcela_id,
                        parcela_pm_censo=self.pm_censo,
                        position=self.regeneracion[key].regen_position,
                        regen_subparcela_id=self.regeneracion[key].regen_subparcela_id,
                        regen_distancia=self.regeneracion[key].regen_distancia,
                        regen_distancia_unit_name=self.regeneracion[key].regen_distancia_unit_name,
                        regen_rumbo=self.regeneracion[key].regen_rumbo,
                        regen_rumbo_unit_name=self.regeneracion[key].regen_rumbo_unit_name,
                        regen_especie_code=self.regeneracion[key].regen_especie_code,
                        regen_especie_scientific_name=self.regeneracion[key].regen_especie_scientific_name,
                        regen_especie_vernacular_name=self.regeneracion[key].regen_especie_vernacular_name,
                        regen_especie_language_code=self.regeneracion[key].regen_especie_language_code,
                        regen_especie_language_variety=self.regeneracion[key].regen_especie_language_variety,
                        regen_frec=self.regeneracion[key].regen_frec)
            out.append(string)
        result = []
        for i in out:
            result.append(str.replace(i, 'None', ''))
        return result

    def export_equipo(self):
        """ Function to create the strings for the equipment / team  observation from the plot class

        :return: List of strings of each equipment recorded in OF Collect format
        """
        out = []
        for key in self.equipo:
            string = '"{parcela_parcela_id}",' \
                     '"{parcela_pm_censo}",' \
                     '"{position}",' \
                     '"{equipo_nom}",' \
                     '"{equipo_app}",' \
                     '"{equipo_cargo}",' \
                     '"{equipo_emp}"' \
         .format(parcela_parcela_id=self.parcela_id,
                        parcela_pm_censo=self.pm_censo,
                        position=self.equipo[key].equipo_position,
                        equipo_nom=self.equipo[key].equipo_nom,
                        equipo_app=self.equipo[key].equipo_app,
                        equipo_cargo=self.equipo[key].equipo_cargo,
                        equipo_emp=self.equipo[key].equipo_emp)
            out.append(string)
        result = []
        for i in out:
            result.append(str.replace(i, 'None', ''))
        return result

    def export_sanidad(self):
        """ Function to create the strings for the forest health observations

        :return: List of strings of each forest health record in OF Collect format
        """
        out = []
        for key in self.equipo:
            string = '"{parcela_parcela_id}",' \
                     '"{parcela_pm_censo}",' \
                     '"{san_genero}",' \
                     '"{san_arbol_id}",' \
                     '"{san_dap}",' \
                     '"{san_dap_unit_name}",' \
                     '"{san_categoria}",' \
                     '"{san_tipo_fuste}",' \
                     '"{san_porcopa}",' \
                     '"{san_enfermedad}",' \
                     '"{san_causa_euca1}",' \
                     '"{san_causa_euca1_qualifier}",' \
                     '"{san_causa_euca1_estado}",' \
                     '"{san_causa_euca1_estado_qualifier}",' \
                     '"{san_causa_euca2}",' \
                     '"{san_causa_euca2_qualifier}",' \
                     '"{san_causa_euca2_estado}",' \
                     '"{san_causa_euca2_estado_qualifier}",' \
                     '"{san_causa_euca3}",' \
                     '"{san_causa_euca3_qualifier}",' \
                     '"{san_causa_euca3_estado}",' \
                     '"{san_causa_euca3_estado_qualifier}",' \
                     '"{san_causa_euca4}",' \
                     '"{san_causa_euca4_qualifier}",' \
                     '"{san_causa_euca4_estado}",' \
                     '"{san_causa_euca4_estado_qualifier}",' \
                     '"{san_causa_pino1_qualifier}",' \
                     '"{san_causa_pino1_estado}",' \
                     '"{san_causa_pino1_estado_qualifier}",' \
                     '"{san_causa_pino2}",' \
                     '"{san_causa_pino2_qualifier}",' \
                     '"{san_causa_pino2_estado}",' \
                     '"{san_causa_pino2_estado_qualifier}",' \
                     '"{san_causa_pino3}",' \
                     '"{san_causa_pino3_qualifier}",' \
                     '"{san_causa_pino3_estado}",' \
                     '"{san_causa_pino3_estado_qualifier}",' \
                     '"{san_causa_pino4}",' \
                     '"{san_causa_pino4_qualifier}",' \
                     '"{san_causa_pino4_estado}",' \
                     '"{san_causa_pino4_estado_qualifier}",' \
                .format(parcela_parcela_id=self.parcela_id,
                        parcela_pm_censo=self.pm_censo,
                        san_genero=self.sanidad[key].san_genero,
                        san_arbol_id=self.sanidad[key].san_arbol_id,
                        san_dap=self.sanidad[key].san_dap,
                        san_dap_unit_name=self.sanidad[key].san_dap_unit_name,
                        san_categoria=self.sanidad[key].san_categoria,
                        san_tipo_fuste=self.sanidad[key].san_tipo_fuste,
                        san_porcopa=self.sanidad[key].san_porcopa,
                        san_enfermedad=self.sanidad[key].san_enfermedad,
                        san_causa_euca1=self.sanidad[key].san_causa_euca1,
                        san_causa_euca1_qualifier=self.sanidad[key].san_causa_euca1_qualifier,
                        san_causa_euca1_estado=self.sanidad[key].san_causa_euca1_estado,
                        san_causa_euca1_estado_qualifier=self.sanidad[key].san_causa_euca1_estado_qualifier,
                        san_causa_euca2=self.sanidad[key].san_causa_euca1,
                        san_causa_euca2_qualifier=self.sanidad[key].san_causa_euca1_qualifier,
                        san_causa_euca2_estado=self.sanidad[key].san_causa_euca1_estado,
                        san_causa_euca2_estado_qualifier=self.sanidad[key].san_causa_euca1_estado_qualifier,
                        san_causa_euca3=self.sanidad[key].san_causa_euca1,
                        san_causa_euca3_qualifier=self.sanidad[key].san_causa_euca1_qualifier,
                        san_causa_euca3_estado=self.sanidad[key].san_causa_euca1_estado,
                        san_causa_euca3_estado_qualifier=self.sanidad[key].san_causa_euca1_estado_qualifier,
                        san_causa_euca4=self.sanidad[key].san_causa_euca1,
                        san_causa_euca4_qualifier=self.sanidad[key].san_causa_euca1_qualifier,
                        san_causa_euca4_estado=self.sanidad[key].san_causa_euca1_estado,
                        san_causa_euca4_estado_qualifier=self.sanidad[key].san_causa_euca1_estado_qualifier,
                        san_causa_pino1=self.sanidad[key].san_causa_pino1,
                        san_causa_pino1_qualifier=self.sanidad[key].san_causa_pino1_qualifier,
                        san_causa_pino1_estado=self.sanidad[key].san_causa_pino1_estado,
                        san_causa_pino1_estado_qualifier=self.sanidad[key].san_causa_pino1_estado_qualifier,
                        san_causa_pino2=self.sanidad[key].san_causa_pino1,
                        san_causa_pino2_qualifier=self.sanidad[key].san_causa_pino1_qualifier,
                        san_causa_pino2_estado=self.sanidad[key].san_causa_pino1_estado,
                        san_causa_pino2_estado_qualifier=self.sanidad[key].san_causa_pino1_estado_qualifier,
                        san_causa_pino3=self.sanidad[key].san_causa_pino1,
                        san_causa_pino3_qualifier=self.sanidad[key].san_causa_pino1_qualifier,
                        san_causa_pino3_estado=self.sanidad[key].san_causa_pino1_estado,
                        san_causa_pino3_estado_qualifier=self.sanidad[key].san_causa_pino1_estado_qualifier,
                        san_causa_pino4=self.sanidad[key].san_causa_pino1,
                        san_causa_pino4_qualifier=self.sanidad[key].san_causa_pino1_qualifier,
                        san_causa_pino4_estado=self.sanidad[key].san_causa_pino1_estado,
                        san_causa_pino4_estado_qualifier=self.sanidad[key].san_causa_pino1_estado_qualifier)

            out.append(string)
        result = []
        for i in out:
            result.append(str.replace(i, 'None', ''))
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
        self.corteza_espesor = None
        self.corteza_espesor_unit_name = None
        self.distancia = None
        self.distancia_unit_name = None
        self.rumbo = None
        self.rumbo_unit_name = None
        self.ht = ht
        self.ht_unit_name = None
        self.hc = None
        self.hc_unit_name = None
        self.hp = None
        self.hp_unit_name = None
        self.estrado = None
        self.rango_edad = None
        self.forma = None
        self.observacion = None

    def __str__(self):
        return "I am a stem"

class Distance:
    """
    Base class for all distance measurements
    """

    def __init__(self, parcela_parcela_id):
        self.parcela_parcela_id = parcela_parcela_id
        self.parcela_pm_censo = None
        self.distancia_position = None
        self.distancia_categoria = None
        self.distancia_kilometros = None
        self.distancia_kilometros_unit_name = None
        self.rumbo_punto_gps_centro = None
        self.rumbo_punto_gps_centro_unit_name = None
        self.distancia_camino_estado = None

    def __str__(self):
        return "I am a distance object"

class Fauna:
    """
    Base class for fauna observations
    """

    def __init__(self, parcela_parcela_id,fauna_especies_code):
        self.parcela_parcela_id = parcela_parcela_id
        self.parcela_pm_censo = None
        self.position = None
        self.fauna_especies_code = fauna_especies_code
        self.fauna_especie_scientific_name = None
        self.fauna_especie_vernacular_name = None
        self.fauna_especie_language_code = None
        self.fauna_especie_language_variety = None
        self.fauna_tipo_observacion = None
        self.fauna_cant = None

    def __str__(self):
        return "I am a fauna object"

class FloraSuelo:
    """
    Base class for soil fauna observations
    """
    def __init__(self, parcela_parcela_id,flora_suelo_especies_code):
        self.parcela_parcela_id = parcela_parcela_id
        self.parcela_pm_censo = None
        self.position = None
        self.flora_suelo_especies_code = flora_suelo_especies_code
        self.flora_suelo_especie_scientific_name = None
        self.flora_suelo_especie_vernacular_name = None
        self.flora_suelo_especie_language_code = None
        self.flora_suelo_especie_language_variety = None
        self.flora_suelo_freq = None

    def __str__(self):
        return "I am a flora suelo object"
    
class FloraSoto:
    """
    Base class for flora sotobosque observations
    """

    def __init__(self, parcela_parcela_id,flora_soto_tipo):
        self.parcela_parcela_id = parcela_parcela_id
        self.parcela_pm_censo = None
        self.position = None
        self.flora_soto_tipo = flora_soto_tipo
        self.flora_soto_altura = None
        self.flora_soto_altura_unit_name = None

    def __str__(self):
        return "I am a flora soto object"

class Foto:
    """
    Base class for foto information
    """

    def __init__(self, foto_id):
        self.foto_id=foto_id
        self.foto_position = None
        self.foto_tipo = None
        self.foto_desc = None
        self.foto_archivo = None
        self.foto_fichero = None
        self.foto_lat = None
        self.foto_lon = None
        self.foto_systema_referencia = None

    def __str__(self):
        return "I am an instance of class Fotos"

class Invasora:
    """
    Base class for invasive species
    """

    def __init__(self, invasora_id, especies_code):
        self.invasora_id = invasora_id
        self.invasora_especie_code = especies_code
        self.invasora_position = None
        self.invasora_categoria = None
        self.invasora_especie_scientific_name = None
        self.invasora_especie_vernacular_name = None
        self.invasora_especie_language_code = None
        self.invasora_especie_language_variety = None
        self.invasora_severidad = None

    def __str__(self):
        return "I am an instance of class Invensora"

class Regeneracion:
    """
    Base class for regeneration records
    """

    def __init__(self, regen_id, especies_code):
        self.regen_id = regen_id
        self.regen_especie_code = especies_code
        self.regen_position = None
        self.regen_subparcela_id = None
        self.regen_distancia = None
        self.regen_distancia_unit_name =None
        self.regen_rumbo = None
        self.regen_rumbo_unit_name =None
        self.regen_especie_scientific_name = None
        self.regen_especie_vernacular_name = None
        self.regen_especie_language_code = None
        self.regen_especie_language_variety = None
        self.regen_frec = None
    def __str__(self):
        return "I am an instance of class Regeneracion"

class Equipo:
    """
    Base class for equipment and team information
    """
    def __init__(self, equipo_nom):
        #self.equipo_id = equipo_id
        self.equipo_nom = equipo_nom
        self.equipo_app = None
        self.equipo_cargo = None
        self.equipo_emp = None
    def __str__(self):
        return "I am an instance of class Equipo"

class Sanidad:
    """
    Base class for forest health information
    """
    def __init__(self, sanidad_id):
        self.san_id = sanidad_id
        self.san_genero = None
        self.san_arbol_id = None
        self.san_dap = None
        self.san_dap_unit_name =None
        self.san_categoria = None
        self.san_tipo_fuste = None
        self.san_porcopa = None
        self.san_enfermedad = None
        self.san_causa_euca1 = None
        self.san_causa_euca1_qualifier = None
        self.san_causa_euca1_estado =None
        self.san_causa_euca1_estado_qualifier = None
        self.san_causa_euca2 = None
        self.san_causa_euca2_qualifier = None
        self.san_causa_euca2_estado =None
        self.san_causa_euca2_estado_qualifier = None
        self.san_causa_euca3 = None
        self.san_causa_euca3_qualifier = None
        self.san_causa_euca3_estado =None
        self.san_causa_euca3_estado_qualifier = None
        self.san_causa_euca4 = None
        self.san_causa_euca4_qualifier = None
        self.san_causa_euca4_estado =None
        self.san_causa_euca4_estado_qualifier = None
        self.san_causa_pino1 = None
        self.san_causa_pino1_qualifier = None
        self.san_causa_pino1_estado = None
        self.san_causa_pino1_estado_qualifier = None
        self.san_causa_pino2 = None
        self.san_causa_pino2_qualifier = None
        self.san_causa_pino2_estado = None
        self.san_causa_pino2_estado_qualifier = None
        self.san_causa_pino3 = None
        self.san_causa_pino3_qualifier = None
        self.san_causa_pino3_estado = None
        self.san_causa_pino3_estado_qualifier = None
        self.san_causa_pino4 = None
        self.san_causa_pino4_qualifier = None
        self.san_causa_pino4_estado = None
        self.san_causa_pino4_estado_qualifier = None
    def __str__(self):
        return "I am an instance of class Sanidad"

