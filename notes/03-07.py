# -----------
# Mon,  7 Mar
# -----------

"""
Class (you must attend your lecture)
	MWF 10 am CT, Anshul, Vaishnav
	MWF 11 am CT, Alex,   Mengning

Website
	https://www.cs.utexas.edu/users/downing/cs373/Schedule.html

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

Cold Calling
	you're only called ONCE per rotation
	it's totally fine to not know the answer, the idea is to discuss and to learn

Notes
	these notes will be posted on GitLab

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
	5.9.6
	must use UT EID credentials (@eid.utexas.edu)
	classes recorded
	published later that day

Specifications Grading
	please ask about this if you don't undestand it
	please use the Google Sheet that we're providing to track your grades

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
Paper #7: Liskov Substitution Principle
you MUST go to Perusall THROUGH Canvas

this is the third of a 5-paper series
SOLID design
"""

"""
Project #3: IDB2
	 1. provide feedback to your development team about the 5 user stories
	 2. provide 5 new user stories to your development team
	 3. collect data on many instances
	 4. create a DB
	 5. change your site from being static to dynamic
	 6. implement your API
	 7. your backend must provide the API, your frontend must consume the API
	 8. splash page
	 9. 3 model pages (tables with cards, show 5 attributes per card)
	10. add pagination to the model pages
	 	a. how many instances total
	 	b. how many pages total
	 	c. next page
	 	d. previous page
	 	e. first page
	 	f. last page
	 	g. what page am I on
	11. MANY instance pages (a lot of text AND rich media: feeds, images, videos, etc.)
	12. about page (dynamic from GitLab with a RESTful API)
	13. unit tests
	 	a. API with Postman
	 	b. frontend with JavaScript
	 	c. backend with Python
	14. acceptance tests of the GUI with Selenium
	15. technical report (very important, SWE is has a writing flag)
	16. UML diagram
	17. schedule your weekly meeting with the TA
	18. be responsive to your teammates and your mentor TA on Discord
	19. be responsive to the other two teams that you're connected to on Canvas

https://www.cs.utexas.edu/users/downing/cs373/Groups.html

IDB2 rubric is out
IDB1 peer reviews were published by CATME
"""

"""
Takeaways:

1. assertions are not good for testing
2. assertions are not good for user errors
3. frozenset, str, tuple are immutable in content and size
4. set is immutable in content
5. iter on an iterator returns itself
6. iterators are exhaustible, containers are not
7. generators are iterators
8. generators, map, and filter are capturing objects, not pointers
"""

#!/usr/bin/env python3

# pylint: disable = consider-using-dict-items
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = no-member

# -----------------
# Comprehensions.py
# -----------------

# https://docs.python.org/3.9/tutorial/datastructures.html

import types

def test1 () :
    a = [2, 3, 4]
    b = []
    for v in a :
        b += [v * v]
    assert isinstance(b, list)
    assert a       == [2, 3,  4]
    assert b       == [4, 9, 16]

def test2 () :
    a = [2, 3, 4]
    b = [v * v for v in a]       # list comprehension, O(n), eager
    assert isinstance(b, list)
    assert a       == [2, 3,  4]
    assert b       == [4, 9, 16]

def test3 () :
    a = [2, 3, 4]
    g = (v * v for v in a)                    # generator, O(1), lazy
    assert isinstance(g, types.GeneratorType)
    assert     hasattr(g, "__next__")         # a generator is an iterator
    assert     hasattr(g, "__iter__")
    assert not hasattr(g, "__getitem__")
    assert not hasattr(g, "__len__")
    assert iter(g) is g
    assert a       == [2, 3,  4]
    assert list(g) == [4, 9, 16] # O(n)
    assert list(g) == []

def test4 () :
    a  = [2, 3, 4]
    g  = (v * v for v in a)          # capture the list, NOT a
    a += [5]                         # change  the list, NOT a
    assert a       == [2, 3,  4,  5]
    assert list(g) == [4, 9, 16, 25]
    assert list(g) == []
    a += [5]
    assert list(g) == []

def test5 () :
    a = [2, 3, 4]
    g = (v * v for v in a)           # capture the list, NOT a
    a = [2, 3, 4, 5]                 # change a,         NOT the list
    assert a       == [2, 3,  4,  5]
    assert list(g) == [4, 9, 16]
    assert list(g) == []

class Justin :
	def __call__ (...) : # this would make a Justin object callable
		...

	def __iter__ (...) : # this would make a Justin object iterable
		...

	def __getitem__ (...) : # this would make a Justin object indexable
		...

x = Justin()
x(...)       # a Justin object being callable

map(x, ...)  # that would be ok

"""
map takes two arguments:
	1. a  callable (unary)
	2. an iterable
"""

