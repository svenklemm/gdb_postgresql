
def oid_to_type(self, oid):
  # type oids < 10000 are assigned statically by postgres so might as well include them all
  # dictionary is produces by following query:
  # select '{' || string_agg(format('%s:"%s"',oid,typname),',' ORDER BY oid) || '}' from pg_type WHERE oid < 10000;

  assigned_values = {16:"bool",17:"bytea",18:"char",19:"name",20:"int8",21:"int2",22:"int2vector",23:"int4",24:"regproc",25:"text",26:"oid",27:"tid",28:"xid",29:"cid",30:"oidvector",32:"pg_ddl_command",71:"pg_type",75:"pg_attribute",81:"pg_proc",83:"pg_class",114:"json",142:"xml",143:"_xml",194:"pg_node_tree",199:"_json",210:"_pg_type",269:"table_am_handler",270:"_pg_attribute",271:"_xid8",272:"_pg_proc",273:"_pg_class",325:"index_am_handler",600:"point",601:"lseg",602:"path",603:"box",604:"polygon",628:"line",629:"_line",650:"cidr",651:"_cidr",700:"float4",701:"float8",705:"unknown",718:"circle",719:"_circle",774:"macaddr8",775:"_macaddr8",790:"money",791:"_money",829:"macaddr",869:"inet",1000:"_bool",1001:"_bytea",1002:"_char",1003:"_name",1005:"_int2",1006:"_int2vector",1007:"_int4",1008:"_regproc",1009:"_text",1010:"_tid",1011:"_xid",1012:"_cid",1013:"_oidvector",1014:"_bpchar",1015:"_varchar",1016:"_int8",1017:"_point",1018:"_lseg",1019:"_path",1020:"_box",1021:"_float4",1022:"_float8",1027:"_polygon",1028:"_oid",1033:"aclitem",1034:"_aclitem",1040:"_macaddr",1041:"_inet",1042:"bpchar",1043:"varchar",1082:"date",1083:"time",1114:"timestamp",1115:"_timestamp",1182:"_date",1183:"_time",1184:"timestamptz",1185:"_timestamptz",1186:"interval",1187:"_interval",1231:"_numeric",1248:"pg_database",1263:"_cstring",1266:"timetz",1270:"_timetz",1560:"bit",1561:"_bit",1562:"varbit",1563:"_varbit",1700:"numeric",1790:"refcursor",2201:"_refcursor",2202:"regprocedure",2203:"regoper",2204:"regoperator",2205:"regclass",2206:"regtype",2207:"_regprocedure",2208:"_regoper",2209:"_regoperator",2210:"_regclass",2211:"_regtype",2249:"record",2275:"cstring",2276:"any",2277:"anyarray",2278:"void",2279:"trigger",2280:"language_handler",2281:"internal",2283:"anyelement",2287:"_record",2776:"anynonarray",2842:"pg_authid",2843:"pg_auth_members",2949:"_txid_snapshot",2950:"uuid",2951:"_uuid",2970:"txid_snapshot",3115:"fdw_handler",3220:"pg_lsn",3221:"_pg_lsn",3310:"tsm_handler",3361:"pg_ndistinct",3402:"pg_dependencies",3500:"anyenum",3614:"tsvector",3615:"tsquery",3642:"gtsvector",3643:"_tsvector",3644:"_gtsvector",3645:"_tsquery",3734:"regconfig",3735:"_regconfig",3769:"regdictionary",3770:"_regdictionary",3802:"jsonb",3807:"_jsonb",3831:"anyrange",3838:"event_trigger",3904:"int4range",3905:"_int4range",3906:"numrange",3907:"_numrange",3908:"tsrange",3909:"_tsrange",3910:"tstzrange",3911:"_tstzrange",3912:"daterange",3913:"_daterange",3926:"int8range",3927:"_int8range",4066:"pg_shseclabel",4072:"jsonpath",4073:"_jsonpath",4089:"regnamespace",4090:"_regnamespace",4096:"regrole",4097:"_regrole",4191:"regcollation",4192:"_regcollation",4451:"int4multirange",4532:"nummultirange",4533:"tsmultirange",4534:"tstzmultirange",4535:"datemultirange",4536:"int8multirange",4537:"anymultirange",4538:"anycompatiblemultirange",4600:"pg_brin_bloom_summary",4601:"pg_brin_minmax_multi_summary",5017:"pg_mcv_list",5038:"pg_snapshot",5039:"_pg_snapshot",5069:"xid8",5077:"anycompatible",5078:"anycompatiblearray",5079:"anycompatiblenonarray",5080:"anycompatiblerange",6101:"pg_subscription",6150:"_int4multirange",6151:"_nummultirange",6152:"_tsmultirange",6153:"_tstzmultirange",6155:"_datemultirange",6157:"_int8multirange"}

  if int(oid) in assigned_values:
    return assigned_values[int(oid)]
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

