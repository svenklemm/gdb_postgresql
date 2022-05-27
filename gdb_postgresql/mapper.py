
from gdb_postgresql.constants.regtype import REGTYPE_ASSIGNED
from gdb_postgresql.constants.regoperator import REGOPERATOR_ASSIGNED
from gdb_postgresql.constants.regproc import REGPROC_ASSIGNED

def oid_to_type(self, oid):
  # type oids < 10000 are assigned statically by postgres so might as well include them all
  # dictionary is produces by following query:
  # select '{' || string_agg(format('%s:"%s"',oid,typname),',' ORDER BY oid) || '}' from pg_type WHERE oid < 10000;

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

