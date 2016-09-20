Class API
=========
To separate the programming logic of "*Import*", "*Storage*" and "*Export*" functions we created a set of python packages
for each of this tasks. The core module :ref:`model_label` holds the class description and the main functions required
to store and export the NFI data in the correct format. The packages :ref:`package_data_mappings_2010` and
:ref:`package_data_mappings_2015` provide the modules to import the data in either the 2010 or 2015 data format. For each
information group (e.g. trees, plots, distances) a single module is provided where it is defined which source variable
is used to import the data of a specific target variable of the OF Collect schema. For categorical variables the source information
is translated using the code lists specified in OF Collect. However, as the spelling and naming differs in between the
file versions we created lookup dictionaries which can be found in the module :ref:`label_code_lists`

The code list

.. _model_label:

Data Model
**********
The package holds all generic classes and functions to store the inventory data and to conduct the data mapping
between the 2010 and 2015 data formats

Class Lib
---------

.. automodule:: src.model.class_lib
    :members: Species,Survey,Plot,Tree,Stem,Distance,Foto,Fauna,FloraSuelo,FloraSoto


.. _label_code_lists:

Code Lists
----------

The code list file contains the lookup tables in form of dictionaries for the categorical variables. To give but one
example. The data mapping for the variable "*subbosque_tipo*" is based on the following dictionary:

.. code-block:: python

    subbosque_tipo = {
        11: ['Galería','galería','galeria'],
        12: ['Serrano','serrano'],
        13: ['Parque', 'parque'],
        14: ['Quebrada','quebrada'],
        15: ['Palmar','palmar'],
        21: ['Plantación','plantación','plantacion'],
        22: ['Costero','costero']

Thus all plots where the variable "*subbosque_tipo*"  has values like "Galería","galería","galeria" will be assigned
the category "*11*" which correspond to the class "*Galería*" in OF Collect. Thus, if you find that some of the
categorical, variables are not detected correctly you can add the different spellings to the list of each code. You
can also change which source categories are assigned to which target categories here.


Data Mappings
*************

.. _package_data_mappings_2010:

Data Mapping 2010
-----------------

Import Parcela 2010
~~~~~~~~~~~~~~~~~~~
.. automodule:: src.data_mapping_2010.import_plots_2010
    :members: import_fni_plots_2010

Import Distancia 2010
~~~~~~~~~~~~~~~~~~~~~
.. automodule:: src.data_mapping_2010.import_distancia_2010
    :members:  import_distancia_2010

Import Flora Suelo 2010
~~~~~~~~~~~~~~~~~~~~~~~
.. automodule:: src.data_mapping_2010.import_flora_suelo_2010
    :members:  import_flora_suelo_2010

Import Flora Soto Bosque 2010
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. automodule:: src.data_mapping_2010.import_flora_soto_2010
    :members:  import_flora_soto_2010

Import Fauna 2010
~~~~~~~~~~~~~~~~~
.. automodule:: src.data_mapping_2010.import_fauna_2010
    :members:  import_fauna_2010



.. _package_data_mappings_2015:

Data Mapping 2015
-----------------

Import Parcela 2015
~~~~~~~~~~~~~~~~~~~
.. automodule:: src.data_mapping_2015.import_plots_2015
    :members: import_fni_plots_2015

Import Distancia 2015
~~~~~~~~~~~~~~~~~~~~~
.. automodule:: src.data_mapping_2015.import_distancia_2015
    :members:  import_distanca_2015

Import Flora Suelo 2015
~~~~~~~~~~~~~~~~~~~~~~~
.. automodule:: src.data_mapping_2015.import_flora_suelo_2015
    :members:  import_flora_suelo_2015

Import Flora Soto Bosque 2015
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. automodule:: src.data_mapping_2015.import_flora_soto_2015
    :members:  import_flora_soto_2015

Import Fauna 2015
~~~~~~~~~~~~~~~~~
.. automodule:: src.data_mapping_2015.import_fauna_2015
    :members:  import_fauna_2015

Utils
-----
.. automodule:: src.utils.tools_lib
    :members:  find_key,convert_text_to_numbers,convert_cobertura_copas,convert_cobertura_residuos,find_species,find_species_scientific,find_species_code,find_species_common,convert_plantacion_edad,convert_ntfp_gando_tipo,fix_coordinate_notation,convert_degrees_to_decimal,convert_arbol_diametro,convert_arbol_radius,import_variable,import_survey,import_species_list







