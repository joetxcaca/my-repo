# -----------
# Mon, 29 Feb
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
	https://forms.gle/evXiWYUc6wqHzffb6/

Teams
	https://docs.google.com/spreadsheets/d/1dmteNPBFr6wc-OAksyKTdGrg1RDN0EMzUiNbixt-iSY/
"""

"""
cold calling
specifications grading
huge disconnect between lectures and Web project
"""

"""
please track your grades
please be responsive on Canvas
"""

"""
Paper #6: Open-Closed Principle
you MUST go to Perusall THROUGH Canvas

this is the first of a 5-paper series
SOLID design
"""

"""
Project #2: IDB1
	 1. respond to the RFP
	 2. THREE disparate data sources with a RESTful API
	 3. civic engagement
	 4. splash page
	 5. 3 model pages (tables with cards, show 5 attributes per card)
	 6. 9 instance pages (a lot of text AND rich media: feeds, images, videos, etc.)
	 7. about page (dynamic from GitLab with a RESTful API)
	 8. API documentation on Postman
	 9. technical report (very important, SWE is has a writing flag)
	10. schedule your weekly meeting with the TA
	11. be responsive to your teammates and your mentor TA on Discord
	12. be responsive to the other two teams that you're connected to on Canvas
	13. 5 user stories to the team that you are the customer of
	14. customer teams to give feedback to developer teams about the technical report

https://www.cs.utexas.edu/users/downing/cs373/Groups.html
"""

#!/usr/bin/env python3

# pylint: disable = chained-comparison
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = literal-comparison
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# ------------
# Operators.py
# ------------

# https://docs.python.org/3/library/operator.html
# https://docs.python.org/3/reference/datamodel.html
# https://graphics.stanford.edu/~seander/bithacks.html

import copy
import operator

class Rodrigo :
	def __getitem__ (x) : # x might be an int   (pos or neg)
		...               # x might be a  slice (pos or neg step)

	def _setitem__ (x, v) :
		...

def test26 () :
    a = [2, 3, 4]
    assert a[ 1] == 3 # pos indices:  0 to n-1
    assert a[-1] == 4 # neg indices: -1 to -n

    assert a[1 : 2] == [3] # list slicing, start (inclusive), stop (exclusive)

    s = slice(1, 2) # two arg constr
    assert s.start                == 1
    assert s.stop                 == 2
    assert a[s]                   == [3]
    assert a.__getitem__(s)       == [3]
    assert list.__getitem__(a, s) == [3]

    assert a[ 1 : 3] == [3, 4]
    assert a[-2 : 3] == [3, 4]
    assert a[ 0 : 3] == [2, 3, 4]

    assert a[0 : 3 : 2] == [2, 4] # this like range(start, stop, step)

    s = slice(0, 3, 2) # three arg constr
    assert s.start                == 0
    assert s.stop                 == 3
    assert s.step                 == 2
    assert a[s]                   == [2, 4]
    assert a.__getitem__(s)       == [2, 4]
    assert list.__getitem__(a, s) == [2, 4]

    assert a[2 : -4 : -2] == [4, 2]
    assert a[:]           == [2, 3, 4] # this MIGHT be a copy

def test27 () :
    a = [2, 3, 4]
    b = a[:]      # made a copy
    assert a is not b
    assert a ==     b
    b[1] += 1
    assert a == [2, 3, 4]
    assert b == [2, 4, 4]

def test28 () :
    u = (2, 3, 4)
    v = u[:]      # NO copy
    assert u is v

def test29 () :
    a = [2, 3, 4]
    b = copy.copy(a)
    assert a is not b
    assert a ==     b
    b[1] += 1
    assert a == [2, 3, 4]
    assert b == [2, 4, 4]

def test30 () :
    u = (2, 3, 4)
    v = copy.copy(u) # NO copy
    assert u is v

def test31 () :
    a = [2, 3, 4]
    b = [1, a, 5] # three elements: int, pointer, int
    c = b[:]      # made a copy
    assert b    is not c
    assert b    ==     c
    assert b[1] is     c[1]

def test32 () :
    a = [2, 3, 4]
    b = [1, a, 5]
    c = copy.copy(b)
    assert b    is not c
    assert b    ==     c
    assert b[1] is     c[1]

def test33 () :
    a = [2, 3, 4]
    b = [1, a, 5]
    c = copy.deepcopy(b)
    assert b    is not c
    assert b    ==     c
    assert b[1] is not c[1]
    assert b[1] ==     c[1]

def test34 () :
    s = "a"
    t = "bc"
    u = s + t             # string concatenation
    u = s.__add__(t)
    u = str.__add__(s, t)
    assert u is not "abc"
    assert u ==     "abc"

def test35 () :
    a = [2]
    b = [3, 4]
    c = a + b                 # list concatenation
    c = a.__add__(b)
    c = list.__add__(a, b)
    assert c is not [2, 3, 4]
    assert c ==     [2, 3, 4]
    assert c !=     (2, 3, 4)

def test36 () :
    u = (2,)
    v = (3, 4)
    w = (u + v)               # tuple concatenation
    w = u.__add__(v)
    w = tuple.__add__(u, v)
    assert w is not (2, 3, 4)
    assert w ==     (2, 3, 4)
    assert w !=     [2, 3, 4]

def test37 () :
    s = "abc"
    t = s * 2                # string replication
    t = s.__mul__(2)
    t = str.__mul__(s, 2)
    assert t is not "abcabc"
    assert t ==     "abcabc"

def test38 () :
    a = [2, 3, 4]
    b = a * 2                          # list replication
    b = 2 * a                          # the same
    b = a.__mul__(2)
    b = list.__mul__(a, 2)
    assert b is not [2, 3, 4, 2, 3, 4]
    assert b ==     [2, 3, 4, 2, 3, 4]

def test39 () :
    u = (2, 3, 4)
    v = u * 2                          # tuple replication
    v = u.__mul__(2)
    v = tuple.__mul__(u, 2)
    assert u is not (2, 3, 4, 2, 3, 4)
    assert v ==     (2, 3, 4, 2, 3, 4)

def test40 () :
    a = [2, 3, 4]
    b = a
    assert a is b
    b += [5]           # what is changing, b or the list? list
    b.__iadd__([6])    # in-place add
    list.__iadd__(b, [7])
    assert a == [2, 3, 4, 5, 6, 7]
    assert a is b

def test41 () :
    a = [2, 3, 4]
    b = a
    assert a is b
    b += (5,)        # list's += takes what on the right? an iterable
    b.__iadd__((6,))
    list.__iadd__(b, (7,))
    assert a == [2, 3, 4, 5, 6, 7]
    assert a is b

"""
x += y
is that the same as
x = x + y