def test6 () :
    a = [2, 3, 4]
    m = map(lambda v : v * v, a)         # O(1), lazy
    assert isinstance(m, map)
    assert     hasattr(m, "__next__")    # map is an iterator
    assert     hasattr(m, "__iter__")
    assert not hasattr(m, "__getitem__")
    assert not hasattr(m, "__len__")
    assert iter(m) is m                  # iter on any iterator returns itself
    assert a       == [2, 3,  4]
    assert list(m) == [4, 9, 16]         # O(n), eager
    assert list(m) == []

def test7 () :
    a = [2, 3, 4]
    m = map(lambda v : v * v, a)     # capture the list, NOT a
    a += [5]                         # change  the list, NOT a
    assert a       == [2, 3,  4,  5]
    assert list(m) == [4, 9, 16, 25]
    assert list(m) == []
    a += [5]
    assert list(m) == []

"""
map takes many arguments:
	1. a  callable that takes the right number of arguments
	2. an iterable
	3. an iterable
	...
	n. an iterable

	all iterables MUST be the same length
"""

def test8 () :
    a = [2, 3, 4]
    b = [5, 6, 7]
    m = map(lambda x, y : x + y, a, b) # O(1), lazy
    assert list(m) == [7, 9, 11]       # O(n), eager
    assert list(m) == []

def test9 () :
    a = [2, 3, 4]
    b = [5, 6, 7]
    z = zip(a, b)                # O(1), lazy -> (2, 5) (3, 6) (4, 7)
    m = (x + y for x, y in z)    # binary for in
    assert list(m) == [7, 9, 11]
    assert list(m) == []
    assert list(z) == []

def test10 () :
    a = [2, 3, 4, 5, 6]
    b = []
    for v in a :
        if v % 2 :
            b += [v * v]
    assert a == [2, 3, 4,  5,  6]
    assert b == [   9,    25]

def test11 () :
    a = [2, 3, 4, 5, 6]
    b = [v * v for v in a if v % 2] # O(n), eager
    assert a == [2, 3, 4,  5,  6]
    assert b == [   9,    25]

def test12 () :
    a = [2, 3, 4, 5, 6]
    g = (v * v for v in a if v % 2) # O(1), lazy, a generator which is an iterator
    assert a       == [2,  3,  4,  5,  6]
    assert list(g) == [    9,     25]
    assert list(g) == []

def test13 () :
    a = [2, 3, 4, 5, 6]
    f = filter(lambda v : v % 2, a)
    assert isinstance(f, filter)
    assert     hasattr(f, "__next__")
    assert     hasattr(f, "__iter__")
    assert not hasattr(f, "__getitem__")
    assert not hasattr(f, "__len__")
    assert iter(f) is f
    m = map(lambda v : v * v, f)
    assert a       == [2,  3,  4,  5,  6]
    assert list(m) == [    9,     25]
    assert list(f) == []
    assert list(m) == []

def test14 () :
    a = [2, 3, 4, 5, 6]
    f = (v for v in a if v % 2)
    m = (v * v for v in f)
    assert a       == [2,  3,  4,  5,  6]
    assert list(m) == [    9,     25]
    assert list(f) == []
    assert list(m) == []

def test15 () :
    a = [2, 3, 4]
    b = [4, 5]
    c = []
    for v in a :
        for w in b :
            c += [v + w]
    assert a == [2, 3, 4]
    assert b == [4, 5]
    assert c == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5]
    assert c == [  6,   7,   7,   8,   8,   9]

def test16 () :
    a = [2, 3, 4]
    b = [4, 5]
    c = [v + w for v in a for w in b]
    assert a == [2, 3, 4]
    assert b == [4, 5]
    assert c == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5]
    assert c == [  6,   7,   7,   8,   8,   9]

def test17 () :
    a = [2, 3, 4]
    b = [4, 5]
    g = (v + w for v in a for w in b)
    assert a       == [2, 3, 4]
    assert b       == [4, 5]
    assert list(g) == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5]
    assert list(g) == []

def test18 () :
    s = {2, 3, 4}
    t = set()              # NOT {}
    for v in s :
        t |= {v * v}       # union equal differs from plus equal
    assert s == {2, 3,  4}
    assert t == {4, 9, 16}

def test19 () :
    s = {2, 3, 4}
    t = {v * v for v in s} # set comprehension, O(n), eager
    assert s == {2, 3,  4}
    assert t == {4, 9, 16}

def test20 () :
    d = {2: "abc", 3: "def", 4: "ghi"}
    e = {}
    for k in d :
        e[k + 1] = d[k] + "xyz"
    assert d == {2: "abc",    3: "def",    4: "ghi"}
    assert e == {3: "abcxyz", 4: "defxyz", 5: "ghixyz"}

def test21 () :
    d = {2: "abc", 3: "def", 4: "ghi"}
    e = {k + 1: d[k] + "xyz" for k in d}                # dict comprehension, O(n), eager
    assert d == {2: "abc",    3: "def",    4: "ghi"}
    assert e == {3: "abcxyz", 4: "defxyz", 5: "ghixyz"}

def main () :
    print("Comprehensions.py")
    for i in range(21) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
