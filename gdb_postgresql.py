
import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
if not script_dir in sys.path:
    sys.path.append(script_dir)

from gdb.printing import RegexpCollectionPrettyPrinter, register_pretty_printer
import gdb

from gdb_postgresql.mapper import oid_to_type, varno_to_name
from gdb_postgresql.base import Registry, PgObject, Node, inspect_node
from gdb_postgresql.lists import *
from gdb_postgresql.value import *
from gdb_postgresql.bitmapset import Bitmapset

class Expr(Node):
  pass

class Alias(PgObject):
  skipped_fields = ['type']

class RangeTblEntry(PgObject):
  skipped_fields = ['type']

class RelOptInfo(PgObject):
  skipped_fields = ['baserestrictcost','baserestrict_min_security','consider_partitionwise_join','consider_startup','consider_param_startup','consider_parallel','type']

class RestrictInfo(PgObject):
  skipped_fields = ['eval_cost','left_bucketsize','left_mcvfreq','mergeopfamilies','norm_selec','outer_selec','right_bucketsize','right_mcvfreq','type']

class Const(PgObject):
  prefix = "const"
  skipped_fields = ['constbyval','constcollid','constlen','consttypmod','location','xpr']

  lookup_consttype = oid_to_type

class TargetEntry(PgObject):
  skipped_fields = ['resorigcol','resorigtbl','type','xpr']

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

def register_printers():
  pp = RegexpCollectionPrettyPrinter("postgresql")

  for (name, cls) in Registry.printers.items():
    pp.add_printer(name, "^{}$".format(name), cls)

  return pp

gdb.printing.register_pretty_printer(None, register_printers(), True)