in Python, it's MAYBE!
NO  for list
YES for tuple
"""

def test42 () :
    a = [2, 3, 4]
    b = a
    assert a is b
    b = b + [5]      # what is changing, b or the list? b
    b = b.__add__([6])
    b = list.__add__(b, [7])
    assert a == [2, 3, 4]
    assert b == [2, 3, 4, 5, 6, 7]

def test43 () :
    a = [2, 3, 4]
    b = a
    assert a is b
    #b = b + (5,) # TypeError: can only concatenate list (not "tuple") to list
    		      # list's + takes on the right ONLY another list

def test44 () :
    x = (2, 3, 4)
    y = x
    assert x is y
    y += (5,)        # what is changing, y or the tuple? y
#   y.__iadd__((6,))             # AttributeError: 'tuple' object has no attribute 'iadd'
    assert x == (2, 3, 4)
    assert y == (2, 3, 4, 5)

def test45 () :
    u = (2, 3, 4)
    v = u
    assert u is v
    #v += [5]     # TypeError: can only concatenate tuple (not "list") to tuple
				  # tuple's += takes what on the right? ONLY another tuple

def test46 () :
    x = (2, 3, 4)
    y = x
    assert x is y
    y = y + (5,)     # what is changing, y or the tuple? y
    y = y.__add__((6,))
    y = tuple.__add__(y, (7,))
    assert x == (2, 3, 4)
    assert y == (2, 3, 4, 5, 6, 7)

def test47 () :
    u = (2, 3, 4)
    v = u
    assert u is v
    #v = v + [5]  # TypeError: can only concatenate tuple (not "list") to tuple
				  # tuple's + takes on the right ONLY another tuple
