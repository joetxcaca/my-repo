# -----------
# Fri, 21 Jan
# -----------

"""
Class Modality
	first two weeks on Zoom, you're welcome to go to physical room (PAR 301)

Cold Calling
	you're only called ONCE per rotation
	it's totally fine to not know the answer, the idea is to discuss and to learn

Lectures (you must attend your lecture)
	MWF 10 am, Anshul, Vaishnav
	MWF 11 am, Alex,   Mengning

Help Sessions
	T  6-8 pm, Anshul, Vaishnav
	Th 6-8 pm, Alex, Mengning

Office Hours
	Glenn Downing
		Th 3-4 pm, Zoom

	Alex Zuzow (grad, '23)
		T 12-1 pm, Zoom

	Anshul Modh (undergrad, '22)
		Th 11-12 pm, Zoom

	Mengning (grad, '22)
		W 1-2 pm, Zoom

	Vaishnav Bipin (undergrad, '23)
		M 4-5 pm, Zoom

Canvas
	personal questions
	please message all 5 of us

CATME, peer assessment platform
	create student groups (you have no control who you will be with)
	peer review
	4 group Web projects

Ed Discussion (EdStem), replaces Piazza
	class questions
	ask and answer questions
	please be proactive

GitLab, like GitHub, do a git clone, later git pull, on	 a regular basis
	notes
	examples
	exercises

HackerRank, competitive programming platform
	exercises

Perusall, collaborative annotation tool (always go to Perusall via Canvas)
	annotate a series of papers
	the first one will be the syllabus

Zoom
	5.9.1
	must use UT EID credentials (@eid.utexas.edu)
	classes recorded
	published later that day

Specifications Grading
	please ask about this if you don't undestand it
	please use the Google Sheet that we're providing to track your grades

Website
	https://www.cs.utexas.edu/users/downing/cs373/Schedule.html

Discord
	https://discord.gg/xeRT5mqPaG
"""

"""
Calendar: office hours
Discord: please change your server name to your full name
Perusall: syllabus assignment (answer questions)

there is a HUGE disconnect between what we do in lecture and the WEB project
"""

"""
for software development you need access to a tool chain
Python tool chain
	python
	pydoc,         auto documentation
	black,         auto formatting tool
	coverage,      coverage tool
	pylint,        static analyzer
	checktestdata, verifier of input files
"""

"""
to get a tool chain
	1. install the tools on your machine
	2. ssh into the CS machines
	3. use Docker
"""

"""
P1
	optionally use my docker image
P2, P3, P4, P5
	required to create TWO Docker images (backend, frontend)
"""

https://hub.docker.com/r/gpdowning/python/



% which docker
/usr/local/bin/docker



% docker --version
Docker version 20.10.12, build e91ed57



% docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE



% cat Dockerfile
FROM python

RUN apt-get update

RUN apt-get -y install dos2unix
RUN apt-get -y install libboost-dev
RUN apt-get -y install libgmp-dev
RUN apt-get -y install vim

RUN pip install --upgrade pip
RUN pip --version

RUN pip install black    # auto formatter
RUN pip install coverage
RUN pip install mypy     # type annotator
RUN pip install numpy    # numerical analysis
RUN pip install pylint   # static analyzer

RUN git clone https://github.com/DOMjudge/checktestdata checktestdata && \
    cd checktestdata                                                  && \
    git checkout release                                              && \
    ./bootstrap                                                       && \
    make                                                              && \
    cp checktestdata /usr/bin                                         && \
    cd -

CMD bash



% docker build -t gpdowning/python .
...



% docker login
...



% docker push gpdowning/python
...



% docker pull gpdowning/python
...



% docker images
REPOSITORY         TAG       IMAGE ID       CREATED          SIZE
gpdowning/python   latest    149abb40cecd   15 minutes ago   1.34GB
python             latest    cecf555903c6   2 days ago       917MB




% pwd
/Users/downing/git/cs373/python



% ls
Assertions.py	Dockerfile	Hello.py	Script.txt	makefile



% docker run --rm -i -t -v /Users/downing/git/cs373/python:/usr/python -w /usr/python gpdowning/python
root@a4fe84a658f0:/usr/python# pwd
/usr/python



root@a4fe84a658f0:/usr/python# ls
Assertions.py	Dockerfile	Hello.py	Script.txt	makefile



root@a4fe84a658f0:/usr/python# which black
/usr/local/bin/black
root@a4fe84a658f0:/usr/python# black --version
black, 21.12b0 (compiled: no)



root@a4fe84a658f0:/usr/gcc# which checktestdata
/usr/bin/checktestdata
root@c70871d08248:/usr/gcc# checktestdata --version
checktestdata -- version 20220121, written by Jan Kuipers, Jaap Eldering, Tobias Werth



root@a4fe84a658f0:/usr/python# which coverage
/usr/local/bin/coverage
root@a4fe84a658f0:/usr/python# coverage --version
Coverage.py, version 6.2 with C extension



root@a4fe84a658f0:/usr/python# which git
/usr/bin/git
root@a4fe84a658f0:/usr/python# git --version
git version 2.30.2



root@a4fe84a658f0:/usr/python# which make
/usr/bin/make
root@a4fe84a658f0:/usr/python# make --version
GNU Make 4.3



root@a4fe84a658f0:/usr/python# which mypy
/usr/local/bin/mypy
root@a4fe84a658f0:/usr/python# mypy --version
mypy 0.931



root@a4fe84a658f0:/usr/python# which pip
/usr/local/bin/pip
root@a4fe84a658f0:/usr/python# pip --version
pip 21.3.1 from /usr/local/lib/python3.10/site-packages/pip (python 3.10)



root@a4fe84a658f0:/usr/python# which pydoc
/usr/local/bin/pydoc
root@a4fe84a658f0:/usr/python# pydoc --version
...



root@a4fe84a658f0:/usr/python# which pylint
/usr/local/bin/pylint
root@a4fe84a658f0:/usr/python# pylint --version
pylint 2.12.2



root@a4fe84a658f0:/usr/python# which python
/usr/local/bin/python
root@a4fe84a658f0:/usr/python# python --version
Python 3.10.2



root@a4fe84a658f0:/usr/python# which vim
/usr/bin/vim
root@a4fe84a658f0:/usr/python# vim --version
VIM - Vi IMproved 8.2 (2019 Dec 12, compiled Oct 01 2021 01:51:08)
