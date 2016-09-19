#!/usr/bin/env python
# -*- coding: utf-8 -*-s

import csv
import logging
import subprocess
from model import class_lib


def find_key(dic, val):
    """return the key of dictionary dic given the value"""
    outvalue = None
    for k, v in dic.iteritems():
        if str.lower(val) in v:
            outvalue = k
            break
    if outvalue:
        return outvalue
    else:
        return

def find_value(dic, key):
    """return the value of dictionary dic given the key"""
    return dic[key]

def convert_text_to_numbers(string, stat, type):
    """
    converts the string expresion  into a numeric variable by calculating the mean values of expression X-X
    """
    # check if this is an empty string
    if string is '':
        out = None
    elif string in ['N', "2'0", 'otoño 2009', 'Otoño 2009','No se define']:
        warn_msg ='The following non-interpretable string found was found when converting text to number:{}'.format(string)
        logging.warn(warn_msg)
        out = None
    else:
        # replace comma with dot
        string = str.replace(string, ',', '.')
        # remove > and <
        string = str.replace(string, '>', '')
        string = str.replace(string, '<', '')
        string = str.replace(string, '(regeneracion)', '')
        string = str.replace(string, ' años', '')
        string = str.replace(string, '(a)', '')
        # split string with '-'
        tmp = str.split(string, '-')
        # remove white spaces
        tmp1 = []
        for i in tmp:
            tmp1.append(str.strip(i))
        # remove empty elements from list
        if tmp1.__len__() > 2:
            tmp1.remove('')
        if tmp1.__len__() == 1:
            try:
                out = float(tmp1[0])
            except:
                warn_msg = 'The following string could not be converted to a number:{}'.format(tmp1[0])
                logging.warn(warn_msg)
                return

        else:
            tmp2 = []
            for i in tmp1:
                try:
                    num = float(i)
                    tmp2.append(num)
                except:
                    warn_msg ='The following string could not be converted to a number:{}'.format(i)
                    logging.warn(warn_msg)
                    return
            if stat == 'mean':
                out = sum(tmp2)/float(len(tmp2))
            if stat == 'max':
                out = max(tmp2)
        if type == 'real':
            out = '{:.2f}'.format(out)
        if type == 'integer':
            out = '{:.0f}'.format(out)
    return out

def convert_cobertura_copas(percent):
    """
    Converts the numeric value into a class
    """
    if percent is None:
        return None
    else:

        try:
            percent = float(percent)
        except ValueError:
            print "Cannot conver the variable {} to a number"

        if percent == '':
          out = None
        if percent == 0:
            out = 1
        elif percent <= 5:
            out = 2
        elif percent <= 10:
            out = 3
        elif percent <= 40:
            out = 4
        elif percent <= 70:
            out = 5
        else:
            out = 6
    return out

def convert_cobertura_residuos(percent):
    """
    Converts the numeric value into a class
    """
    if percent == '':
        out = None
    if percent == 0:
        out = 1
    elif percent < 5:
        out = 2
    elif percent < 10:
        out = 3
    elif percent < 20:
        out = 4
    elif percent < 30:
        out = 5
    elif percent < 50:
        out = 6
    elif percent < 70:
        out = 7
    else:
        out = 8
    return out

def find_species(dic, val):
    """return the species_id based on the alternative spellings"""
    outlist = []
    for k, v in dic.iteritems():
        if str.lower(val) in str.lower(v.alternative):
            outlist.append(k)
    return outlist

def find_species_scientific(dic, val):
    """return the species_id based on the scientific name"""
    outlist = []
    val = val.replace('ssp.','subsp.')
    val = val.strip()
    for k, v in dic.iteritems():
        if str.lower(val) == str.lower(v.scientific_name):
            outlist.append(k)
    return outlist

def find_species_code(dic, val):
    """return the species_id based on the species code"""
    outvalue = []
    for k, v in dic.iteritems():
        if val in v.species_code:
            outvalue = k
            break
    return outvalue

def find_species_common(dic, val):
    """return the species_id based on the common name"""
    outvalue = []
    for k, v in dic.iteritems():
        if val in v.common_name:
            outvalue = k
            break
    return outvalue

def convert_plantacion_edad(edad):
    """
    Converts the numeric value into a class
    """
    if edad == '':
        out = None
    elif edad <= 5.0:
        out = 1
    elif edad <= 10.0:
        out = 2
    elif edad <= 15.0:
        out = 3
    elif edad <= 20.0:
        out = 4
    else:
        out = 5
    return out

def convert_ntfp_gando_tipo(tipo):
    out = []
    tmp = str.replace(tipo, '.', '')
    tmp = str.replace(tipo, 'y', ',')
    tmp = str.replace(tipo, '-', ',')
    out = str.split(tmp, ',')
    return out

