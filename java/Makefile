.DEFAULT_GOAL := all

FILES :=                    \
    Hello

%.class: %.java
	javac -Xlint $<

%.javax: %.class
	java -ea $(patsubst %.class,%,$<)

all: $(FILES:=.class)

clean:
	rm -f *.class

docker:
	docker run -it -v $(PWD):/usr/java -w /usr/java gpdowning/java

run: $(FILES:=.javax)

sync:
	make clean
	@echo ~/examples/java/
	@rsync -r -t -u -v --delete            \
    --include "Hello.java"                 \
    --exclude "*"                          \
    ~/examples/java/ .
	@echo ~/exercises/java/
	@rsync -r -t -u -v --delete            \
    --include "StrategyPattern1.java"      \
    --include "StrategyPattern2.java"      \
    --exclude "*"                          \
    ~/exercises/java/ .

versions:
	@echo "% which java"
	@which java
	@echo
	@echo "% java --version"
	@java --version
	@echo
	@echo "% which javac"
	@which javac
	@echo
	@echo "% javac --version"
	@javac --version
	@echo
	@echo "% which vim"
	@which vim
	@echo
	@echo "% vim --version"
	@vim --version
