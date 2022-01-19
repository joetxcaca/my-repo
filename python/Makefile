.DEFAULT_GOAL := all

ifeq ($(shell uname -s), Darwin)
    BLACK         := black
    CHECKTESTDATA := checktestdata
    COVERAGE      := coverage
    MYPY          := mypy
    PYDOC         := pydoc3
    PYLINT        := pylint
    PYTHON        := python3
else ifeq ($(shell uname -p), unknown)
    BLACK         := black
    CHECKTESTDATA := checktestdata
    COVERAGE      := coverage
    MYPY          := mypy
    PYDOC         := pydoc
    PYLINT        := pylint
    PYTHON        := python
else
    BLACK         := black
    CHECKTESTDATA := checktestdata
    COVERAGE      := coverage
    MYPY          := mypy
    PYDOC         := pydoc3
    PYLINT        := pylint
    PYTHON        := python3
endif

FILES  :=                   \
    Hello

.pylintrc:
	$(PYLINT) --disable=locally-disabled --reports=no --generate-rcfile > $@

%.pyx: %.py .pylintrc
	-$(MYPY)     $<
	-$(PYLINT)   $<
	-$(COVERAGE) run    --branch $<
	-$(COVERAGE) report -m

all:

clean:
	rm -f  .coverage
	rm -f  .pylintrc
	rm -f  *.pyc
	rm -rf __pycache__
	rm -rf .mypy_cache

docker:
	docker run --rm -i -t -v $(PWD):/usr/python -w /usr/python gpdowning/python

run: $(FILES:=.pyx)

sync:
	make clean
	@echo ~/examples/python/
	@rsync -r -t -u -v --delete            \
    --include "Hello.py"                   \
    --exclude "*"                          \
    ~/examples/python/ .
	@echo ~/exercises/python/
	@rsync -r -t -u -v --delete            \
    --exclude "*"                          \
    ~/exercises/python/ .

versions:
	@echo "% which $(BLACK)"
	@which $(BLACK)
	@echo
	@echo "% $(BLACK) --version"
	@$(BLACK) --version
	@echo
	@echo "% which $(CHECKTESTDATA)"
	@which $(CHECKTESTDATA)
	@echo
	@echo "% $(CHECKTESTDATA) --version"
	@$(CHECKTESTDATA) --version
	@echo
	@echo "% which $(COVERAGE)"
	@which $(COVERAGE)
	@echo
	@echo "% $(COVERAGE) --version"
	@$(COVERAGE) --version
	@echo
	@echo "% which git"
	@which git
	@echo
	@echo "% git --version"
	@git --version
	@echo
	@echo "% which make"
	@which make
	@echo
	@echo "% make --version"
	@make --version
	@echo
	@echo "% which $(MYPY)"
	@which $(MYPY)
	@echo
	@echo "% $(MYPY) --version"
	@$(MYPY) --version
	@echo
	@echo "% which pip"
	@which pip
	@echo
	@echo "% pip --version"
	@pip --version
	@echo
	@echo "% which $(PYDOC)"
	@which $(PYDOC)
	@echo
	@echo "% $(PYDOC) --version"
	@$(PYDOC) --version
	@echo
	@echo "% which $(PYLINT)"
	@which $(PYLINT)
	@echo
	@echo "% $(PYLINT) --version"
	@$(PYLINT) --version
	@echo
	@echo "% which $(PYTHON)"
	@which $(PYTHON)
	@echo
	@echo "% $(PYTHON) --version"
	@$(PYTHON) --version
	@echo "% which vim"
	@which vim
	@echo
	@echo "% vim --version"
	@vim --version