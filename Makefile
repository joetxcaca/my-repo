.DEFAULT_GOAL := all

all:

clean:
	cd java; make --no-print-directory clean
	@echo
	cd python; make --no-print-directory clean

config:
	git config -l

init:
	git init
	git remote add origin git@gitlab.com:gpdowning/cs373.git
	git add README.md
	git commit -m 'first commit'
	git push -u origin master

pull:
	make --no-print-directory clean
	@echo
	git pull
	git status

push:
	make --no-print-directory clean
	@echo
	git add .gitignore
	git add .gitlab-ci.yml
	git add java
	git add Makefile
	git add notes
	git add python
	git add README.md
	git add sql
	git add uml
	git commit -m "another commit"
	git push
	git status

status:
	make --no-print-directory clean
	@echo
	git branch
	git remote -v
	git status

sync:
	cd java; make --no-print-directory sync
	@echo
	cd python; make --no-print-directory sync
	@echo
	cd sql; make --no-print-directory sync
	@echo
	cd uml; make --no-print-directory sync

versions:
	cd java; make --no-print-directory versions
	@echo
	cd python; make --no-print-directory versions
