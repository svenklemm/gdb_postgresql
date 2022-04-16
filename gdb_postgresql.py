
import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
if not script_dir in sys.path:
    sys.path.append(script_dir)

from gdb.printing import RegexpCollectionPrettyPrinter, register_pretty_printer
import gdb
from traceback import print_exception

from gdb_postgresql.mapper import oid_to_type, varno_to_name

def inspect_node(val):
  node = val.cast(gdb.lookup_type("Node"))
  node_type = str(node['type'])

  return node_type[2:]

class Registry(type):
  printers = dict()

  def __init__(cls, name, bases, clsdict):
    if len(cls.mro()) > 2:
      Registry.printers[name] = cls
    super(Registry, cls).__init__(name, bases, clsdict)

class PgObject(object, metaclass=Registry):
  prefix = ""

  def __init__(self, val):
    if not hasattr(self.__class__, 'typename'):
      self.typename = self.__class__.__name__

    self.pgtype = gdb.lookup_type(self.typename)

    self.val = val.cast(self.pgtype)

  def to_string(self):
    data = []
    try:
      for f in self.pgtype.fields():
        field_name = f.name
        if hasattr(self.__class__, 'skipped_fields') and field_name in getattr(self.__class__, 'skipped_fields'):
          continue

        val = self.val[f]
        str_val = str(val)

        if str_val == "0x0":
          continue

        if gdb.default_visualizer(val):
          str_val = gdb.default_visualizer(val).to_string()
        elif str(f.type) == "void *":
          pass
        elif str(f.type) == "char *" and str_val != "0x0":
          str_val = repr(val.string())
        elif str(f.type)[-2:] == " *" and str_val != "0x0" and gdb.default_visualizer(val.dereference()):
          str_val = gdb.default_visualizer(val.dereference()).to_string()
        elif str(f.type) == "Relids" and str_val != "0x0":
          str_val = gdb.default_visualizer(val.dereference()).to_string()
        elif hasattr(self.__class__, 'lookup_' + f.name):
          str_val = getattr(self.__class__, 'lookup_' + f.name)(self, val)

        if self.prefix and field_name.startswith(self.prefix):
          field_name = f.name[len(self.prefix):]

        data.append("{}={}".format(field_name,str_val))

      return "<{} {}>".format(self.pgtype.name, ", ".join(data))
    except BaseException as err:
      print_exception(err)
      raise

class Node(PgObject):

  def to_string(self):
    node_type = inspect_node(self.val)
    if node_type in Registry.printers.keys():
      return Registry.printers[node_type](self.val).to_string()

    return "<{}>".format(node_type)

class Expr(Node):
  pass

class Value(PgObject):
  def to_string(self):
    node_type = inspect_node(self.val)
    if node_type == "String":
      return repr(self.val['val']['str'].string())
    else:
      return self.val['val']['ival'].string()

class String(Value):
  typename = "Value"

class Alias(PgObject):
  skipped_fields = ['type']

class Bitmapset(PgObject):
  bits_per_word = 64 

  def to_string(self):
    nwords = self.val['nwords']

    exps = list()
    for i in range(nwords):
      num = self.val['words'][i]
      for b in range(self.bits_per_word):
        if num % 2 == 1:
          exps.append(str(b + i * self.bits_per_word))

        num = num >> 1

    return "<Bitmapset {}>".format(" ".join(exps))

class RangeTblEntry(PgObject):
  skipped_fields = ['type']

class RelOptInfo(PgObject):
  skipped_fields = ['type','consider_startup','consider_param_startup','consider_parallel']

class RestrictInfo(PgObject):
  skipped_fields = ['type']

class Const(PgObject):
  prefix = "const"
  skipped_fields = ['constbyval','constcollid','constlen','consttypmod','location','xpr']

  lookup_consttype = oid_to_type

class FuncExpr(PgObject):
  prefix = "func"
  skipped_fields = ['funcformat','funcvariadic','funcretset', 'funccollid', 'inputcollid', 'location', 'xpr']

class Var(PgObject):
  prefix = "var"
  skipped_fields = ['varnosyn','varattnosyn','vartypmod','varcollid','location','xpr']

  lookup_vartype = oid_to_type
  lookup_varno = varno_to_name

class OpExpr(PgObject):
  prefix = "op"
  skipped_fields = ['inputcollid','opcollid','opretset','location','xpr']

  lookup_opresulttype = oid_to_type

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

def register_printers():
  pp = RegexpCollectionPrettyPrinter("postgresql")

  for (name, cls) in Registry.printers.items():
    pp.add_printer(name, "^{}$".format(name), cls)

  return pp

gdb.printing.register_pretty_printer(None, register_printers(), True)
