from gdb_postgresql.constants.regtype import REGTYPE_ASSIGNED
from gdb_postgresql.constants.regoperator import REGOPERATOR_ASSIGNED
from gdb_postgresql.constants.regproc import REGPROC_ASSIGNED


def oid_to_type(self, oid):
    # type oids < 10000 are assigned statically by postgres so might as well include them all
    if int(oid) in REGTYPE_ASSIGNED:
        return REGTYPE_ASSIGNED[int(oid)]
    else:
        return str(oid)


def varno_to_name(self, varno):
    match varno:
        case 65000:
            return "INNER_VAR"
        case 65001:
            return "OUTER_VAR"
        case 65002:
            return "INDEX_VAR"
        case 65003:
            return "ROWID_VAR"
        case _:
            return str(varno)


def lockmode_to_name(self, lockmode):
    match lockmode:
        case 0:
            return "NoLock"
        case 1:
            return "AccessShareLock"
        case 2:
            return "RowShareLock"
        case 3:
            return "RowExclusiveLock"
        case 4:
            return "ShareUpdateExclusiveLock"
        case 5:
            return "ShareLock"
        case 6:
            return "ShareRowExclusiveLock"
        case 7:
            return "ExclusiveLock"
        case 8:
            return "AccessExclusiveLock"
        case _:
            return str(lockmode)


def relkind_to_name(self, relkind):
    match chr(relkind):
        case "r":
            return "RELATION"
        case "i":
            return "INDEX"
        case "S":
            return "SEQUENCE"
        case "t":
            return "TOASTVALUE"
        case "v":
            return "VIEW"
        case "m":
            return "MATVIEW"
        case "c":
            return "COMPOSITE_TYPE"
        case "f":
            return "FOREGIN_TABLE"
        case "p":
            return "PARTITIONED_TABLE"
        case "I":
            return "PARTITIONED_INDEX"
        case _:
            return str(relkind)


def oid_to_operator(self, oid):
    if int(oid) in REGOPERATOR_ASSIGNED:
        return REGOPERATOR_ASSIGNED[int(oid)]
    else:
        return str(oid)


def oid_to_proc(self, oid):
    if int(oid) in REGPROC_ASSIGNED:
        return REGPROC_ASSIGNED[int(oid)]
    else:
        return str(oid)
