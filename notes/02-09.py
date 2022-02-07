# -----------
# Wed,  9 Feb
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

.gitlab-ci.yml
make run-all
"""

"""
virtual tokens
"""

"""
assertions are not good for user errors
exceptions are
"""

"""
let's pretend we don't have exceptions
as an example C doesn't exceptions
"""

# use the return

def f (...) :
	...
	if (...)
		# something is wrong
		return """special value"""
	...

def g (...) :
	...
	x = f(...)
	if (x == """special value""")
		# do something about it
	...

# use global

h = 0

def f (...) :
	global h
	...
	if (...)
		# something is wrong
		h = """special value"""
		return ...
	...

def g (...) :
	global h
	...
	h = 0
	x = f(...)
	if (h == """special value""")
		# do something about it
	...

# use a parameter, this doesn't work

def f (..., e2) : # e2 is a COPY of e
	...
	if (...)
		# something is wrong
		e2 = """special value"""
		return ...
	...

def g (...) :
	...
	e = 0
	x = f(..., e)
	if (e == """special value""")
		# do something about it
	...

# let's Java
# use a parameter, doesn't work because ints are passed by value (copy)

int f (..., int e2) {} # e2 is a copy of an int
	...
	if (...) {
		# something is wrong
		e2 = """special value"""
		return ...}
	...}

int g (...) {
	...
	int e = 0;
	x = f(..., e);
	if (e == """special value""")
		# do something about it
	...

# let's Java
# use a parameter, still doesn't work, because Integer is immuatable

int f (..., Integer e2) {} # e2 is a copy of a reference (address)
	...
	if (...) {
		# something is wrong
		e2 = """special value""" # this creates a new Integer object
		return ...}
	...}

int g (...) {
	...
	Integer e = 0;              # does this line work? YES, because of boxing
	Integer e = new Integer(0); # e is reference (address) to an Integer object
	x = f(..., e);
	if (e == """special value""")
		# do something about it
	...

# let's Java
# use a parameter

int f (..., int[] e2) {} # e2 is a copy of a reference (address)
	...
	if (...) {
		# something is wrong
		e2    = """special value""" # this creates a new array object
		e2[0] = """special value"""
		return ...}
	...}

int g (...) {
	...
	int[] e = {0}; # e is a reference (address) to an array object
	x = f(..., e);
	if (e[0] == """special value""")
		# do something about it
	...

# use a parameter

def f (..., e2) : # e2 is a COPY of e
	...
	if (...)
		# something is wrong
		e2[0] = """special value"""
		return ...
	...

def g (...) :
	...
	e = [0] # e is a reference (address) of a list object
	x = f(..., e)
	if (e[0] == """special value""")
		# do something about it
	...

"""
three cases
	1. the return
	2. a global
	3. a parameter

if the user doesn't check, the language does NOT complain
the error propagates
"""

# use a exception

def f (...) :
	...
	if (...)
		# something is wrong
		raise E()
	...

def g (...) :
	...
	try :
		...
		x = f(...)
		...
	except E as e :
		# do something about it
	...
	else :
		# ONLY when NO exception is raised
	finally :
		# ALWAYS

"""
f doesn't raise E
	rest of f
	rest of try body
	NO except clause
	ELSE
	FINALLY
	rest of g
"""

"""
f does raise E
	NO rest of f
	NO rest of try body
	except clause
	NO else
	FINALLY
	rest of g
"""

# use a exception

def f (...) :
	...
	if (...)
		# something is wrong
		raise E()
	...
	else :
		# ONLY when NO exception is raised
	finally :
		# ALWAYS

def g (...) :
	...
	try :
		...
		x = f(...)
		...
	except F as e : # F is unrelated E
		# do something about it
	...
	else :
		# ONLY when NO exception is raised
	finally :
		# ALWAYS

"""
f does raise E
	NO rest of f
	NO rest of try body
	NO except clause
	NO else
	FINALLY
	NO rest of g
	go to the caller of g
		no except clause in the caller of g:                    go to the caller of the caller of g
		except clause in the caller of g, but doesn't handle E: go to the caller of the caller of g
		except clause in the caller of g, does handle E:        rest of the caller g
"""
