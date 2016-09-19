#!/usr/bin/env python
# -*- coding: utf-8 -*-s

bosque_tipo = {
    1: ['bosque nativo'],
    2: ['plantacion', 'plantación']
}

# dictionary of sub forest types
subbosque_tipo = {
    11: ['Galería','galería','galeria'],
    12: ['Serrano','serrano'],
    13: ['Parque', 'parque'],
    14: ['Quebrada','quebrada'],
    15: ['Palmar','palmar'],
    21: ['Plantación','plantación','plantacion'],
    22: ['Costero','costero']
}

accesibilidad = {
    1: ['fácil', 'facil'],
    2: ['medio', 'medio', 'media'],
    3: ['difícil', 'dificil', 'muy difícil', 'muy difíci'],
}

departamento = {
    1: ['montevideo'],
    2: ['artigas'],
    3: ['canelones'],
    4: ['cerro largo'],
    5: ['colonia'],
    6: ['durazno', 'duranzno'],
    7: ['flores'],
    8: ['florida'],
    9: ['lavalleja'],
    10: ['maldonado'],
    11: ['paysandú', 'paysandu', 'paysand\xc3\x9a'],
    12: ['río negro', 'rio', 'rio negro'],
    13: ['rivera'],
    14: ['rocha'],
    15: ['salto'],
    16: ['san josé', 'san jose'],
    17: ['soriano'],
    18: ['tacuarembó', 'tacuarembo'],
    19: ['treinta y tres']
}

foto_tipo = {
    1: ['carretera a cno. vecinal','carretera a camino vecinal'],
    2: ['cno. vecinal a cno. de acceso','camino vecinal a camino de acceso'],
    3: ['cno. de acceso a punto de gps','camino de acceso a punto gps'],
    4: ['punto de gps a centro de la parcela','punto gps a centro de parcela'],
    5: ['rumbo cno. a centro de la parcela',''],
    6: ['relieve'],
    7: ['fotos de parcela','fotos parcela'],
    8: ['otros','otras'],
}

estado_1 = {
    1: ["con información relevada"],
    2: ["ausencia de Bosque"],
    3: ["bosque cortado"],
    4: ["inaccesible"],
}


estado_2 = {
    1: ['bosque nativo'],
    2: ['planatación']
}


estado_3 = {
    1: ["Con rebrote (DAP < 3cm)"],
    2: ["plantación reciente (dab < 3cm)"],
    3: ["replantación  (dab < 3cm)"],
    4: ["cosecha reciente"]
}

relieve_ubicaion = {
    1: ["plano"],
    2: ["ladera media"],
    3: ["ladera baja"],
    4: ["ladera alta"],
    5: ["cumbre"]
}

relieve_exposicion = {
    1: ["ninguna","plano","plana"],
    2: ["este"],
    3: ["oeste"],
    4: ["sur"],
    5: ["norte"],
    6: ["noreste"],
    7: ["noroeste"],
    8: ["sureste"],
    9: ["suroeste"]
}

relieve_pediente_forma = {
    1: ["cóncava", "concava"],
    2: ["convexa"],
    3: ["lineal"]
}

