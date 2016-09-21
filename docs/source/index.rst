.. IFN data mirgation Uruguay documentation master file, created by
    sphinx-quickstart on Wed Aug 10 20:58:03 2016.
    You can adapt this file completely to your liking, but it should at least
    contain the root `toctree` directive.

Documentation of the NFI data migration module for the Project W-URY-15-01
==========================================================================

Project Background
------------------

In the context of the Project W-URY-15-01 `ForestEye Research <http://www.foresteye.de/>`_ developed a new database
for managing the National Forest Inventory (NFI) data of Uruguay. The database was created using the Collect module
of the `OpenForis <http://www.openforis.org/>`_ software developed by FAO. The monitoring program already collected a
large number of plots during the years 2010, 2011 and 2015. However, in lack of a unique database there are different
data formats for each of the periods making a comprehensive analysis difficult. In a joint effort with the Direcíon
Gerneral Forestal (DGF), ForestEye Research developed software to migrate the collected information from the
various old formats into a standard format that can be used to import the existing NFI data into the new collect
database.

Conceptual Framework & Program Structure
-----------------------------------------

We tried to develop the software in a way that they it can adapted to either changes in the collect database
structure or changes in the input data structure. Therefore, the *import*, *storage* and *export* logic are separated
as far as possible. In that sense we are able to provide sufficient flexibility to adopt the modules also to other
NFI data sets in the future. However, it need to be said, that mapping data from one format to another is always
quite project specific and the degree of generalization is limited.

The separation is achieved by structuring ths software into four packages as shown in the structure of the source
folder:

.. code-block:: bash

    project
    |-- src
    |    |-- data_mapping_2010
    |    |-- data mapping_2015
    |    |-- import_modules
    |    |   |-- import_distances.py
    |    |   |-- import_equipment.py
    |    |   |-- import_fauna.py
    |    |   |-- import_fotos.py
    |    |   |-- import_forest_flora.py
    |    |   |-- import_soil_flora.py
    |    |   |-- import_regeneration.py
    |    |   |-- import_invasives.py
    |    |   |-- import_trees.py
    |    |   |-- import_plots.py
    |    |-- model
    |    |    |-- class_lib
    |    |    |-- code_list
    |    |-- utils
    |    |    |-- tools_lib

The module "*class_lib*" in the package "*model*" defines the important classes and functions to store and export
the data in the OF Collect data format. Thus, when the OF Collect Schema changes such that new variables are added or
variables are renamed only the "*class_lib.py*" module need to be adapted. The data mappings for the formats
"*2010*" and "*2015*" are defined in the corresponding modules. Here it is define which source variable is mapped to
which target variable. Thus, changes in the input data will mainly affect the data_mapping modules. The "*Utils*"
package provides a set of helper functions to safeguard the import of variables or to convert the format (e.g.
degree in minutes, seconds to decimal degree). Finally, the the package "*import modules*" contains the executable
scripts that can be used to preform the data translation.

Contents
--------

.. toctree::
    :maxdepth: 2

    installation
    data_preparation
    usage
    data_upload_collect
    import_modules
    class_api



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

