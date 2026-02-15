
format:
	uv tool run black gdb_postgresql

regproc:
	psql postgres -t -A -X -c "select 'REGPROC_ASSIGNED = {' || string_agg(format('%s:\"%s\"',oid,case when prosrc NOT IN ('','aggregate_dummy') AND prosrc NOT LIKE '% %' THEN prosrc ELSE replace(replace(replace(oid::regprocedure::text,'\"',''),' with time zone','tz'),' without time zone','') END),',' ORDER BY oid) || '}' from pg_proc WHERE oid < 10000;" > gdb_postgresql/constants/regproc.py
	uv tool run black gdb_postgresql/constants/regproc.py