suelo_suelo_coneat = {
    '-': ["No se define"],
    2: ["1.10a"],
    3: ["1.10b"],
    4: ["1.11a"],
    5: ["1.11b"],
    6: ["1.12"],
    7: ["1.20"],
    8: ["1.21"],
    9: ["1.22"],
    10: ["1.23"],
    11: ["1.24"],
    12: ["1.25"],
    13: ["2.10"],
    14: ["2.11a"],
    15: ["2.11b"],
    16: ["2.12"],
    17: ["2.13"],
    18: ["2.14"],
    19: ["2.20"],
    20: ["2.21"],
    21: ["2.22"],
    22: ["3.10"],
    23: ["3.11"],
    24: ["3.12"],
    25: ["3.13"],
    26: ["3.14"],
    27: ["3.15"],
    28: ["3.2"],
    29: ["3.30"],
    30: ["3.31"],
    31: ["3.40"],
    32: ["3.41"],
    33: ["3.50"],
    34: ["3.51"],
    35: ["3.52"],
    36: ["3.53"],
    37: ["3.54"],
    38: ["03.10"],
    39: ["03.11"],
    40: ["03.2"],
    41: ["03.3"],
    42: ["03.40"],
    43: ["03.41"],
    44: ["03.51"],
    45: ["03.52"],
    46: ["03.6"],
    47: ["b03.1"],
    48: ["g03.10"],
    49: ["g03.11"],
    50: ["g03.21"],
    51: ["g03.22"],
    52: ["g03.3"],
    53: ["4.1"],
    54: ["4.2"],
    55: ["5.01a"],
    56: ["5.01b"],
    57: ["5.01c"],
    58: ["5.02a"],
    59: ["5.02b"],
    60: ["5.3"],
    61: ["5.4"],
    62: ["5.5"],
    63: ["6.1/1"],
    64: ["6.1/2"],
    65: ["6.1/3"],
    66: ["6.2"],
    67: ["6.3"],
    68: ["6.4"],
    69: ["6.5"],
    70: ["6.6"],
    71: ["6.7"],
    72: ["6.8"],
    73: ["6.9"],
    74: ["6.10a"],
    75: ["6.10b"],
    76: ["6.11"],
    77: ["6.12"],
    78: ["6.13"],
    79: ["6.14"],
    80: ["6.15"],
    81: ["6.16"],
    82: ["6.17"],
    83: ["7.1"],
    84: ["7.2"],
    85: ["7.31"],
    86: ["7.32"],
    87: ["7.33"],
    88: ["7.41"],
    89: ["7.42"],
    90: ["07.1"],
    91: ["07.2"],
    92: ["8.1"],
    93: ["8.02a"],
    94: ["8.02b"],
    95: ["8.3"],
    96: ["8.4"],
    97: ["8.5"],
    98: ["8.6"],
    99: ["8.7"],
    100: ["8.8"],
    101: ["8.9"],
    102: ["8.10"],
    103: ["8.11"],
    104: ["8.12"],
    105: ["8.13"],
    106: ["8.14"],
    107: ["8.15"],
    108: ["8.16"],
    109: ["9.1"],
    110: ["9.2"],
    111: ["9.3"],
    112: ["9.41"],
    113: ["9.42"],
    114: ["9.5"],
    115: ["9.6"],
    116: ["9.7"],
    117: ["9.8"],
    118: ["9.9"],
    119: ["09.1"],
    120: ["09.2"],
    121: ["09.3"],
    122: ["09.4"],
    123: ["09.5"],
    124: ["s09.10"],
    125: ["s09.11"],
    126: ["s09.20"],
    127: ["s09.21"],
    128: ["s09.22"],
    129: ["10.1"],
    130: ["10.2"],
    131: ["10.3"],
    132: ["10.4"],
    133: ["10.5"],
    134: ["10.6a"],
    135: ["10.6b"],
    136: ["10.7"],
    137: ["10.8a"],
    138: ["10.8b"],
    139: ["10.9"],
    140: ["10.10"],
    141: ["10.11"],
    142: ["10.12"],
    143: ["10.13"],
    144: ["10.14"],
    145: ["10.15"],
    146: ["10.16"],
    147: ["d10.1"],
    148: ["d10.2"],
    149: ["d10.3"],
    150: ["g10.1"],
    151: ["g10.2"],
    152: ["g10.3"],
    153: ["g10.4"],
    154: ["g10.5"],
    155: ["g10.6a"],
    156: ["g10.6b"],
    157: ["g10.7"],
    158: ["g10.8"],
    159: ["g10.9"],
    160: ["g10.10"],
    161: ["s10.10"],
    162: ["s10.11"],
    163: ["s10.12"],
    164: ["s10.13"],
    165: ["s10.20"],
    166: ["s10.21"],
    167: ["11.1"],
    168: ["11.2"],
    169: ["11.3"],
    170: ["11.4"],
    171: ["11.5"],
    172: ["11.6"],
    173: ["11.7"],
    174: ["11.8"],
    175: ["11.9"],
    176: ["11.10"],
    177: ["12.10"],
    178: ["12.11"],
    179: ["12.12"],
    180: ["12.13"],
    181: ["12.20"],
    182: ["12.21"],
    183: ["12.22"],
    184: ["13.1"],
    185: ["13.2"],
    186: ["13.31"],
    187: ["13.32"],
    188: ["13.4"],
    189: ["13.5"]
}

