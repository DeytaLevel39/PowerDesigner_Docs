# References
This is a re-write of the original Python 2 PDMHandler which is available at:- https://github.com/petjiang/PDMHandler

# PDMHandler
A tool class to handle sybase PowerDesigner datafile(.pdm). 
Currently, it is able to handle PhysicalDiagram in .pdm.

## Source Code Intro.
### PDMHandler.py
The class implementation  of PDMHandler.
use following command to see help docs 

``` shell
$ echo "import PDMHandler; help(PDMHandler);"|python
```
### TEST PDM files
 PowerDesigner model file (.pdm) is prepared in [repodir]/src/testpdm
 use these as input argument for testing the example1.py
* NOTICE: (.pdm) files come from PowerDesigner15 directory [Sybase\PowerDesigner 15\Examples]
 
### cr_datadict.py
This will read the PowerDesigner Physical Data Model (PDM) file and write a data dictionary to an excel file
```

By running :
``` shell
$ python example1.py testpdm/Consol.pdm Consul_datadict.xlsx
```

### cr_ddl.py
This will read the PowerDesigner Physical Data Model (PDM) file located at testpdm and write a data definition language (DDL) file

By running :
``` shell
$ python example1.py testpdm/Consol.pdm Consul_datadict.xlsx
```
