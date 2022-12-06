#!/usr/bin/python
# -*- coding: utf-8 -*- #

from xml.dom.minidom import parse
import xml.dom.minidom

class CDMHandler(object):
  PKG_ATTR_LIST    = ["Name","Code","CreationDate","Creator"]
  ENT_ATTR_LIST    = ["Name","Code","CreationDate","Creator"]
  def __init__(self):
    return

  @staticmethod
  def parse(cdmfilename):
    return xml.dom.minidom.parse(cdmfilename)

  @staticmethod
  def __get_nodes_by_path(parent,xml_path):
    curr_node = parent
    for tag in xml_path.split("/")[0:-1] :
      tag_desc = tag.split("|")
      tag_name,tag_index = tag_desc[0], ( int(tag_desc[1]) if len(tag_desc) == 2 else 0 )
      child_nodes = []
      for child_node in curr_node.childNodes :
        if child_node.nodeName == tag_name :
          child_nodes.append(child_node)
      if len(child_nodes) < tag_index + 1 :
        return []
      curr_node = child_nodes[tag_index]
    tag = xml_path.split("/")[-1]
    tag_desc = tag.split("|")
    tag_name,tag_index = tag_desc[0], ( int(tag_desc[1]) if len(tag_desc) == 2 else None )
    child_nodes = []
    for child_node in curr_node.childNodes :
      if child_node.nodeName == tag_name :
        child_nodes.append(child_node)
    if tag_index == None :
      return child_nodes
    elif len(child_nodes) < tag_index + 1 :
      return []
    else :
      curr_node = child_nodes[tag_index]
      return curr_node

  @staticmethod
  def __get_attrs_by_list(parent,attr_list):
    ret_dict = {}
    for attr in attr_list :
      ret_dict[attr] = ""
      for child in parent.childNodes :
        if child.nodeName == "a:" + attr :
          if child.childNodes != []:
            ret_dict[attr] = child.childNodes[0].data
          break
    return ret_dict

  @staticmethod
  def __get_pkgnodes_recursively(o_pkg):
    if o_pkg.nodeName != "o:Model" and o_pkg.nodeName != "o:Package" :
      return []
    ret_list = []
    subpkgs = CDMHandler.__get_nodes_by_path(o_pkg,"c:Packages/o:Package")
    if subpkgs != None :
      for subpkg in subpkgs :
        ret_list.append(subpkg)
        ret_list = ret_list + CDMHandler.__get_pkgnodes_recursively(subpkg)
    else :
      return []
    return ret_list

  @staticmethod
  def getPkgNodes(hpdm):
    ret_list = []
    try:
      o_mdl  = CDMHandler.__get_nodes_by_path(hpdm,"Model/o:RootObject/c:Children/o:Model")[0]
      ret_list.append(o_mdl)
    except IndexError:
      print("ERROR:Cound not parse the index!")
      return []
    ret_list = ret_list + CDMHandler.__get_pkgnodes_recursively(o_mdl)
    return ret_list

  @staticmethod
  def getPkgAttrs(pkgnode):
    return CDMHandler.__get_attrs_by_list(pkgnode,CDMHandler.PKG_ATTR_LIST)

  @staticmethod
  def getEntNodesInPkg(pkgnode):
    return CDMHandler.__get_nodes_by_path(pkgnode, "c:Entities/o:Entity")

  def getEntAttrs(entnode):
    return CDMHandler.__get_attrs_by_list(entnode,CDMHandler.ENT_ATTR_LIST)

  @staticmethod
  def getNodePath(node) :
    curr = node
    path_nodes = []
    while(1):
      if curr != None and curr.nodeName != "#document" :
        path_nodes.append(curr.tagName)
      else :
        break
      curr = curr.parentNode 
    path_nodes.reverse()
    path = "".join([ slash + node for slash in '/' for node in path_nodes ])
    return path

