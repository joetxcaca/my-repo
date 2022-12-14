# -----------
# Wed,  9 Mar
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

"""
yield
digits_iterator
"""

def f () :
	print("abc")
	yield 2
	print("def")
	yield 3
	print("ghi")

p = f()        # f() does NOT run, prints nothing, O(1), lazy, building a generator
print(type(p)) # generator

v = next(p)    # f() begins to run, prints abc
print(v)       # 2

v = next(p)    # f() begins where it left off, prints def
print(v)       # 3

v = next(p)    # f() begins where it left off, prints ghi
			   # raises StopIteration

#!/usr/bin/env python3

# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = no-member

# --------
# Yield.py
# --------

# https://docs.python.org/3.9/reference/simple_stmts.html?highlight=yield#grammar-token-yield-stmt

import types

def f () :
    yield 2
    yield 3
    yield 4

def test1 () :
    p = f()
    assert isinstance(p, types.GeneratorType)
    assert     hasattr(p, "__next__")
    assert     hasattr(p, "__iter__")
    assert not hasattr(p, "__getitem__")
    assert not hasattr(p, "__len__")
    assert iter(p) is p
    n = next(p)
    assert n == 2
    n = next(p)
    assert n == 3
    n = next(p)
    assert n == 4
    try :
        n = next(p)
    except StopIteration :
        pass

def test2 () :
    p = f()
    assert list(p) == [2, 3, 4]
    assert list(p) == []

def g () :
    for v in [2, 3, 4] :
        yield v

def test3 () :
    p = g()
    assert iter(p) is p
    n = next(p)
    assert n == 2
    n = next(p)
    assert n == 3
    n = next(p)
    assert n == 4
    try :
        n = next(p)
    except StopIteration :
        pass

def test4 () :
    p = g()
    assert list(p) == [2, 3, 4]
    assert list(p) == []

def main () :
    print("Yield.py")
    for i in range(4) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()




class digits_iterator_1 :
    def __init__ (self, v) :
        self.v = v

    def __iter__ (self) :
        return self

    def __next__ (self) :
        if self.v == 0 :
            raise StopIteration
        w = self.v % 10
        self.v //= 10
        return w

def digits_iterator_2 (v) :
    while v != 0 :
        yield v % 10
        v //= 10

def test0 () :
    p = digits_iterator(0)
    assert hasattr(p, "__next__")
    assert hasattr(p, "__iter__")
    assert iter(p) is p
    try :
        next(p)
        assert False
    except StopIteration :
        pass

def test1 () :
    p = digits_iterator(2)
    assert next(p) == 2
    try :
        next(p)
        assert False
    except StopIteration :
        pass

def test2 () :
    p = digits_iterator(23)
    assert next(p) == 3
    assert next(p) == 2
    try :
        next(p)
        assert False
    except StopIteration :
        pass

def test3 () :
    p = digits_iterator(234)
    a = [v for v in p]
    assert a == [4, 3, 2]
    a = [v for v in p]
    assert a == []

def test4 () :
    p = digits_iterator(234)
    assert list(p) == [4, 3, 2]
    assert list(p) == []
