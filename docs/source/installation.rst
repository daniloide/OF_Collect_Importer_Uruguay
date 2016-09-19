Installation and Prerequisite
=============================

The usage of the different :ref:`sec-import-modules` usually does'nt require the installation of any additional software.
However, in some cases specific Microsoft Visual C runtime dll files need to be installed. The binaries are created
using the software `Py2exe <http://py2exe.org>`_. If you encounter runtime errors when using the binaries make sure you
have the required Microsoft Visual C runtime dlls installed. You can find an instruction how to install them
the `Py2exe Tutorial <http://py2exe.org/index.cgi/Tutorial>`_ at section 5.

If you wish to modify the code or run the provided Python scripts or modules you need have a Python 2.7.x version
installed on your system. Toc check if this is already available on your system Window users can open the command line
from the start menu (search for cmd.exe) and type:

.. code-block:: python

    python -v

If this shows you output including a Python version number 2.7.x no action is required. If you get an error message e.g.
command unknown it is very likely that Python is not yet installed on your system. In this case please download the latest
Windows installer for Python 2.7.x from the official `Python <https://www.python.org/downloads/>`_ repositories. Make
sure that you are not installing Python 3.x!



