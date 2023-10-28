import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
if not script_dir in sys.path:
    sys.path.append(script_dir)

from gdb.printing import RegexpCollectionPrettyPrinter, register_pretty_printer
import gdb

from gdb_postgresql.mapper import (
    lockmode_to_name,
    oid_to_operator,
    oid_to_proc,
    oid_to_type,
    relkind_to_name,
    varno_to_name,
)
from gdb_postgresql.base import Registry, PgObject, Node, inspect_node
from gdb_postgresql.lists import *
from gdb_postgresql.value import *
from gdb_postgresql.bitmapset import Bitmapset


class Expr(Node):
    pass


class EquivalenceMember(PgObject):
    prefix = "em_"
    skipped_fields = ["type"]
    skipped_zero = [
        "em_is_const",
        "em_is_child",
    ]
    lookup_em_datatype = oid_to_type


class FromExpr(PgObject):
    skipped_fields = ["type"]


class Query(PgObject):
    skipped_fields = ["canSetTag", "stmt_len", "type"]
    skipped_zero = [
        "groupDistinct",
        "hasAggs",
        "hasDistinctOn",
        "hasForUpdate",
        "hasModifyingCTE",
        "hasRecursive",
        "hasRowSecurity",
        "hasSubLinks",
        "hasTargetSRFs",
        "hasWindowFuncs",
        "isReturn",
        "override",
        "resultRelation",
        "stmt_location",
    ]


class RangeTblRef(PgObject):
    skipped_fields = ["type"]


class Alias(PgObject):
    prefix = "alias"
    skipped_fields = ["type"]


class RangeTblEntry(PgObject):
    skipped_fields = ["type"]
    skipped_zero = [
        "checkAsUser",
        "ctelevelsup",
        "enrtuples",
        "funcordinality",
        "inFromCl",
        "inh",
        "joinmergedcols",
        "lateral",
        "perminfoindex",
        "relid",
        "relkind",
        "security_barrier",
        "self_reference",
    ]
    lookup_relkind = relkind_to_name
    lookup_rellockmode = lockmode_to_name


class RelOptInfo(PgObject):
    skipped_fields = [
        "allvisfrac",
        "amflags",
        "attr_needed",
        "attr_widths",
        "baserestrictcost",
        "baserestrict_min_security",
        "consider_parallel",
        "consider_param_startup",
        "consider_partitionwise_join",
        "consider_startup",
        "eclass_indexes",
        "has_eclass_joins",
        "lateral_referencers",
        "nparts",
        "partbounds_merged",
        "rel_parallel_workers",
        "serverid",
        "type",
        "userid",
        "useridiscurrent",
    ]


class RestrictInfo(PgObject):
    skipped_fields = [
        "eval_cost",
        "left_bucketsize",
        "left_mcvfreq",
        "mergeopfamilies",
        "norm_selec",
        "outer_selec",
        "outerjoin_delayed",
        "right_bucketsize",
        "right_mcvfreq",
        "type",
    ]
    skipped_zero = [
        "outer_is_left",
        "hashjoinoperator",
        "left_hasheqoperator",
        "right_hasheqoperator",
    ]


class Const(PgObject):
    prefix = "const"
    skipped_fields = [
        "constbyval",
        "constcollid",
        "constlen",
        "consttypmod",
        "location",
        "xpr",
    ]
    skipped_zero = [
        "constisnull",
    ]

    lookup_consttype = oid_to_type


class PathTarget(PgObject):
    skipped_fields = ["cost", "type", "width"]


class TargetEntry(PgObject):
    skipped_fields = ["resorigcol", "resorigtbl", "type", "xpr"]
    skipped_zero = ["resjunk", "ressortgroupref"]


class FuncExpr(PgObject):
    prefix = "func"
    skipped_fields = [
        "funcformat",
        "funcvariadic",
        "funcretset",
        "funccollid",
        "inputcollid",
        "location",
        "xpr",
    ]

    lookup_funcid = oid_to_proc
    lookup_funcresulttype = oid_to_type


class Var(PgObject):
    prefix = "var"
    skipped_fields = ["varnosyn", "varattnosyn", "vartypmod", "location", "xpr"]
    skipped_zero = ["varcollid", "varlevelsup"]

    lookup_vartype = oid_to_type
    lookup_varno = varno_to_name


class BoolExpr(PgObject):
    skipped_fields = ["location", "xpr"]


class OpExpr(PgObject):
    prefix = "op"
    skipped_fields = [
        "opfuncid",
        "opresulttype",
        "inputcollid",
        "opcollid",
        "opretset",
        "xpr",
    ]

    lookup_opno = oid_to_operator
    lookup_opfuncid = oid_to_proc
    lookup_opresulttype = oid_to_type


class ScalarArrayOpExpr(PgObject):
    skipped_fields = ["inputcollid", "location", "xpr"]


class ArrayExpr(PgObject):
    skipped_fields = ["array_collid", "location", "xpr"]

    lookup_array_typeid = oid_to_type
    lookup_element_typeid = oid_to_type


def register_printers():
    pp = RegexpCollectionPrettyPrinter("postgresql")

    for (name, cls) in Registry.printers.items():
        pp.add_printer(name, "^{}$".format(name), cls)

    return pp


gdb.printing.register_pretty_printer(None, register_printers(), True)
