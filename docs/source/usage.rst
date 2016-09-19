
Usage of the import modules
===========================
The import modules provide the functionality to generate csv files which can later be uploaded to OF collect (see :ref:`sec-upload`).
The data import modules are provided in three ways. They can be used as `Windows binaries`_ , as `Python scripts`_ or as
`Python modules`_ The syntax for the usage of the program as python script or as windows binarie in the Windows console
is identical.

Windows binaries
----------------

The windows binaries are provided as standalone executables. Thus no further installation of software is required. They
can be used from the Windows commandline. For each of the Import Modules provided a explantaion can be obtained from the documentation
or from the program itself by submitting the command with a "-h" flag e.g.

.. code-block:: bat

    import_distances.exe -h

    usage: import_distances.exe [-h] [-v] [-f {2010,2015}] [-log LOGFILENAME]
                            InFileNamePlots OutFileName

    Function to create csv of the distance recordings

    positional arguments:
    InFileNamePlots       Input csv file with 2010 plot data
    OutFileName           Outputfile Name

    optional arguments:
    -h, --help            show this help message and exit
    -v, --verbose         increase output verbosity
    -f {2010,2015}, --format {2010,2015}
                        The data format either '2010' or '2015'
    -log LOGFILENAME, --LogFileName LOGFILENAME
                        Filepath for the logfile

A complete list of all import modules as well as a detailed documentation is procided here :ref:`sec-import-modules`


Python scripts
--------------

If you have a running version of Python 2.7 installed on your system you can call the import modules also as standalone python script.

.. code-block:: bat

    python import_distances.py -h
    usage: import_distances.py [-h] [-v] [-f {2010,2015}] [-log LOGFILENAME]
                           InFileNamePlots OutFileName

    Function to create csv of the distance recordings

    positional arguments:
        InFileNamePlots       Input csv file with 2010 plot data
        OutFileName           Outputfile Name

    optional arguments:
        -h, --help            show this help message and exit
        -v, --verbose         increase output verbosity
        -f {2010,2015}, --format {2010,2015}
                        The data format either "2010" or "2015"
        -log LOGFILENAME, --LogFileName LOGFILENAME
                        Filepath for the logfile




Python modules
--------------

The last option to use the software is to develop your own import scripts based on the class-api. The major advantages
of this approach is the option to import multiple files / data sources into one survey instance and then to export only
one csv. Following this path it is possible e.g. to import all files from 2010 and 2015 and then export only one csv file
for each table. However, this requires basic Python programming skills. In the follwing block we provide a minimal example
for importing the distances records from two differn files and exporting them in one csv:

To be continued

.. code-block:: python

