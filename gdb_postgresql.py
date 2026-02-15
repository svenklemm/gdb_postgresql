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

class PlannerInfo(PgObject):
    skipped_zero = [
        "parse",
        "glob",
        "parent_root",
        "plan_params",
        "outer_params",
        "simple_rel_array",
        "simple_rel_array_size",
        "simple_rte_array",
        "append_rel_array",
        "all_baserels",
        "outer_join_rels",
        "all_query_rels",
        "join_rel_list",
        "join_rel_hash",
        "join_rel_level",
        "join_cur_level",
        "init_plans",
        "cte_plan_ids",
        "multiexpr_params",
        "join_domains",
        "eq_classes",
        "ec_merging_done",
        "canon_pathkeys",
        "left_join_clauses",
        "right_join_clauses",
        "full_join_clauses",
        "join_info_list",
        "last_rinfo_serial",
        "all_result_relids",
        "leaf_result_relids",
        "append_rel_list",
        "row_identity_vars",
        "rowMarks",
        "placeholder_list",
        "placeholder_array",
        "placeholder_array_size",
        "fkey_list",
        "query_pathkeys",
        "group_pathkeys",
        "num_groupby_pathkeys",
        "window_pathkeys",
        "distinct_pathkeys",
        "sort_pathkeys",
        "setop_pathkeys",
        "part_schemes",
        "initial_rels",
        "upper_rels",
        "upper_targets",
        "processed_groupClause",
        "processed_distinctClause",
        "processed_tlist",
        "update_colnos",
        "grouping_map",
        "minmax_aggs",
        "planner_cxt",
        "total_table_pages",
        "tuple_fraction",
        "limit_tuples",
        "qual_security_level",
        "hasJoinRTEs",
        "hasLateralRTEs",
        "hasHavingQual",
        "hasPseudoConstantQuals",
        "hasAlternativeSubPlans",
        "placeholdersFrozen",
        "hasRecursion",
        "agginfos",
        "aggtransinfos",
        "numOrderedAggs",
        "hasNonPartialAggs",
        "hasNonSerialAggs",
        "wt_param_id",
        "non_recursive_path",
        "curOuterRels",
        "curOuterParams",
        "isAltSubplan",
        "isUsedSubplan",
        "join_search_private",
        "partColsUpdated",
    ]

class NameData():
    def __init__(self, val):
        if not hasattr(self.__class__, "typename"):
            self.typename = self.__class__.__name__

        self.pgtype = gdb.lookup_type(self.typename)

        self.val = val.cast(self.pgtype)

    def to_string(self):
        return str(self.val['data']).replace('\\000','')

Registry.printers["nameData"] = NameData

class Expr(Node):
    pass

class Aggref(PgObject):
    prefix = "agg"
    skipped_fields = ["xpr"]
    lookup_aggfnoid = oid_to_proc
    lookup_aggresulttype = oid_to_type
    lookup_aggtranstype = oid_to_type
    lookup_aggtype = oid_to_type
    skipped_zero = [
        "aggcollid",
        "inputcollid",
        "agglevelsup",
        "aggpresorted",
        "aggstar",
        "aggvariadic",
    ]

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

class SortGroupClause(PgObject):
    skipped_fields = ["eqop", "hashable", "nulls_first", "type"]

    lookup_eqop = oid_to_operator
    lookup_sortop = oid_to_operator

def register_printers():
    pp = RegexpCollectionPrettyPrinter("postgresql")

    for (name, cls) in Registry.printers.items():
        pp.add_printer(name, "^{}$".format(name), cls)

    return pp


gdb.printing.register_pretty_printer(None, register_printers(), True)
