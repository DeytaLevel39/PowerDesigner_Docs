# References
This is a re-write of the original Python 2 PDMHandler which is available at:- https://github.com/petjiang/PDMHandler

This is a Python 3 version with improved documentation output formats

# PowerDesigner_Docs
Python scripts designed to generate documentation from 
Sybase PowerDesigner datafiles
. 
Currently, it is able to handle:-
* Conceptual Data Model (.cdm) files
* Physical Data Model (.pdm) files

## TEST CDM files

Run from the src directory

### cr_cdm_datadict.py
This will read the PowerDesigner Conceptual Data Model (CDM) file and write a data dictionary to an excel file
```
By running :
``` shell
$ python cr_cdm_datadict.py testpdm\<filename>.cdm <filename>_datadict.xlsx
e.g. 
$ cr_cdm_datadict.py testpdm\project.cdm project_cdm_datadict.xlsx
```

## TEST PDM files
* NOTICE: (.pdm) files come from PowerDesigner15 directory [Sybase\PowerDesigner 15\Examples]

### cr_pdm_datadict.py
This will read the PowerDesigner Physical Data Model (PDM) file and write a data dictionary to an excel file
```
By running :
``` shell
$ python cr_pdm_datadict.py testpdm\project.pdm project_pdm_datadict.xlsx
```

### cr_pdm_ddl.py
This will read the PowerDesigner Physical Data Model (PDM) file located at testpdm and write a data definition language (DDL) file

By running :
``` shell
$ python cr_pdm_ddl.py testpdm\project.pdm project.ddl
```
