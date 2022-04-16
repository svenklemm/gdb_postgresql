
def oid_to_type(self, oid):
  match oid:
    case 16:
      return "bool"
    case 17:
      return "bytea"
    case 18:
      return "char"
    case 19:
      return "name"
    case 20:
      return "int8"
    case 21:
      return "int2"
    case 22:
      return "int2vector"
    case 23:
      return "int4"
    case 25:
      return "text"
    case 26:
      return "oid"
    case 30:
      return "oidvector"
    case 114:
      return "json"
    case 194:
      return "pg_node_tree"
    case 700:
      return "float4"
    case 701:
      return "float8"
    case 1082:
      return "date"
    case 1114:
      return "timestamp"
    case 1184:
      return "timestamptz"
    case 1186:
      return "interval"

    case _:
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

