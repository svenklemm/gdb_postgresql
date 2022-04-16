
import gdb

from .base import PgObject, inspect_node

class List(PgObject):
  typename = "List"

  def to_string(self):
    # doublecheck this isn't IntList/OidList
    list_type = inspect_node(self.val)
    if list_type == "OidList":
      return OidList(self.val).to_string()
    if list_type == "IntList":
      return IntList(self.val).to_string()

    length = self.val['length']
    items = list()
    for i in range(length):
      val = self.val['elements'][i]['ptr_value']
      node_val = val.cast(gdb.lookup_type('Node').pointer()).dereference()
      node_type = inspect_node(node_val)
      if node_type == "String":
        node_type = "Value"

      typed_val = val.cast(gdb.lookup_type(node_type).pointer()).dereference()
      if gdb.default_visualizer(typed_val):
        str_val = gdb.default_visualizer(typed_val).to_string()
      else:
        str_val = str(node_val)

      items.append(str_val)

    return "<List {}>".format(", ".join(items))

class IntList(List):

  def to_string(self):
    length = self.val['length']
    items = list()
    for i in range(length):
      val = self.val['elements'][i]['int_value']
      items.append(str(val))

    return "<IntList {}>".format(", ".join(items))

class OidList(List):
 
  def to_string(self):
    length = self.val['length']
    items = list()
    for i in range(length):
      val = self.val['elements'][i]['oid_value']
      items.append(str(val))

    return "<OidList {}>".format(", ".join(items))

