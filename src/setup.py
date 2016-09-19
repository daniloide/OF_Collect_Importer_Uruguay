from distutils.core import setup
import py2exe
import sys
sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True,'excludes': ['Tkconstants', 'Tkinter']}
               },
    console = ['src/import_modules/import_trees.py',
               'src/import_modules/import_plots.py',
               'src/import_modules/import_distances.py',
               'src/import_modules/import_forest_flora.py',
               'src/import_modules/import_soil_flora.py',
               'src/import_modules/import_fauna.py',
               'src/import_modules/import_equipment.py',
               'src/import_modules/import_fotos.py',
               'src/import_modules/import_invasives.py',
               'src/import_modules/import_regeneration.py'],
    zipfile = None,
   # data_files = DATA,
)
