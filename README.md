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
 
### example1.py
* It is a usecase of PDMHandler class, read it as a reference code.
* example1.py shows 5 levels of pdm file -- Package/Table/Column/Index/IndexColumn
* each level has their own attributes which are defined in PDMHandler class :
``` python
PKG_ATTR_LIST=["Name","Code","CreationDate","Creator","ModificationDate","Modifier"]
TBL_ATTR_LIST=["Name","Code","CreationDate","Creator","ModificationDate","Modifier", "PhysicalOptions"]
COL_ATTR_LIST=["Name","Code","CreationDate","Creator","ModificationDate","Modifier", "DataType","Length","Column.Mandatory","Comment"]
IDX_ATTR_LIST=["Name","Code","CreationDate","Creator","ModificationDate","Modifier", "PhysicalOptions","Unique"]
IDXCOL_ATTR_LIST=["CreationDate","Creator","ModificationDate","Modifier"]
```

By running :
``` shell
$ python example1.py testpdm/Consol.pdm Consul_datadict.xlsx
```

will read the PowerDesigner Physical Data Model (PDM) file located at testpdm and write a data dictionary to the Consul_datadict.xlsx excel file