def fix_coordinate_notation(coord):
    """
    Fixes different spellings of the coordinates
    """
    degrees = None
    seconds = None
    minutes = None
    # Remove heading 0 from degrees

    tmp = str.lstrip(coord, '0')
    # Remove trainling seconds
    tmp = str.rstrip(tmp, "\xc2\xb4")
    tmp = str.rstrip(tmp, "'")
    tmp = str.rstrip(tmp, "`")
    degrees = tmp[0:2]
    # 1.Variante 34°22.123
    print 'Temp: {}'.format(tmp)
    if str.find(tmp, '\xc2') == 2 and str.find(tmp, '.') == 6:
        print "V1"
        minutes = tmp[4:6]
    # 2.Variante 34° 22.123
    if str.find(tmp, '\xc2\xba') == 2 and str.find(tmp, ' ') == 4:
        print "V2"
        minutes = tmp[5:7]
    # 3. Variante 34°22 123
    if str.find(tmp, '\xc2') == 2 and str.find(tmp, ' ') == 6:
        print "V3"
        minutes = tmp[4:6]
    # 4. Variante 33 22.123
    if str.find(tmp, ' ') == 2 and tmp.__len__() < 12:
        print "V4"
        minutes = tmp[3:5]
    # 5. Variante 34 º 22.123
    if str.find(tmp, '\xc2 ') == 3:
        print "V5"
        minutes = tmp[6:8]
    # 6. Variante 34 º22 123
    if str.find(tmp, ' \xc2') == 2 and tmp.__len__() == 11:
        print "v6"
        minutes = tmp[5:7]
    # 7. Variante 34'33.123
    if str.find(tmp, "'") == 2 and tmp.__len__() == 9:
        print "v7"
        minutes = tmp[3:5]
    # 8. Variante 34°33,123
    if str.find(tmp, '\xc2\xba') == 2 and tmp.__len__() == 10 and str.find(tmp, ',') == 6:
        print "v8"
        minutes = tmp[4:6]
    # 9. Variante "34 º 33 12.3"
    if str.find(tmp, '\xc2\xba') == 3 and tmp.__len__() == 13 and str.find(tmp, '.') == 11:
        print "v9"
        minutes = tmp[6:8]
    # 10. Variantre "34°5.123"
    if str.find(tmp, '\xc2\xba') == 2 and str.find(tmp, '.') == 5 and tmp.__len__() == 9:
        print "V10"
        minutes = tmp[4]

    if minutes is not None:
        minutes = str.replace(minutes, 'O', '')
    if minutes is not None:
        minutes = str.replace(minutes, '.', '')

    seconds = tmp[tmp.__len__() - 3:tmp.__len__()]
    seconds = str.replace(seconds, '.', '')
    seconds = str.replace(seconds, 'O', '')

    print 'Degrees: {}'.format(degrees)
    print 'Minutes: {}'.format(minutes)
    print 'Seconds: {}'.format(seconds)
    out = None
    if degrees is not None and minutes is not None and seconds is not None:
        out = '{degrees},{minutes},{seconds}'.format(degrees=degrees, minutes=minutes, seconds=seconds)
    return out

def convert_degrees_to_decimal(coord):
    """
    Converts degrees into decimal degrees
    """
    out = None
    if coord is not None:
        tmp = str.split(coord, ',')
        try:
            degrees = int(tmp[0])
        except ValueError:
            degrees = None

        try:
            minutes = int(tmp[1])
        except ValueError:
            minutes = None

        try:
            seconds = int(tmp[2])
        except ValueError:
            seconds = None

        out = -(degrees + minutes / 60.0 + seconds / 3600.0)
    return out

def convert_arbol_diametro(area):
    """
    Converts the numeric value of plot size into plot size class
    """
    try:
        area = int(area)
    except:
        warn_msg = "Cannot convert the plot area {area} to a integer numer".format(area=area)
        logging.warn(warn_msg)
    if area == '':
        out = None
    elif area <= 113:
        out = 1
    elif area <= 314:
        out = 2
    elif area <= 616:
        out = 3
    elif area <= 1018:
        out = 4
    else:
        out = None
    return out

def convert_arbol_radius(radius):
    """
    Converts the numeric value of plot radius into plot size class
    :param radius: Plot Rrdius in meter
    """
    if radius == '':
        out = None
    elif radius <= 6:
        out = 1
    elif radius <= 10:
        out = 2
    elif radius <= 14:
        out = 3
    elif radius <= 18:
        out = 4
    return out

