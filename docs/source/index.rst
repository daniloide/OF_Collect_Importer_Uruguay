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
large number of plots during the years 2010,2011 and 2015. However, in lack of a unique database there are also different
data formats for each of this periods making a wider analysis difficult. In a joint effort with the Direcíon Gerneral
Forestal (DGF) ForestEye Research developed software to translate the different old data formats into a standard format
that can be used to import the NFI data nto the new NFI collect database.

Conceptual Framework
--------------------

We tried to develop the modules in a way that they can be adapted to either changes in the collect database structure or
changes in the input data structure. In order to do so we separated the *import*, *storage* and *export* logic as far as
possible. In that sense we are able to provide sufficient flexibility to adopt the modules also to other NFI data sets
in the future. However, it need to be said, that mapping data from one format to another is always quite project specific.


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

