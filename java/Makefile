.DEFAULT_GOAL := all

FILES :=                    \
    Hello                   \
    StrategyPattern1        \
    StrategyPattern2        \
    StrategyPattern3        \
    StrategyPattern4        \
    StrategyPattern5        \
    StrategyPattern6        \
    StrategyPattern8

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
    --include "StrategyPattern3.java"      \
    --include "StrategyPattern4.java"      \
    --include "StrategyPattern5.java"      \
    --include "StrategyPattern6.java"      \
    --include "StrategyPattern8.java"      \
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
