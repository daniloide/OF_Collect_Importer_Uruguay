.. _sec-upload:

Workflow in OF Collect
======================


Uploading the generated csv files into the OF Collect database
--------------------------------------------------------------

The OF Collect software offers various options to import data from external sources. Besides the options to import data
in the collect xml format it is also possible to import data as csv text files. For each of the different
tables that is available in the OF Collect database schema a separate csv file can be uploaded. The OF upload functions
are started from the "*Data Management*" module under "*Import Data*":

.. figure:: _figures/OF_collect_import_dialog.png
    :scale: 70 %

    Screenshot of the OF Collect Import Dialog

As import type "*CSV file*" need to be selected. As the plot information is the 'root' knot of the OF Collect schema
it is required to upload the plot information first. When importing plot data for the first time you need to choose
the option "*Insert new records*". Once the plots are uploaded you can later uploaded modified files for the same
plots with the option "*Updated existing records*". For the import we recommend the following order

    #. Plot records (If you upload the plot files to a new empty OF Collect database you need to choose the option "insert new records)"
    #. Tree records (e.g. arbols_bn_2010.csv, arbols_pl_2010.csv)
    #. Foto records
    #. Distance records
    #. Equipment / Team records
    #. Fauna records (Mammal, Amphibians, Birds, Reptiles)
    #. Forest flora records (sotobosque)
    #. Soil flora records (flora suelo)
    #. Invasive species records
    #. Regeneration records



Data cleansing
--------------

The data cleansing can be done in two steps:

    #. When any of the import_modules are executed a log file is created with different information about the data
        translation process. Here, you will find information on such as misspelled or unknown species names or codes. \
        Missing information in the dataset etc. If you run the import modules with the flag "*-v*" you will also get \
        information about missing values.
    #. While uploading the data files and internal validation will be done and OF Collect will display errors and warnings in the data management view.

There are different reasons why an error is issued when uploading the data:

* The value for a required variable was not set as it is not provided in the raw data
* The value is out of the value range
* The included validation procedures raise a warning (e.g. GPS coordinates to far from the original plot coordinates)

Before a meaningful analysis of the inventory data can be done the pending warnings and errors should be resolved for
each of the plots. OF Collect offers the data cleansing module for this task! Furthermore, the data management module
shows the number of errors and warnings for each plot. And allows to create a validation report. Further information
on the data management workflow in OF collect can be found in the `OF Collect Tutorial <http://www.openforis
.org/tools/collect/tutorials/data-management.html>`_.
