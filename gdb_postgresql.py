
from gdb.printing import RegexpCollectionPrettyPrinter, register_pretty_printer
import gdb

def inspect_node(val):
  node = val.cast(gdb.lookup_type("Node"))
  node_type = str(node['type'])
  return node_type[2:]

class Registry(type):
  printers = list()

  def __init__(cls, name, bases, clsdict):
    if len(cls.mro()) > 2:
      Registry.printers.append((name, cls))
    super(Registry, cls).__init__(name, bases, clsdict)

class PgObject(object, metaclass=Registry):

  def __init__(self, val):
    self.val = val.cast(self.pgtype)

  def to_string(self):
    data = []
    for f in self.pgtype.fields():
      if f.name in self.skipped_fields:
        continue

      val = self.val[f]
      str_val = str(val)

      if str_val == "0x0":
        continue

      if gdb.default_visualizer(val):
        str_val = gdb.default_visualizer(val).to_string()

      elif str(f.type) == "List *" and str_val != "0x0":
        str_val = gdb.default_visualizer(val.dereference()).to_string()
      elif str(f.type) == "Bitmapset *" and str_val != "0x0":
        str_val = gdb.default_visualizer(val.dereference()).to_string()

      data.append("{}={}".format(f.name,str_val))

    return "<{} {}>".format(self.pgtype.name, ", ".join(data))

class Bitmapset(PgObject):
  pgtype = gdb.lookup_type('Bitmapset')
  skipped_fields = []

  def to_string(self):
    return "<Bitmapset>"

class RelOptInfo(PgObject):
  pgtype = gdb.lookup_type('RelOptInfo')
  skipped_fields = ['type']

class RestrictInfo(PgObject):
  pgtype = gdb.lookup_type('RestrictInfo')
  skipped_fields = ['type']

class Const(PgObject):
  pgtype = gdb.lookup_type('Const')
  skipped_fields = ['constbyval','constcollid','constlen','consttypmod','location','xpr']

class Var(PgObject):
  pgtype = gdb.lookup_type('Var')
  skipped_fields = ['varnosyn','varattnosyn','vartypmod','varcollid','location','xpr']

class OpExpr(PgObject):
  pgtype = gdb.lookup_type('OpExpr')
  skipped_fields = ['inputcollid','opcollid','opretset','location','xpr']

class List(PgObject):
  pgtype = gdb.lookup_type('List')

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
      typed_val = val.cast(gdb.lookup_type(inspect_node(node_val)).pointer()).dereference()
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

  for (name, cls) in Registry.printers:
    pp.add_printer(name, "^{}$".format(name), cls)

  return pp

gdb.printing.register_pretty_printer(None, register_printers(), True)
