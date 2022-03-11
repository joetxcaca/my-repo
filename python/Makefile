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
    Hello                   \
    UnitTests1              \
    Coverage1               \
    Coverage2               \
    Coverage3               \
    IsPrimeT                \
    Exceptions              \
    Types                   \
    FactorialT              \
    ReduceT                 \
    Operators               \
    Iteration               \
    Comprehensions          \
    Iterables               \
    Functions

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

run: $(FILES:=.pyx)

sync:
	make clean
	@echo ~/examples/python/
	@rsync -r -t -u -v --delete            \
    --include "Dockerfile"                 \
    --include "Script.txt"                 \
    --include "Hello.py"                   \
    --include "Assertions.py"              \
    --include "UnitTests1.py"              \
    --include "UnitTests2.py"              \
    --include "UnitTests3.py"              \
    --include "Coverage1.py"               \
    --include "Coverage2.py"               \
    --include "Coverage3.py"               \
    --include "Exceptions.py"              \
    --include "Types.py"                   \
    --include "Operators.py"               \
    --include "Iteration.py"               \
    --include "Comprehensions.py"          \
    --include "Iterables.py"               \
    --include "Functions.py"               \
    --exclude "*"                          \
    ~/examples/python/ .
	@echo ~/exercises/python/
	@rsync -r -t -u -v --delete            \
    --include "IsPrimeT.py"                \
    --include "FactorialT.py"              \
    --include "ReduceT.py"                 \
    --include "DigitsIteratorT.py"         \
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
