
# oids < 10000 are assigned statically by postgres so might as well include them all
# dictionary is produces by following query:
# select '{' || string_agg(format('%s:"%s"',oid,oprcode),',' ORDER BY oid) || '}' from pg_operator WHERE oid < 10000;
REGOPERATOR_ASSIGNED = {15:"int48eq",36:"int48ne",37:"int48lt",58:"boollt",59:"boolgt",76:"int48gt",80:"int48le",82:"int48ge",85:"boolne",91:"booleq",92:"chareq",93:"nameeq",94:"int2eq",95:"int2lt",96:"int4eq",97:"int4lt",98:"texteq",254:"nameeqtext",255:"namelttext",256:"nameletext",257:"namegetext",258:"namegttext",259:"namenetext",260:"texteqname",261:"textltname",262:"textlename",263:"textgename",264:"textgtname",265:"textnename",349:"array_append",352:"xideq",353:"xideqint4",374:"array_prepend",375:"array_cat",385:"cideq",387:"tideq",402:"tidne",410:"int8eq",411:"int8ne",412:"int8lt",413:"int8gt",414:"int8le",415:"int8ge",416:"int84eq",417:"int84ne",418:"int84lt",419:"int84gt",420:"int84le",430:"int84ge",433:"box_contain_pt",439:"int8mod",473:"int8abs",484:"int8um",485:"poly_left",486:"poly_overleft",487:"poly_overright",488:"poly_right",489:"poly_contained",490:"poly_contain",491:"poly_same",492:"poly_overlap",493:"box_left",494:"box_overleft",495:"box_overright",496:"box_right",497:"box_contained",498:"box_contain",499:"box_same",500:"box_overlap",501:"box_ge",502:"box_gt",503:"box_eq",504:"box_lt",505:"box_le",506:"point_above",507:"point_left",508:"point_right",509:"point_below",510:"point_eq",511:"on_pb",512:"on_ppath",513:"box_center",514:"int4mul",517:"point_distance",518:"int4ne",519:"int2ne",520:"int2gt",521:"int4gt",522:"int2le",523:"int4le",524:"int2ge",525:"int4ge",526:"int2mul",527:"int2div",528:"int4div",529:"int2mod",530:"int4mod",531:"textne",532:"int24eq",533:"int42eq",534:"int24lt",535:"int42lt",536:"int24gt",537:"int42gt",538:"int24ne",539:"int42ne",540:"int24le",541:"int42le",542:"int24ge",543:"int42ge",544:"int24mul",545:"int42mul",546:"int24div",547:"int42div",550:"int2pl",551:"int4pl",552:"int24pl",553:"int42pl",554:"int2mi",555:"int4mi",556:"int24mi",557:"int42mi",558:"int4um",559:"int2um",584:"float4um",585:"float8um",586:"float4pl",587:"float4mi",588:"float4div",589:"float4mul",590:"float4abs",591:"float8pl",592:"float8mi",593:"float8div",594:"float8mul",595:"float8abs",596:"dsqrt",597:"dcbrt",606:"dist_bp",607:"oideq",608:"oidne",609:"oidlt",610:"oidgt",611:"oidle",612:"oidge",613:"dist_pl",614:"dist_ps",615:"dist_pb",616:"dist_sl",617:"dist_sb",618:"dist_ppath",620:"float4eq",621:"float4ne",622:"float4lt",623:"float4gt",624:"float4le",625:"float4ge",630:"charne",631:"charlt",632:"charle",633:"chargt",634:"charge",639:"nameregexeq",640:"nameregexne",641:"textregexeq",642:"textregexne",643:"namene",644:"oidvectorne",645:"oidvectorlt",646:"oidvectorgt",647:"oidvectorle",648:"oidvectorge",649:"oidvectoreq",654:"textcat",660:"namelt",661:"namele",662:"namegt",663:"namege",664:"text_lt",665:"text_le",666:"text_gt",667:"text_ge",670:"float8eq",671:"float8ne",672:"float8lt",673:"float8le",674:"float8gt",675:"float8ge",682:"int2abs",684:"int8pl",685:"int8mi",686:"int8mul",687:"int8div",688:"int84pl",689:"int84mi",690:"int84mul",691:"int84div",692:"int48pl",693:"int48mi",694:"int48mul",695:"int48div",706:"box_distance",707:"path_distance",708:"line_distance",709:"lseg_distance",712:"poly_distance",713:"point_ne",731:"point_add",732:"point_sub",733:"point_mul",734:"point_div",735:"path_add",736:"path_add_pt",737:"path_sub_pt",738:"path_mul_pt",739:"path_div_pt",755:"path_contain_pt",756:"pt_contained_poly",757:"poly_contain_pt",758:"pt_contained_circle",759:"circle_contain_pt",760:"dist_lp",761:"dist_sp",762:"dist_ls",763:"dist_bs",773:"int4abs",784:"dist_pathp",792:"path_n_eq",793:"path_n_lt",794:"path_n_gt",795:"path_n_le",796:"path_n_ge",797:"path_npoints",798:"path_inter",799:"path_length",800:"box_above_eq",801:"box_below_eq",802:"box_overlap",803:"box_intersect",804:"box_add",805:"box_sub",806:"box_mul",807:"box_div",808:"point_horiz",809:"point_vert",818:"int82pl",819:"int82mi",820:"int82mul",821:"int82div",822:"int28pl",823:"int28mi",824:"int28mul",825:"int28div",843:"cash_mul_flt4",844:"cash_div_flt4",845:"flt4_mul_cash",900:"cash_eq",901:"cash_ne",902:"cash_lt",903:"cash_gt",904:"cash_le",905:"cash_ge",906:"cash_pl",907:"cash_mi",908:"cash_mul_flt8",909:"cash_div_flt8",912:"cash_mul_int4",913:"cash_div_int4",914:"cash_mul_int2",915:"cash_div_int2",916:"flt8_mul_cash",917:"int4_mul_cash",918:"int2_mul_cash",931:"network_sub",932:"network_subeq",933:"network_sup",934:"network_supeq",965:"dpow",966:"aclinsert",967:"aclremove",968:"aclcontains",969:"lseg_center",970:"path_center",971:"poly_center",974:"aclitemeq",1038:"numeric_power",1054:"bpchareq",1055:"bpcharregexeq",1056:"bpcharregexne",1057:"bpcharne",1058:"bpcharlt",1059:"bpcharle",1060:"bpchargt",1061:"bpcharge",1070:"array_eq",1071:"array_ne",1072:"array_lt",1073:"array_gt",1074:"array_le",1075:"array_ge",1076:"date_pl_interval",1077:"date_mi_interval",1093:"date_eq",1094:"date_ne",1095:"date_lt",1096:"date_le",1097:"date_gt",1098:"date_ge",1099:"date_mi",1100:"date_pli",1101:"date_mii",1108:"time_eq",1109:"time_ne",1110:"time_lt",1111:"time_le",1112:"time_gt",1113:"time_ge",1116:"float48pl",1117:"float48mi",1118:"float48div",1119:"float48mul",1120:"float48eq",1121:"float48ne",1122:"float48lt",1123:"float48gt",1124:"float48le",1125:"float48ge",1126:"float84pl",1127:"float84mi",1128:"float84div",1129:"float84mul",1130:"float84eq",1131:"float84ne",1132:"float84lt",1133:"float84gt",1134:"float84le",1135:"float84ge",1201:"network_eq",1202:"network_ne",1203:"network_lt",1204:"network_le",1205:"network_gt",1206:"network_ge",1207:"namelike",1208:"namenlike",1209:"textlike",1210:"textnlike",1211:"bpcharlike",1212:"bpcharnlike",1220:"macaddr_eq",1221:"macaddr_ne",1222:"macaddr_lt",1223:"macaddr_le",1224:"macaddr_gt",1225:"macaddr_ge",1226:"nameicregexeq",1227:"nameicregexne",1228:"texticregexeq",1229:"texticregexne",1234:"bpcharicregexeq",1235:"bpcharicregexne",1320:"timestamptz_eq",1321:"timestamptz_ne",1322:"timestamptz_lt",1323:"timestamptz_le",1324:"timestamptz_gt",1325:"timestamptz_ge",1327:"timestamptz_pl_interval",1328:"timestamptz_mi",1329:"timestamptz_mi_interval",1330:"interval_eq",1331:"interval_ne",1332:"interval_lt",1333:"interval_le",1334:"interval_gt",1335:"interval_ge",1336:"interval_um",1337:"interval_pl",1338:"interval_mi",1360:"datetime_pl",1361:"datetimetz_pl",1363:"timedate_pl",1366:"timetzdate_pl",1382:"dist_bl",1383:"dist_polyc",1399:"time_mi_time",1420:"circle_center",1500:"circle_eq",1501:"circle_ne",1502:"circle_lt",1503:"circle_gt",1504:"circle_le",1505:"circle_ge",1506:"circle_left",1507:"circle_overleft",1508:"circle_overright",1509:"circle_right",1510:"circle_contained",1511:"circle_contain",1512:"circle_same",1513:"circle_overlap",1514:"circle_above",1515:"circle_below",1516:"circle_add_pt",1517:"circle_sub_pt",1518:"circle_mul_pt",1519:"circle_div_pt",1520:"circle_distance",1521:"poly_npoints",1522:"dist_pc",1523:"dist_cpoly",1524:"dist_lb",1525:"lseg_intersect",1526:"lseg_parallel",1527:"lseg_perp",1528:"lseg_horizontal",1529:"lseg_vertical",1535:"lseg_eq",1536:"lseg_interpt",1537:"inter_sl",1538:"inter_sb",1539:"inter_lb",1546:"on_pl",1547:"on_ps",1548:"on_sl",1549:"on_sb",1550:"timetz_eq",1551:"timetz_ne",1552:"timetz_lt",1553:"timetz_le",1554:"timetz_gt",1555:"timetz_ge",1557:"close_pl",1558:"close_ps",1559:"close_pb",1566:"close_sl",1567:"close_sb",1568:"close_lb",1577:"close_ls",1578:"close_lseg",1583:"interval_mul",1584:"mul_d_interval",1585:"interval_div",1586:"lseg_ne",1587:"lseg_lt",1588:"lseg_le",1589:"lseg_gt",1590:"lseg_ge",1591:"lseg_length",1611:"line_intersect",1612:"line_parallel",1613:"line_perp",1614:"line_horizontal",1615:"line_vertical",1616:"line_eq",1617:"line_interpt",1625:"nameiclike",1626:"nameicnlike",1627:"texticlike",1628:"texticnlike",1629:"bpchariclike",1630:"bpcharicnlike",1694:"boolle",1695:"boolge",1751:"numeric_uminus",1752:"numeric_eq",1753:"numeric_ne",1754:"numeric_lt",1755:"numeric_le",1756:"numeric_gt",1757:"numeric_ge",1758:"numeric_add",1759:"numeric_sub",1760:"numeric_mul",1761:"numeric_div",1762:"numeric_mod",1763:"numeric_abs",1784:"biteq",1785:"bitne",1786:"bitlt",1787:"bitgt",1788:"bitle",1789:"bitge",1791:"bitand",1792:"bitor",1793:"bitxor",1794:"bitnot",1795:"bitshiftleft",1796:"bitshiftright",1797:"bitcat",1800:"time_pl_interval",1801:"time_mi_interval",1802:"timetz_pl_interval",1803:"timetz_mi_interval",1804:"varbiteq",1805:"varbitne",1806:"varbitlt",1807:"varbitgt",1808:"varbitle",1809:"varbitge",1849:"interval_pl_time",1862:"int28eq",1863:"int28ne",1864:"int28lt",1865:"int28gt",1866:"int28le",1867:"int28ge",1868:"int82eq",1869:"int82ne",1870:"int82lt",1871:"int82gt",1872:"int82le",1873:"int82ge",1874:"int2and",1875:"int2or",1876:"int2xor",1877:"int2not",1878:"int2shl",1879:"int2shr",1880:"int4and",1881:"int4or",1882:"int4xor",1883:"int4not",1884:"int4shl",1885:"int4shr",1886:"int8and",1887:"int8or",1888:"int8xor",1889:"int8not",1890:"int8shl",1891:"int8shr",1916:"int8up",1917:"int2up",1918:"int4up",1919:"float4up",1920:"float8up",1921:"numeric_uplus",1955:"byteaeq",1956:"byteane",1957:"bytealt",1958:"byteale",1959:"byteagt",1960:"byteage",2016:"bytealike",2017:"byteanlike",2018:"byteacat",2060:"timestamp_eq",2061:"timestamp_ne",2062:"timestamp_lt",2063:"timestamp_le",2064:"timestamp_gt",2065:"timestamp_ge",2066:"timestamp_pl_interval",2067:"timestamp_mi",2068:"timestamp_mi_interval",2314:"text_pattern_lt",2315:"text_pattern_le",2317:"text_pattern_ge",2318:"text_pattern_gt",2326:"bpchar_pattern_lt",2327:"bpchar_pattern_le",2329:"bpchar_pattern_ge",2330:"bpchar_pattern_gt",2345:"date_lt_timestamp",2346:"date_le_timestamp",2347:"date_eq_timestamp",2348:"date_ge_timestamp",2349:"date_gt_timestamp",2350:"date_ne_timestamp",2358:"date_lt_timestamptz",2359:"date_le_timestamptz",2360:"date_eq_timestamptz",2361:"date_ge_timestamptz",2362:"date_gt_timestamptz",2363:"date_ne_timestamptz",2371:"timestamp_lt_date",2372:"timestamp_le_date",2373:"timestamp_eq_date",2374:"timestamp_ge_date",2375:"timestamp_gt_date",2376:"timestamp_ne_date",2384:"timestamptz_lt_date",2385:"timestamptz_le_date",2386:"timestamptz_eq_date",2387:"timestamptz_ge_date",2388:"timestamptz_gt_date",2389:"timestamptz_ne_date",2534:"timestamp_lt_timestamptz",2535:"timestamp_le_timestamptz",2536:"timestamp_eq_timestamptz",2537:"timestamp_ge_timestamptz",2538:"timestamp_gt_timestamptz",2539:"timestamp_ne_timestamptz",2540:"timestamptz_lt_timestamp",2541:"timestamptz_le_timestamp",2542:"timestamptz_eq_timestamp",2543:"timestamptz_ge_timestamp",2544:"timestamptz_gt_timestamp",2545:"timestamptz_ne_timestamp",2551:"interval_pl_date",2552:"interval_pl_timetz",2553:"interval_pl_timestamp",2554:"interval_pl_timestamptz",2555:"integer_pl_date",2570:"box_below",2571:"box_overbelow",2572:"box_overabove",2573:"box_above",2574:"poly_below",2575:"poly_overbelow",2576:"poly_overabove",2577:"poly_above",2589:"circle_overbelow",2590:"circle_overabove",2634:"inetnot",2635:"inetand",2636:"inetor",2637:"inetpl",2638:"int8pl_inet",2639:"inetmi_int8",2640:"inetmi",2750:"arrayoverlap",2751:"arraycontains",2752:"arraycontained",2779:"textanycat",2780:"anytextcat",2799:"tidlt",2800:"tidgt",2801:"tidle",2802:"tidge",2860:"multirange_eq",2861:"multirange_ne",2862:"multirange_lt",2863:"multirange_le",2864:"multirange_ge",2865:"multirange_gt",2866:"range_overlaps_multirange",2867:"multirange_overlaps_range",2868:"multirange_overlaps_multirange",2869:"multirange_contains_elem",2870:"multirange_contains_range",2871:"multirange_contains_multirange",2872:"elem_contained_by_multirange",2873:"range_contained_by_multirange",2874:"multirange_contained_by_multirange",2875:"range_overleft_multirange",2876:"multirange_overleft_range",2877:"multirange_overleft_multirange",2972:"uuid_eq",2973:"uuid_ne",2974:"uuid_lt",2975:"uuid_gt",2976:"uuid_le",2977:"uuid_ge",2988:"record_eq",2989:"record_ne",2990:"record_lt",2991:"record_gt",2992:"record_le",2993:"record_ge",3147:"macaddr_not",3148:"macaddr_and",3149:"macaddr_or",3188:"record_image_eq",3189:"record_image_ne",3190:"record_image_lt",3191:"record_image_gt",3192:"record_image_le",3193:"record_image_ge",3206:"jsonb_extract_path_text",3211:"jsonb_object_field",3212:"jsonb_array_element",3213:"jsonb_extract_path",3222:"pg_lsn_eq",3223:"pg_lsn_ne",3224:"pg_lsn_lt",3225:"pg_lsn_gt",3226:"pg_lsn_le",3227:"pg_lsn_ge",3228:"pg_lsn_mi",3240:"jsonb_eq",3241:"jsonb_ne",3242:"jsonb_lt",3243:"jsonb_gt",3244:"jsonb_le",3245:"jsonb_ge",3246:"jsonb_contains",3247:"jsonb_exists",3248:"jsonb_exists_any",3249:"jsonb_exists_all",3250:"jsonb_contained",3276:"dist_ppoly",3284:"jsonb_concat",3285:"pg_catalog.jsonb_delete",3286:"pg_catalog.jsonb_delete",3287:"jsonb_delete_path",3289:"dist_polyp",3291:"dist_cpoint",3315:"xidneq",3316:"xidneqint4",3346:"cash_mul_int8",3347:"cash_div_int8",3349:"int8_mul_cash",3362:"macaddr8_eq",3363:"macaddr8_ne",3364:"macaddr8_lt",3365:"macaddr8_le",3366:"macaddr8_gt",3367:"macaddr8_ge",3368:"macaddr8_not",3369:"macaddr8_and",3370:"macaddr8_or",3398:"pg_catalog.jsonb_delete",3477:"jsonb_object_field_text",3481:"jsonb_array_element_text",3516:"enum_eq",3517:"enum_ne",3518:"enum_lt",3519:"enum_gt",3520:"enum_le",3521:"enum_ge",3552:"network_overlap",3585:"range_overright_multirange",3627:"tsvector_lt",3628:"tsvector_le",3629:"tsvector_eq",3630:"tsvector_ne",3631:"tsvector_ge",3632:"tsvector_gt",3633:"tsvector_concat",3636:"ts_match_vq",3637:"ts_match_qv",3660:"ts_match_vq",3661:"ts_match_qv",3674:"tsquery_lt",3675:"tsquery_le",3676:"tsquery_eq",3677:"tsquery_ne",3678:"tsquery_ge",3679:"tsquery_gt",3680:"tsquery_and",3681:"tsquery_or",3682:"tsquery_not",3693:"tsq_mcontains",3694:"tsq_mcontained",3762:"ts_match_tt",3763:"ts_match_tq",3825:"cash_div_cash",3877:"starts_with",3882:"range_eq",3883:"range_ne",3884:"range_lt",3885:"range_le",3886:"range_ge",3887:"range_gt",3888:"range_overlaps",3889:"range_contains_elem",3890:"range_contains",3891:"elem_contained_by_range",3892:"range_contained_by",3893:"range_before",3894:"range_after",3895:"range_overleft",3896:"range_overright",3897:"range_adjacent",3898:"range_union",3899:"range_minus",3900:"range_intersect",3962:"json_object_field",3963:"json_object_field_text",3964:"json_array_element",3965:"json_array_element_text",3966:"json_extract_path",3967:"json_extract_path_text",4012:"jsonb_path_exists_opr",4013:"jsonb_path_match_opr",4035:"multirange_overright_range",4142:"multirange_overright_multirange",4161:"point_above",4162:"point_below",4179:"range_adjacent_multirange",4180:"multirange_adjacent_range",4198:"multirange_adjacent_multirange",4392:"multirange_union",4393:"multirange_minus",4394:"multirange_intersect",4395:"range_before_multirange",4396:"multirange_before_range",4397:"multirange_before_multirange",4398:"range_after_multirange",4399:"multirange_after_range",4400:"multirange_after_multirange",4539:"range_contains_multirange",4540:"multirange_contained_by_range",5005:"pg_catalog.tsquery_phrase",5025:"pg_lsn_pli",5026:"numeric_pl_pg_lsn",5027:"pg_lsn_mii",5068:"xid8eq",5072:"xid8ne",5073:"xid8lt",5074:"xid8gt",5075:"xid8le",5076:"xid8ge"}
