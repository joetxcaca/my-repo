# -----------
# Wed,  2 Feb
# -----------

"""
Class Modality
	online until further notice

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
	5.9.3
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

Grades Tracker Google Sheet
	https://docs.google.com/spreadsheets/d/1kLH8yXozudQh3VktnAl5GqTNXgRFQ6Bs0bqfO0uRqck/

Virtual Token Google Form
	https://forms.gle/evXiWYUc6wqHzffb6
"""

"""
cold calling
specifications grading
huge disconnect between lectures and Web project
"""

"""
Paper #03: 2022-02-06: Continuous Integration
you MUST go to Perusall THROUGH Canvas
"""

"""
Project #1: Collatz
Poll: Project #1: Collatz
Academic Integrity Quiz

Add
SHELL := /bin/bash
to the Makefile.
"""

"""
first exercise
on HackerRank
I will give you a URL
I will give you a password

1. e-mail (any e-mail)
2. password (I will provide)
3. name (all the names of all of the students)
4. EID  (all the EIDs  of all of the students)

breakout rooms
1. ONE of you to volunteer to drive
	SHARE their screen and do all the typing
	ask for help
	submit the solution
2. Please turn ON your video
3. Everyone please collaborate

Before you submit ask for one of us to visit your room and ok the code
"""

#!/usr/bin/env python3

# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# -----------
# IsPrimeH.py
# -----------

import math

def is_prime (n: int) -> bool :
    assert n > 0
    if (n == 2)
    	return True
    if (n == 1) or ((n % 2) == 0) :
        return False
    for i in range(3, int(math.sqrt(n) + 1), 2) :
        if (n % i) == 0 :
            return False
    return True

def test0 () :
    assert not is_prime(1)

def test1 () :
    assert is_prime(2) # broken

def test2 () :
    assert is_prime(3)

def test3 () :
    assert not is_prime(4)

def test4 () :
    assert is_prime(5)

def test5 () :
    assert is_prime(7)

def test6 () :
    assert not is_prime(9) # broken

def test7 () :
    assert not is_prime(27)

def test8 () :
    assert is_prime(29)

"""
broken tests can hide broken code
"""

"""
1. run the code as is, confirm success
2. identify and remember and fix the broken tests
3. run the code again, confirm failure
4. identify and remember and fix the broken code
5. run the code again, confirm success
"""

https://hr.gs/cs373-spring-2022-is-prime
1234
