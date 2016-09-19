Data Preparation
================

The forest inventory data in the old formats was delivered in Excel spreadsheets wih "xls" and "xlsx" formats. Due to
issues related to the propriety format of Microsoft Excel we decided to import only plan Comma separated testfile (CSV).
The files need to use the "," as a separator, "." as decimal and need to have a utf8 encoding. Furthermore, it is important that the CSV
files can differentiate line breaks from "breaks with in strings /cells". Therefore, you must not use the export
function of Excel, as this will corrupt the linebreaks in cases where long comment fields include breaks as well. As an
alternative we used the open source software `LibreOffice <https://www.libreoffice.org/>`_ .