def import_variable(row, variable, type, plotid, codelist=None, treeid=None):
    """
    Function to import_modules variable of a specific type from the a row of values
    :param row: A dictionary with keys and values
    :param variable: The name of the key that should be extracted
    :param type: The type of variable (int, float, string or code)
    :param plotid: The plot ID
    :param codelist: the code_list that should be used for the lookup
    :return: a well formated variable or None and a warning in the logger file
    """
    assert isinstance(row,dict), 'Row should be a dictonary'
    assert isinstance(variable,str),'Variable should be a string'
    assert isinstance(type, str), 'Code should be a string'
    assert type in ['int','float','code','string'], 'Type should be either int,float,code or string'
    assert isinstance(plotid,str), 'PlotID should be a string'
    if codelist is not None:
        assert isinstance(codelist,dict), 'The code list should be a dict'
    if treeid is not None:
        assert isinstance(treeid,str), 'The tree id  should be a string'
    #Check if variable name is empty:
    if variable in ['',' ']:
        error_msg = "An empty variable string was specified"\
            .format(var=variable,plotid=plotid)
        logging.error(error_msg)
        return

    #Check if variable exits
    if not row.has_key(variable):
        error_msg = "The variable {var} was not found for plot: {plotid}"\
            .format(var=variable,plotid=plotid)
        logging.error(error_msg)
        return
    #Check if variable is empty
    if row[variable] in ['',' ']:
        debug_msg = "The variable \"{var}\" is empty on plot: {plotid}" \
            .format(var=variable, plotid=plotid)
        if treeid is not None:
            debug_msg = "The variable \"{var}\" is empty for tree: {treeid} on plot: {plotid}" \
                .format(var=variable, treeid=treeid,plotid=plotid)
        logging.debug(debug_msg)
        if type == 'string':
            return '-'
        else:
            return
    if type == 'int':
        try:
            return int(row[variable])
        except ValueError:
            error_msg = "The variable {var} with value \"{value}\" could not be converted to an " \
                       "integer number for plot: {plotid}".format(var=variable,value=row[variable],plotid=plotid)
            logging.error(error_msg)
            return
    if type == 'float':
        try:
            fl=row[variable].replace(',','.')
            return float(fl)
        except ValueError:
            if treeid is not None:
                error_msg = "The variable \"{var}\" with value \"{value}\" could not be converted to a " \
                           "float number for tree: {treeid} on plot: {plotid}".\
                    format(var=variable, value=row[variable], treeid=treeid,plotid=plotid)
            else:
                error_msg = "The variable \"{var}\" with value \"{value}\" could not be converted to a " \
                            "float number for plot: {plotid}".format(var=variable, value=row[variable], plotid=plotid)
            logging.error(error_msg)
            return
    if type =='code':
        if row[variable].strip() == 'No Aplicable':
            return
        if codelist:
            try:
                value = find_key(codelist,row[variable].strip())
                if value:
                    return value
                else:
                    error_msg = "The variable {var} with value \"{value}\" could not be found in code list {list} " \
                                    "for plot: {plotid}".format(var=variable, value=row[variable], list=codelist,
                                                               plotid=plotid)
                    logging.error(error_msg)
                    return
            except ValueError:
                error_msg = "The variable {var} with value \"{value}\" could not be found in code list {list} "\
                                "for plot: {plotid}".format(var=variable, value=row[variable], list= codelist,plotid=plotid)
                logging.error(error_msg)
                return
        else:
            error_msg = "The variable codelist was not set for varriable {var}".format(var=variable)
            logging.error(error_msg)
            return
    if type=='string':
            try:
                stri = row[variable].replace(',',';')
                stri = stri.replace('"','')
                stri =stri.strip()
                return stri
            except ValueError:
                error_msg = "The variable {var} with value \"{value}\" could not be converted to a " \
                           "string for plot: {plotid}".format(var=variable, value=row[variable], plotid=plotid)
                logging.error(error_msg)
            return '-'

def import_survey(infile,PlotIDName,censo):
    """
    Function to create a new survey instance from a sampling list in OF Collect

    :param infile: Filepath of the exported sampling list from OF Collect
    :param PlotIDName: The name of the column specifing the plotID
    :param censo: The censo number to be created
    :return:
    """
    survey = class_lib.Survey(1)
    with open(infile, 'rb') as samplingfile:
         datareader = csv.DictReader(samplingfile, delimiter=',')
         for row in datareader:
             ID = row[PlotIDName]
             if ID.__len__() > 0:
                 survey.add_plot(ID, censo_id=censo)
    return survey

def import_species_list(infile):
    """
    Function to import_modules species lists in the OF Collect format
    :param infile: Filepath of the exported species list from OF Collect
    :return: A dictonatry with species class instances for each species
    """
    with open(infile, 'rb') as csvfile:
        datareader = csv.DictReader(csvfile, delimiter=',')
        species_list = {}
        for row in datareader:
            species = class_lib.Species(row['no'], row['code'], row['scientific_name'])
            species.common_name = row['synonyms']
            species_list[species.species_id] = species
    return species_list


def get_git_tag():
    str = subprocess.check_output(['git', 'describe', '--tags', 'HEAD'])
    if str not in ['']:
        return str
    else:
        return None

def which(program):
    import os
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None
