#!/usr/bin/python
# -*- coding: utf-8 -*- #

from PDMHandler import PDMHandler
if __name__ == '__main__' :
  import sys
  if len(sys.argv) != 3:
    print("USAGE:   ",sys.argv[0],"<filename> <ddl file>")
    print("EXAMPLE: ",sys.argv[0],"testpdm/Consol.pdm Consol.ddl")
    sys.exit(1)
  else:
    filename = sys.argv[1]
    ddl_file = open(sys.argv[2],"w")
  ph = PDMHandler.parse(filename)
  for pkg in PDMHandler.getPkgNodes(ph):
    pkg_attrs = PDMHandler.getPkgAttrs(pkg)
    for tbl in PDMHandler.getTblNodesInPkg(pkg) :
      tbl_attrs = PDMHandler.getTblAttrs(tbl)
      ddl_file.write("%s %s %s"%("CREATE TABLE",tbl_attrs["Code"],"(\n"))
      cols = PDMHandler.getColNodesInTbl(tbl) 
      for col in cols :
        col_attrs = PDMHandler.getColAttrs(col)
        ddl_file.write(" %-16s %-16s"%(col_attrs["Code"],col_attrs["DataType"]))
        if col_attrs["Column.Mandatory"] == "1" : ddl_file.write("NOT NULL")
        else: ddl_file.write("        ")
        if cols.index(col) != len(cols) - 1 : ddl_file.write(",\n")
        else : ddl_file.write(");\n\n")
      for idx in PDMHandler.getIdxNodesInTbl(tbl) :
        idx_attrs = PDMHandler.getIdxAttrs(idx)
        if idx_attrs["Unique"] == "1" : ddl_file.write("CREATE UNIQUE INDEX %s \n("%idx_attrs["Code"])
        else : ddl_file.write("CREATE INDEX %s\n("%idx_attrs["Code"])
        idxcols = PDMHandler.getIdxColNodesInIdx(idx) 
        for idxcol in  idxcols :
          idxcol_attrs = PDMHandler.getIdxColAttrs(idxcol)
          ddl_file.write(str(["  ", "%-16s "%idxcol_attrs["RefColCode"],"ASC",]))
          if idxcols.index(idxcol) != len(idxcols) - 1 : ddl_file.write(",")
          else : ddl_file.write("\n);")