suelo_suelo_uso_tierra = {
    1: ["forestal"],
    2: ["agrícola", "agricola", "agrico,canad.", "agricola,gana", "agricola,ganade", "agricola-gana", "agricolaganad",
        "agricola-ganade","ganadero agricola"],
    3: ["ganadero"],
    4: ["agro forestal", "agroforestal", "fores-ganade", "forest-ganade", "foresta-ganad", "forest-ganad",
        "forestal-agrico", "forestal-gana", "forestal-ganade"]
}

suelo_suelo_uso_previo = {
    1: ["pradera"],
    2: ["forestal", "monte"],
    3: ["otros","otro"]
}
suelo_suelo_labranza = {
    1: ["en línea","en línea" "en lineas", "laborea en lineas", "laboreo en lineas"],
    2: ["curvas de nivel", "curvas de nivel-en lineas"],
    3: ["espina de pescado", "espina"],
    4: ["otras", "surco"],
    5: ["pozo"],
    6: ["no aplica", "no", "no hay","none"]
}

suelo_suelo_erosion_grado = {
    1: ["nula", "no hay", "no aplica"],
    2: ["ligera"],
    3: ["moderada"],
    4: ["severa"],
    5: ["extrema"]
}

suelo_suelo_erosion_tipo = {
    1: ["laminar"],
    2: ["cárcava", "carcava"],
    3: ["zanja"],
    4: ["surco"],
    5: ["nulo","nula"],
}

suelo_suelo_profundidad_horizonte = {
    1: ["profundo"],
    2: ["superficial"],
    3: ["semi profundo"],
}

suelo_suelo_profundidad_humus_y_mantillo = {
    1: ["profundo"],
    2: ["superficial"],
    '-': ["no se define"]
}

suelo_suelo_color = {
    1: ["pardo oscuro", "pardo o", "pardo oscuro-negro", "pardo rojizo"],
    2: ["pardo claro"],
    3: ["pardo grisáceo", "pardo grisaceo"],
    4: ["rojizo"],
    5: ["negro", "negro-pardo oscuro"],
    6: ["marrón", "marron", "marrón claro", "marron claro"],
    7: ["otro", "ocre"]
}

suelo_suelo_textura = {
    1: ["arenoso", "arenoso -", ],
    2: ["franco"],
    3: ["arcilloso", "arcillo-ar", "arcilloso-"],
    4: ["franco-arcilloso", "fran.-arc."],
    5: ["franco-arenoso", "arenoso fr", "arenoso/fr", "arenoso-fr", "fran.-aren", "franco arc", "franco are"],
    6: ["limoso"]
}

suelo_suelo_estructura = {
    1: ["sin estructura"],
    2: ["laminar"],
    3: ["prismática", "prismatica"],
    4: ["en bloques"],
    5: ["granular"]
}

suelo_suelo_drenaje = {
    1: ["bueno", "buen"],
    2: ["regular"],
    3: ["malo"]
}

suelo_suelo_infiltracion = {
    1: ["permeable"],
    2: ["impermeable"],
    3: ["moderado"],
}

si_no = {
    1: ["si", "s","TRUE","true"],
    2: ["no", "n","FALSE","false"]
}

suelo_suelo_humedad = {
    1: ["húmedo", "humedo"],
    2: ["seco", ]
}

suelo_suelo_raices = {
    1: ["presencia"],
    2: ["ausencia"]
}

cobertura_grado = {
    1: ['0'],
    2: ['0-5'],
    3: ['5-10'],
    4: ['10-40'],
    5: ['40-70'],
    6: ['>70']
}

cobertura_grado_residos = {
    1: ['0'],
    2: ['0-5'],
    3: ['5-10'],
    4: ['10-20'],
    5: ['20-30'],
    6: ['30-50'],
    7: ['50-70'],
    8: ['>70']
}


agua_agua_caudal = {
    1: ["río", "rio"],
    2: ["arroyo", "arroyo- lago", "arrojo-tajamar"],
    3: ["cañada", "canada"],
    4: ["embalse"],
    5: ["canal de riego"],
    6: ["represa"],
    7: ["tajamar"],
    8: ["lago"],
    9: ["océano", "oceano", "mar"]
}

agua_agua_frec = {
    1: ["permanente"],
    2: ["temporal"]
}

agua_agua_contaminacion = {
    1: ["alto"],
    2: ["medio"],
    3: ["bajo"],
    4: ["nulo", "nula"]
}

