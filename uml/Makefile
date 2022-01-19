.DEFAULT_GOAL := all

all:

sync:
	@echo ~/examples/uml/
	@rsync -r -t -u -v --delete            \
    --exclude "*"                          \
    ~/examples/uml/ .
