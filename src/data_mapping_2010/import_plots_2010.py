#!/usr/bin/env python
# -*- coding: utf-8 -*-s
"""This module provides the functionality to import_modules the general plot information in to 2010 data format. It can be used
as a general python module in a python program are called as a python script from the console."""

__docformat__ = 'reStructuredText'
import csv
import logging
import os
import sys

from src.model import class_lib
from src.model import code_lists
from src.utils import tools_lib


def import_fni_plots_2010(survey, species_list, infile):
    """This function imports the plot data in the 2010 file format and adds the information to the survey instance.

    :param survey: A survey object into which the plot information will be added
    :param species_list: A list with tree species names as exported from the Collect species list
    :param infile: The file path to the 2010 plot data
    :type survey: An instance of :class:`~model.class_lib.Survey`
    :type species_list: A dictionary with instances of :class:`~model.class_lib.Species`
    :type infile: A file path
    :return: If executed as script a file with the plot information that can be imported in to OF Collect. Otherwise an
     updated survey object
    :rtype: :class:`~model.class_lib.Survey` / CSV File

    .. warning:: The mapping for the variable 'Uso de Tierra" is unclear as the classes in OF Collect are either
        'Agricola' or 'Ganadero'. However, in the 2010 DGF dataset we often find classes like "Ganadero Agricola".
        Therefore the dict "suelo_suelo_uso_tierra" in :mod:`~src.model.code_lists` should be adapted accordingly.

    """

    # Check if survey is of class survey
    try:
        isinstance(survey, class_lib.Survey)
    except:
        print "Survey is not of class Survey"
        sys.exit(0)

    # Check if files exits and readable
    try:
        open(infile, 'r')
    except IOError:
        print "Input file is missing or is not readable"
        sys.exit(0)

    with open(infile, 'rb') as csvfile:
        datareader = csv.DictReader(csvfile, delimiter=',')
        plot_counter = []
        for row in datareader:
            ID = row['nombre_pm']
            if ID in survey.plots.keys():
                # print "Processing PlotID:{}".format(ID)
                if ID not in plot_counter:
                    plot_counter.append(ID)
                survey.plots[ID].pm_censo = 1
                survey.plots[ID].pm_coord_crs = ''
                survey.plots[ID].pm_coord_x = ''
                survey.plots[ID].pm_coord_y = ''
                survey.plots[ID].pm_altitude = ''
                survey.plots[ID].pm_altitude_unit_name = 'metros'
                survey.plots[ID].pm_departamento = \
                    tools_lib.import_variable(row, 'departamento', 'code', ID, codelist=code_lists.departamento)
                survey.plots[ID].pm_cuenca = None
                survey.plots[ID].pm_subcuenca = None
                survey.plots[ID].pm_censal = None
                survey.plots[ID].general_datos_parcela_estado_1 = 1
                survey.plots[ID].general_datos_parcela_bosque_tipo = \
                    tools_lib.import_variable(row, 'tipoDeBosque', 'code', ID, codelist=code_lists.bosque_tipo)
                if survey.plots[ID].general_datos_parcela_bosque_tipo == 2:
                    # Set the nivel 3 category for all plantations to DAB > 3cm by default
                    survey.plots[ID].general_datos_parcela_estado_3 = 2

                survey.plots[ID].general_datos_parcela_bosque_sub_tipo = \
                    tools_lib.import_variable(row, 'subbosque', 'code', ID, codelist=code_lists.subbosque_tipo)

                if row['Observaciones'] in ['', ' ']:
                    survey.plots[ID].general_datos_parcela_commentario = '-'
                else:
                    survey.plots[ID].general_datos_parcela_commentario = \
                        tools_lib.import_variable(row, 'Observaciones', 'string', ID)
                date = str.split(row['fecha'], '/')
                if date.__len__() == 3:
                    survey.plots[ID].general_datos_parcela_fecha_observation_year = date[2]
                    survey.plots[ID].general_datos_parcela_fecha_observation_month = date[0]
                    survey.plots[ID].general_datos_parcela_fecha_observation_day = date[1]
                else:
                    error_msg = 'Cannot convert the variable \"fecha"\" with value "{date}" into a date for plot ' \
                                '{plotid}'.format(date=row['fecha'], plotid=ID)
                    logging.error(error_msg)

                survey.plots[ID].general_datos_parcela_accesibilidad = \
                    tools_lib.import_variable(row, 'facilidadProgresion', 'code', ID,
                                              codelist=code_lists.accesibilidad)
                survey.plots[ID].general_datos_parcela_propietario = \
                    tools_lib.import_variable(row, 'propietario', 'string', ID)
                survey.plots[ID].general_datos_parcela_predio = \
                    tools_lib.import_variable(row, 'predio', 'string', ID)
                survey.plots[ID].rumbo = \
                    tools_lib.import_variable(row, 'rumboCaminoCentroParcela', 'float', ID)
                survey.plots[ID].track_archivo = \
                    tools_lib.import_variable(row, 'track', 'string', ID)
                survey.plots[ID].parcela_coordenadas_gps_coord_x = \
                    tools_lib.import_variable(row, 'oeste', 'float', ID)
                survey.plots[ID].parcela_coordenadas_gps_coord_y = \
                    tools_lib.import_variable(row, 'sur', 'float', ID)
                survey.plots[ID].parcela_coordenadas_gps_coord_srs = 'EPSG:4326'
                survey.plots[ID].parcela_coordenadas_gps_altidud = \
                    tools_lib.import_variable(row, 'altitud', 'int', ID)
                survey.plots[ID].parcela_coordenadas_gps_altiudud_unit = 'metros'
                survey.plots[ID].relieve_relieve_ubicacion = \
                    tools_lib.import_variable(row, 'ubicación_relieve', 'code', ID,
                                              codelist=code_lists.relieve_ubicaion)
                survey.plots[ID].relieve_relieve_exposicion = \
                    tools_lib.import_variable(row, 'exposicion_relieve', 'code', ID,
                                              codelist=code_lists.relieve_exposicion)
                survey.plots[ID].relieve_relieve_pendiente = \
                    tools_lib.convert_text_to_numbers(row['pendiente'], 'mean', 'real')
                survey.plots[ID].relieve_relieve_pendiente_forma = \
                    tools_lib.import_variable(row, 'formaPendiente', 'code', ID,
                                              codelist=code_lists.relieve_pediente_forma)
                survey.plots[ID].suelo_suelo_coneat = \
                    tools_lib.import_variable(row, 'grupoConeat', 'code', ID,
                                              codelist=code_lists.suelo_suelo_coneat)
                if survey.plots[ID].suelo_suelo_coneat is None:
                    survey.plots[ID].suelo_suelo_coneat = '-'
                survey.plots[ID].suelo_suelo_uso_tierra = \
                    tools_lib.import_variable(row, 'usoTierra', 'code', ID,
                                              codelist=code_lists.suelo_suelo_uso_tierra)
                survey.plots[ID].suelo_suelo_uso_previo = \
                    tools_lib.import_variable(row, 'usoPrevio', 'code', ID,
                                              codelist=code_lists.suelo_suelo_uso_previo)
                survey.plots[ID].suelo_suelo_labranza = \
                    tools_lib.import_variable(row, 'tipoLabranza', 'code', ID,
                                              codelist=code_lists.suelo_suelo_labranza)
                survey.plots[ID].suelo_suelo_erosion_grado = \
                    tools_lib.import_variable(row, 'gradoErosion', 'code', ID,
                                              codelist=code_lists.suelo_suelo_erosion_grado)
                survey.plots[ID].suelo_suelo_erosion_tipo = \
                    tools_lib.import_variable(row, 'tipoErosion', 'code', ID,
                                              codelist=code_lists.suelo_suelo_erosion_tipo)
                survey.plots[ID].suelo_suelo_profundidad_horizonte = \
                    tools_lib.import_variable(row, 'profundidadPrimerHorizonte', 'code', ID,
                                              codelist=code_lists.suelo_suelo_profundidad_horizonte)
                survey.plots[ID].suelo_suelo_profundidad_mantillo = \
                    tools_lib.import_variable(row, 'profundidadMantillo', 'code', ID,
                                              codelist=code_lists.suelo_suelo_profundidad_humus_y_mantillo)
                survey.plots[ID].suelo_suelo_profundidad_humus = \
                    tools_lib.import_variable(row, 'profundidadHumus', 'code', ID,
                                              codelist=code_lists.suelo_suelo_profundidad_humus_y_mantillo)
                survey.plots[ID].suelo_suelo_color = \
                    tools_lib.import_variable(row, 'color', 'code', ID,
                                              codelist=code_lists.suelo_suelo_color)
                survey.plots[ID].suelo_suelo_textura = \
                    tools_lib.import_variable(row, 'textura', 'code', ID
                                              , codelist=code_lists.suelo_suelo_textura)
                survey.plots[ID].suelo_suelo_estructura = \
                    tools_lib.import_variable(row, 'estructura_suelo', 'code', ID
                                              , codelist=code_lists.suelo_suelo_estructura)
                survey.plots[ID].suelo_suelo_drenaje = \
                    tools_lib.import_variable(row, 'drenaje', 'code', ID,
                                              codelist=code_lists.suelo_suelo_drenaje)
                survey.plots[ID].suelo_suelo_infiltracion = \
                    tools_lib.import_variable(row, 'infiltracion', 'code', ID,
                                              codelist=code_lists.suelo_suelo_infiltracion)
                survey.plots[ID].suelo_suelo_impedimento = \
                    tools_lib.import_variable(row, 'impedimento', 'code', ID,
                                              codelist=code_lists.si_no)
                survey.plots[ID].suelo_suelo_olor = \
                    tools_lib.import_variable(row, 'olor', 'code', ID,
                                              codelist=code_lists.si_no)
                survey.plots[ID].suelo_suelo_humedad = \
                    tools_lib.import_variable(row, 'humedad', 'code', ID,
                                              codelist=code_lists.suelo_suelo_humedad)
                survey.plots[ID].suelo_suelo_pedregosidad = \
                    tools_lib.convert_text_to_numbers(row['pedregosidad'], 'mean', 'integer')
                survey.plots[ID].suelo_suelo_pedregosidad_unit_name = 'porciento'
                survey.plots[ID].suelo_suelo_rocosidad = \
                    tools_lib.convert_text_to_numbers(row['rocosidad'], 'mean', 'integer')
                survey.plots[ID].suelo_suelo_rocosidad_unit_name = 'porciento'
                survey.plots[ID].suelo_suelo_micorrizas = \
                    tools_lib.import_variable(row, 'micorrizas', 'code', ID,
                                              codelist=code_lists.si_no)
                survey.plots[ID].suelo_suelo_fauna = \
                    tools_lib.import_variable(row, 'faunaSuelo', 'code', ID,
                                              codelist=code_lists.si_no)
                survey.plots[ID].suelo_suelo_raices = \
                    tools_lib.import_variable(row, 'raices', 'code', ID,
                                              codelist=code_lists.suelo_suelo_raices)
                survey.plots[ID].cobertura_vegetal_cobertura_copas = \
                    tools_lib.convert_cobertura_copas(
                        tools_lib.convert_text_to_numbers(row['gradoCoberturaCopas'], 'mean', 'real'))

                survey.plots[ID].cobertura_vegetal_cobertura_sotobosque = \
                    tools_lib.convert_cobertura_copas(
                        tools_lib.convert_text_to_numbers(row['gradoSotobosque'], 'mean', 'real'))

                survey.plots[ID].cobertura_vegetal_cobertura_herbacea = \
                    tools_lib.convert_cobertura_copas(
                        tools_lib.convert_text_to_numbers(row['coberturaHerbacea'], 'mean', 'real'))

                survey.plots[ID].cobertura_vegetal_cobertura_residuos_plantas = \
                    tools_lib.convert_cobertura_residuos(
                        tools_lib.convert_text_to_numbers(row['coberturaResiduosPlantas'], 'mean', 'real'))

                survey.plots[ID].cobertura_vegetal_cobertura_residuos_cultivos = \
                    tools_lib.convert_cobertura_residuos(
                        tools_lib.convert_text_to_numbers(row['coberturaResiduosCultivos'], 'mean', 'real'))
                if row['tipoSotobosque'] == '':
                    survey.plots[ID].flora_soto_flora_soto_presencia = 2
                else:
                    survey.plots[ID].flora_soto_flora_soto_presencia = 1

                survey.plots[ID].agua_agua_caudal = \
                    tools_lib.import_variable(row, 'tipoCaudal', 'code', ID,
                                              codelist=code_lists.agua_agua_caudal)
                survey.plots[ID].agua_agua_distancia = \
                    tools_lib.convert_text_to_numbers(row['distancia_agua'], 'mean', 'integer')

                # The value 0 seems to indicate 'NoData' in this field
                if survey.plots[ID].agua_agua_distancia == '0':
                    survey.plots[ID].agua_agua_distancia = None

                if survey.plots[ID].agua_agua_distancia is not None:
                    survey.plots[ID].agua_agua_presencia = 1
                else:
                    survey.plots[ID].agua_agua_presencia = 2
                survey.plots[ID].agua_agua_distancia_unit_name = 'metros'
                # TODO clarify how to map agua_agua_nombre and 'tipo curso'
                # plotA.agua_agua_nombre = row['tipo_curso']
                survey.plots[ID].agua_agua_manejo = \
                    tools_lib.import_variable(row, 'manejo', 'code', ID,
                                              codelist=code_lists.si_no)
                survey.plots[ID].agua_agua_frec = \
                    tools_lib.import_variable(row, 'frecuencia_caudal', 'code', ID,
                                              codelist=code_lists.agua_agua_frec)
                survey.plots[ID].agua_agua_acuicultura = \
                    tools_lib.import_variable(row, 'acuacultura', 'code', ID,
                                              codelist=code_lists.si_no)
                survey.plots[ID].agua_agua_contaminacion = \
                    tools_lib.import_variable(row, 'gradoContaminacion', 'code', ID,
                                              codelist=code_lists.agua_agua_contaminacion)
                survey.plots[ID].ambiental_ambiental_potabilidad = \
                    tools_lib.import_variable(row, 'pobreCalidadAgua', 'code', ID,
                                              codelist=code_lists.si_no)
                survey.plots[ID].ambiental_ambiental_polucion = \
                    tools_lib.import_variable(row, 'polucionAire', 'code', ID,
                                              codelist=code_lists.si_no)
                survey.plots[ID].ambiental_ambiental_fertalidad = \
                    tools_lib.import_variable(row, 'perdidaFertilidad', 'code', ID,
                                              codelist=code_lists.si_no)
                survey.plots[ID].ambiental_ambiental_invasion = \
                    tools_lib.import_variable(row, 'invasionEspecies', 'code', ID,
                                              codelist=code_lists.si_no)
                survey.plots[ID].ambiental_ambiental_pesticida = \
                    tools_lib.import_variable(row, 'presenciaPesticidas', 'code', ID,
                                              codelist=code_lists.si_no)
                survey.plots[ID].fuego_fuego_evidencia = \
                    tools_lib.import_variable(row, 'evidenciaFuego', 'code', ID,
                                              codelist=code_lists.fuego_fuego_evidencias)
                survey.plots[ID].fuego_fuego_tipo = \
                    tools_lib.import_variable(row, 'tipoFuego', 'code', ID,
                                              codelist=code_lists.fuego_fuego_tipo)
                survey.plots[ID].fuego_fuego_proposito = \
                    tools_lib.import_variable(row, 'propositoFuego', 'code', ID,
                                              codelist=code_lists.fuego_fuego_proposito)

                # For plantationes set the species code
                if survey.plots[ID].general_datos_parcela_bosque_tipo == 2:
                    survey.plots[ID].genero = row['genero'].strip()
                    especies = row['especie_plantacion'].strip()
                    plant_especies = survey.plots[ID].genero + ' ' + especies
                    index = tools_lib.find_species_scientific(species_list, plant_especies)
                    try:
                        if index.__len__() > 0:
                            survey.plots[ID].plantacion_plant_especie_code = \
                                species_list[index[0]].species_code
                            survey.plots[ID].plantacion_plant_especie_scientific_name = \
                                species_list[index[0]].scientific_name
                            survey.plots[ID].plantacion_plant_especie_vernacular_name = \
                                species_list[index[0]].common_name
                        else:
                            error_msg = "Could not find the species \"{species}\" in the tree species code list" \
                                        "for plot {plotid}".format(species=plant_especies, plotid=ID)
                            logging.error(error_msg)
                    except ValueError:
                        error_msg = "Could not find the species \"{species}\" in the tree species code list" \
                                    "for plot{plotid}".format(species=plant_especies, plotid=ID)
                        logging.error(error_msg)

                if row.has_key('edad') and row['edad'] not in ['', ' ']:
                    try:
                        edad_nr = tools_lib.convert_text_to_numbers(row['edad'], 'max', 'real')
                        if edad_nr is not None:
                            edad = tools_lib.convert_plantacion_edad(float(edad_nr))
                            survey.plots[ID].plantacion_plant_edad = edad
                        else:
                            error_msg = "Could not convert the variable \"rango_edad\" with value: \"{value}\" to edad" \
                                        "class for plot{plotid}".format(value=edad_nr, plotid=ID)
                            logging.error(error_msg)

                    except ValueError:
                        error_msg = "Could not convert the variable \"rango_edad\" with value: \"{value}\" to a" \
                                    "number for plot: {plotid}".format(value=row['edad'], plotid=ID)
                        logging.error(error_msg)

                survey.plots[ID].plantacion_plant_raleo = \
                    tools_lib.import_variable(row, 'raleo', 'code', ID,
                                              codelist=code_lists.plantacion_raleo)
                survey.plots[ID].plantacion_plant_poda = \
                    tools_lib.import_variable(row, 'tienePoda', 'code', ID,
                                              codelist=code_lists.si_no)
                survey.plots[ID].plantacion_plant_poda_altura = \
                    tools_lib.import_variable(row, 'alturaPoda', 'float', ID)
                survey.plots[ID].plantacion_plant_poda_altura_unit_name = 'metros'
                survey.plots[ID].plantacion_plant_regular = \
                    tools_lib.import_variable(row,'parcelaRegular','code',ID,code_lists.si_no)
                survey.plots[ID].plantacion_plant_dist_fila = \
                    tools_lib.convert_text_to_numbers(row['distanciaFila'], 'mean', 'real')
                survey.plots[ID].plantacion_plant_dist_fila_unit_name = 'metros'
                survey.plots[ID].plantacion_plant_dist_entrefila = \
                    tools_lib.convert_text_to_numbers(row['distanciaEntreFila'], 'mean', 'real')
                survey.plots[ID].plantacion_plant_dist_entrefila_unit_name = 'metros'
                survey.plots[ID].plantacion_plant_dist_silvopast_unit_name = 'metros'
                survey.plots[ID].plantacion_plant_adaptacion = \
                    tools_lib.import_variable(row, 'adaptacionEspecie', 'code', ID,
                                              codelist=code_lists.plantacion_adaptation)
                survey.plots[ID].plantacion_plant_regimen = \
                    tools_lib.import_variable(row, 'regimen', 'code', ID,
                                              codelist=code_lists.plantacion_regimen)
                survey.plots[ID].plantacion_plant_estado = \
                    tools_lib.import_variable(row, 'estadoGeneral', 'code', ID,
                                              codelist=code_lists.plantacion_estado)
                survey.plots[ID].forestacion_forest_origen = \
                    tools_lib.import_variable(row, 'origenPlantacion', 'code', ID,
                                              codelist=code_lists.forestacion_forest_origen)
                survey.plots[ID].forestacion_forest_estructura = \
                    tools_lib.import_variable(row, 'estructura_forestacion', 'code', ID
                                              , codelist=code_lists.forestacion_forest_estructura)
                survey.plots[ID].forestacion_forest_propiedad = \
                    tools_lib.import_variable(row, 'propiedadTierra', 'code', ID,
                                              codelist=code_lists.forestacion_forest_propiedad)
                survey.plots[ID].forestacion_forest_plan_manejo = \
                    tools_lib.import_variable(row, 'planManejo', 'code', ID,
                                              codelist=code_lists.si_no)
                survey.plots[ID].forestacion_forest_intervencion = \
                    tools_lib.import_variable(row, 'gradoIntervencion', 'code', ID,
                                              codelist=code_lists.human_intervention_degree)
                survey.plots[ID].forestacion_forest_madera_destino_1 = \
                    tools_lib.import_variable(row, 'destinoMadera', 'code', ID,
                                              codelist=code_lists.forestacion_forest_madera_destino)
                survey.plots[ID].forestacion_forest_silvicultura = \
                    tools_lib.import_variable(row, 'maFalTrueeejoTrueilvicultural', 'code', ID,
                                              codelist=code_lists.si_no)
                survey.plots[ID].forestacion_forest_tecnologia = \
                    tools_lib.import_variable(row, 'tecnologiaExplotacion', 'code', ID,
                                              codelist=code_lists.forestacion_forest_tecnologia)

                tmp = tools_lib.convert_ntfp_gando_tipo(row['tipoGanado'])
                if tmp.__len__() == 1:
                    survey.plots[ID].ntfp_ntfp_ganado_tipo_1 = \
                        tools_lib.find_key(code_lists.ntfp_ntfp_ganado_tipo, tmp[0])
                if tmp.__len__() == 2:
                    survey.plots[ID].ntfp_ntfp_ganado_tipo_1 = \
                        tools_lib.find_key(code_lists.ntfp_ntfp_ganado_tipo, tmp[0])
                    survey.plots[ID].ntfp_ntfp_ganado_tipo_2 = \
                        tools_lib.find_key(code_lists.ntfp_ntfp_ganado_tipo, tmp[1])
                if tmp.__len__() == 3:
                    survey.plots[ID].ntfp_ntfp_ganado_tipo_1 = \
                        tools_lib.find_key(code_lists.ntfp_ntfp_ganado_tipo, tmp[0])
                    survey.plots[ID].ntfp_ntfp_ganado_tipo_2 = \
                        tools_lib.find_key(code_lists.ntfp_ntfp_ganado_tipo, tmp[1])
                    survey.plots[ID].ntfp_ntfp_ganado_tipo_3 = \
                        tools_lib.find_key(code_lists.ntfp_ntfp_ganado_tipo, tmp[2])
                if tmp.__len__() == 4:
                    survey.plots[ID].ntfp_ntfp_ganado_tipo_1 = \
                        tools_lib.find_key(code_lists.ntfp_ntfp_ganado_tipo, tmp[0])
                    survey.plots[ID].ntfp_ntfp_ganado_tipo_2 = \
                        tools_lib.find_key(code_lists.ntfp_ntfp_ganado_tipo, tmp[1])
                    survey.plots[ID].ntfp_ntfp_ganado_tipo_3 = \
                        tools_lib.find_key(code_lists.ntfp_ntfp_ganado_tipo, tmp[2])
                    survey.plots[ID].ntfp_ntfp_ganado_tipo_4 = \
                        tools_lib.find_key(code_lists.ntfp_ntfp_ganado_tipo, tmp[3])
                if tmp.__len__() == 5:
                    survey.plots[ID].ntfp_ntfp_ganado_tipo_1 = \
                        tools_lib.find_key(code_lists.ntfp_ntfp_ganado_tipo, tmp[0])
                    survey.plots[ID].ntfp_ntfp_ganado_tipo_2 = \
                        tools_lib.find_key(code_lists.ntfp_ntfp_ganado_tipo, tmp[1])
                    survey.plots[ID].ntfp_ntfp_ganado_tipo_3 = \
                        tools_lib.find_key(code_lists.ntfp_ntfp_ganado_tipo, tmp[2])
                    survey.plots[ID].ntfp_ntfp_ganado_tipo_4 = \
                        tools_lib.find_key(code_lists.ntfp_ntfp_ganado_tipo, tmp[3])
                    survey.plots[ID].ntfp_ntfp_ganado_tipo_5 = \
                        tools_lib.find_key(code_lists.ntfp_ntfp_ganado_tipo, tmp[4])

                survey.plots[ID].ntfp_ntfp_pastoreo_intens = \
                    tools_lib.import_variable(row, 'intensidadPastoreo', 'code', ID,
                                              codelist=code_lists.ntfp_ntfp_pastoreo_intens)
                survey.plots[ID].ntfp_ntfp_prod_cultivo = \
                    tools_lib.import_variable(row, 'sistemasProduccion', 'code', ID,
                                              codelist=code_lists.ntfp_ntfp_prod_cultivo)
                survey.plots[ID].ntfp_ntfp_prod_apicola = \
                    tools_lib.import_variable(row, 'produccionApicola', 'code', ID, codelist=code_lists.si_no)
                survey.plots[ID].ntfp_ntfp_sombra = \
                    tools_lib.import_variable(row, 'sombra', 'code', ID,
                                              codelist=code_lists.si_no)
                survey.plots[ID].ntfp_ntfp_caza_pesca = \
                    tools_lib.import_variable(row, 'actividadesCasaPesca', 'code', ID,
                                              codelist=code_lists.si_no)
                survey.plots[ID].ntfp_ntfp_rompe_vientos = \
                    tools_lib.import_variable(row, 'rompeVientos', 'code', ID,
                                              codelist=code_lists.si_no)
                survey.plots[ID].ntfp_ntfp_recreacion = \
                    tools_lib.import_variable(row, 'actividadesRecreacion', 'code', ID,
                                              codelist=code_lists.si_no)
                survey.plots[ID].ntfp_ntfp_hongos = \
                    tools_lib.import_variable(row, 'recoleccionHongos', 'code', ID,
                                              codelist=code_lists.si_no)
                survey.plots[ID].ntfp_ntfp_semillas = \
                    tools_lib.import_variable(row, 'obtencionSemillas', 'code', ID,
                                              codelist=code_lists.si_no)
                survey.plots[ID].ntfp_ntfp_cientificos = \
                    tools_lib.import_variable(row, 'estudiosCientificos', 'code', ID,
                                              codelist=code_lists.si_no)
                survey.plots[ID].ntfp_ntfp_aceites = \
                    tools_lib.import_variable(row, 'aceitesEsenciales', 'code', ID,
                                              codelist=code_lists.si_no)
                survey.plots[ID].ntfp_ntfp_carbono = \
                    tools_lib.import_variable(row, 'fijacionCarbono', 'code', ID,
                                              codelist=code_lists.si_no)
                survey.plots[ID].san_rumbo_unit_name = 'grados'

    info_msg = "Updated the plot information for {nplots} plots from the file: {file}" \
        .format(nplots=plot_counter.__len__(), file=os.path.basename(infile))
    logging.info(info_msg)
    print(info_msg)