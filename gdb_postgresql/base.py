
import gdb
from traceback import print_exception

class Registry(type):
  printers = dict()

  def __init__(cls, name, bases, clsdict):
    if len(cls.mro()) > 2:
      Registry.printers[name] = cls
    super(Registry, cls).__init__(name, bases, clsdict)

class PgObject(object, metaclass=Registry):
  prefix = ""
  skipped_fields = ['type']

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

        if field_name == 'location' and self.val[f] >= -1:
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

def inspect_node(val):
  node = val.cast(gdb.lookup_type("Node"))
  node_type = str(node['type'])

  return node_type[2:]

