# gdb_postgresql

Pretty printer for postgresql internal objects.

## Usage:
To activate in GDB:

`source gdb_postgresql/gdb_postgresql.py`

To disable in GDB:

`disable pretty-printer`

Show information about pretty-printer:

`info pretty-printer`

You may also enable/disable individual pretty-printers.

`disable pretty-printer global postgresql;Const`

## Examples

`(gdb) p *predicate_list`

`$54 = <List <OpExpr no=96, funcid=65, resulttype=bool, args=<List <Var no=2, attno=2, type=int4, levelsup=0>, <Const type=int4, value=1, isnull=false>>>>`

`(gdb) p *rel->baserestrictinfo`

`$53 =
  <List <RestrictInfo clause=<OpExpr no=96, funcid=65, resulttype=bool, args=<List <Var no=1, attno=2, type=int4, levelsup=0>, <Const type=int4, value=1, isnull=false>>>, is_pushed_down=true, outerjoin_delayed=false, can_join=false, pseudoconstant=false, leakproof=false, has_volatile=VOLATILITY_NOVOLATILE, security_level=0, clause_relids=<Bitmapset 1>, required_relids=<Bitmapset 1>, left_relids=<Bitmapset 1>, eval_cost={startup = -1, per_tuple = 0}, norm_selec=-1, outer_selec=-1, mergeopfamilies=<OidList 1976>, left_ec=0x565436482a20, right_ec=0x565436482a20, left_em=0x565436482b10, right_em=0x565436482be8, outer_is_left=false, hashjoinoperator=0, left_bucketsize=-1, right_bucketsize=-1, left_mcvfreq=-1, right_mcvfreq=-1, hasheqoperator=0>>`