fuego_fuego_evidencias = {
    1: ["sin evidencias"],
    2: ["fuego reciente", "reciente"],
    3: ["fuego antiguo", "antiguo"]
}

fuego_fuego_tipo = {
    1: ["fuego subterráneo"],
    2: ["fuego de superficie", "superficie"],
    3: ["fuego de copas", "copas"]
}

fuego_fuego_proposito = {
    1: ["no aplicable"],
    2: ["limpieza de una nueva tierra", "limpieza nueva tierra"],
    3: ["limpieza de maleza y residuos", "limpieza de maleza"],
    4: ["regeneración de pasturas"],
    5: ["control de plagas"],
    6: ["incendio provocado"],
    7: ["incendio accidental"],
    8: ["incendio natural"]
}

plantacion_raleo = {
    1: ["ninguno"],
    2: ["sistemático", 'sis', 'sis-se'],
    3: ["sanitario", 'san'],
    4: ["selectivo por alto", 'sel: a'],
    5: ["selectivo por bajo", 'sel: b']
}

plantacion_adaptation = {
    1: ["adaptado", "a"],
    2: ["no adaptado", "na"],
}

plantacion_regimen = {
    1: ["fustal", 'f'],
    2: ["tallar", 't']
}

plantacion_estado = {
    1: ["bueno"],
    2: ["regular"],
    3: ["malo"]
}

forestacion_forest_origen = {
    1: ["plantado", 'implantada','implantado'],
    2: ["regeneración natural", 'natural']
}

forestacion_forest_estructura = {
    1: ["fustal"],
    2: ["tallar"],
    3: ["mixto"]
}

forestacion_forest_propiedad = {
    1: ["particular"],
    2: ["estado"]
}

human_intervention_degree = {
    1: ["alto"],
    2: ["medio"],
    3: ["bajo"],
    4: ["ninguno"]
}

forestacion_forest_madera_destino = {
    1: ["ninguno"],
    2: ["aserrado"],
    3: ["pulpa", "pulpa y", "pulpa-as", "pulpa-co", "pulpa-le"],
    4: ["leña","energia","energía"],
    5: ["columnas"],
    6: ["carbón"],
    7: ["postes / piques / uso del establecimiento"]
}

forestacion_forest_tecnologia = {
    1: ["ninguna", "ninguno", "nignuno"],
    2: ["manual"],
    3: ["mecanizado"],
    4: ["semimecanizado", "semi mecanizado"]
}

ntfp_ntfp_ganado_tipo = {
    1: ["vacuno", "vac", "vacas", "vacu", "vacun"],
    2: ["equino", "equi", "eq", "equ", "e", "equin"],
    3: ["ovino", "ovi", "ov", "o", "ovinos", "ove"],
    4: ["porcino"],
    5: ["otros", "sd", "ca", "cab", "sui"],
    6: ["ausencia"]
}

ntfp_ntfp_pastoreo_intens = {
    1: ["no evidente"],
    2: ["ligera"],
    3: ["moderada"],
    4: ["severa"]
}

ntfp_ntfp_prod_cultivo = {
    1: ["silvopastoreo","pastoreo en bosques"],
    2: ["forrajera"],
    3: ["hortícola", "horticola"],
    4: ["frutícola"],
    5: ["otro", "ganadero", "ganadera","otros"],
    '-': ['sin datos','no se define']
}

