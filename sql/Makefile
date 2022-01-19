.DEFAULT_GOAL := all

all:

sync:
	@echo ~/examples/sql/
	@rsync -r -t -u -v --delete            \
    --exclude "*"                          \
    ~/examples/sql/ .
	@echo ~/exercises/sql/
	@rsync -r -t -u -v --delete            \
    --exclude "*"                          \
    ~/exercises/sql/ .
