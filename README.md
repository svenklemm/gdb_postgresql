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