plantacion_plant_especie = {
    'PL1004': ['eucalyptus botryoides', 'e1'],
    'PL1005': ['eucalyptus camaldulensis', 'e2'],
    'PL1006': ['eucalyptus corinocalix', 'e3'],
    'PL1007': ['eucalyptus bicostata', 'e4'],
    'PL1008': ['eucalyptus diversicolor', 'e5'],
    'PL1009': ['eucalyptus globulus subsp. globulus','eucalyptus globulus ssp. globulus' 'e6'],
    'PL1010': ['eucalyptus gomphocephala', 'e7'],
    'PL1011': ['eucalyptus grandis', 'e8'],
    'PL1012': ['eucalyptus hempholia', 'e10'],
    'PL1013': ['eucalyptus leucoxylon', 'e11'],
    'PL1014': ['eucalyptus marcarthuri', 'e12'],
    'PL1015': ['eucalyptus melliodora', 'e13'],
    'PL1016': ['eucalyptus paniculata', 'e14'],
    'PL1017': ['eucalyptus punctata', 'e15'],
    'PL1018': ['eucalyptus resinifera', 'e16'],
    'PL1019': ['eucalyptus robusta', 'e17'],
    'PL1020': ['eucalyptus rudis', 'e18'],
    'PL1021': ['eucalyptus saligna', 'e19'],
    'PL1022': ['eucalyptus smithii', 'e20'],
    'PL1023': ['eucalyptus sideroxylon', 'e21'],
    'PL1024': ['eucalyptus tereticornis', 'e22'],
    'PL1025': ['eucalyptus viminalis', 'e23'],
    'PL1026': ['eucalyptus globulus subsp. maidenii','eucalyptus globulus+maidenii', 'e24','e31'],
    'PL1027': ['eucalyptus cinerea', 'e25'],
    'PL1028': ['eucalyptus grandis+maidenii', 'e26'],
    'PL1029': ['eucalyptus bosistoana', 'e27'],
    'PL1030': ['eucalyptus dunnii', 'e28'],
    'PL1031': ['eucalyptus grandis+saligna', 'e29'],
    'PL1033': ['eucalyptus crebra', 'e32'],
    'PL1034': ['eucalyptus nitens', 'e33'],
    'PL1035': ['eucalyptus benthamii'],
    'PL1037': ['acacia longifolia', 'o3'],
    'PL1038': ['platanus sp.', 'o16'],
    'PL1039': ['fraxinus sp.', 'o19'],
    'PL1040': ['taxodium distinchum', 'o20'],
    'PL1041': ['quercus sp.', 'o21'],
    'PL1043': ['pinus canariensis', 'p1'],
    'PL1044': ['pinus elliottii', 'p2'],
    'PL1045': ['pinus patula', 'p3'],
    'PL1046': ['pinus pinaster', 'p4'],
    'PL1047': ['pinus radiata', 'p5'],
    'PL1048': ['pinus taeda', 'p6'],
    'PL1049': ['pinus elliottii+taeda', 'p7'],
    'PL1050': ['pinus elliottii+pinaster', 'p8'],
    'PL1051': ['pinus roxbughii', 'p10'],
    'PL1053': ['populus deltoides', 's1'],
    'PL1054': ['populus xa euroamericana', 's2'],
    'PL1055': ['populus xb euroamericana', 's3'],
    'PL1056': ['populus xc euroamericana', 's4'],
    'PL1057': ['populus xd euroamericana', 's7'],
    'PL1058': ['salix alba var. coerulea', 's5'],
    'PL1060': ['salix babylonica', 's8']
}

flora_suelo_tipo = {
    1: ["leñoso","lenoso"],
    2: ["no leñoso","no lenoso"]
}

flora_suelo_freq = {

    1: ['poco abundante'],
    2: ['medio abundante'],
    3: ['muy abundante']

}

arbol_estrato ={
    1:  ['inferior'],
    2:  ['intermedio'],
    3:  ['superior'],
    4:  ['emergente'],
    '-': ['no se define','a','b','m']
}

arbol_rango_edad = {
    1: ["0-25"],
    2: ["25-50"],
    3: [">50"],
    '-': ['no se define']
}

arbol_forma ={
    1: ["recto"],
    2: ["inclinado"],
    3: ["curvado"],
    4: ["torcido"],
    5: ["bifurcado"],
    6: ["multifustal"],
    '-': ["no se define"]
}

invasora_categoria = {
    1: ["especies leñosas invasivas",'leñosa'],
    2: ["especies herbáceas invasivas","herbácea"]
}

invasora_severidad = {
    1: ["ligera"],
    2: ["moderada"],
    3: ["seria",],
    4: ["extrema"]
}

equipo_cargo = {
    1: ["jefe de equipo","jefe del campo"],
    2: ["experto fauna",'responsable de fauna','responsable del área de fauna'],
    3: ["experto forestal"],
    4: ["experto suelo"],
    5: ["otro",'coordinador general','encargado de campo','operario de campo','responsable de flora','responsable del área de flora','responsable técnico del trabajo']
}

sanidad_categoria = {
    1: ["dominante"],
    2: ["codominante o medio"],
    3: ["dominado o suprimido"],
    4: ["decadente"],
    5: ["muerto"]
}
