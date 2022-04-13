.DEFAULT_GOAL := all

all:

sync:
	@echo ~/examples/sql/
	@rsync -r -t -u -v --delete            \
    --include "ShowDatabases.sql"          \
    --include "ShowEngines.sql"            \
    --include "CreateDatabase.sql"         \
    --include "CreateTables.sql"           \
    --include "Insert.sql"                 \
    --include "Select.sql"                 \
    --include "Like.sql"                   \
    --exclude "*"                          \
    ~/examples/sql/ .
	@echo ~/exercises/sql/
	@rsync -r -t -u -v --delete            \
    --exclude "*"                          \
    ~/exercises/sql/ .
