# -----------
# Fri, 11 Mar
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
Paper #8: Interface Segregation Principle
you MUST go to Perusall THROUGH Canvas

this is the fourth of a 5-paper series
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
 8. generators and map and filter capture objects!!!
 9. lambdas capture names!!!
"""

"""
iterators vs. containers
callables
"""


#!/usr/bin/env python3

# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods
# pylint: disable = unnecessary-comprehension

# ------------
# Iterables.py
# ------------

import typing

def test_iterator (p: typing.Iterator[int]) :
    assert hasattr(p, "__next__")
    assert hasattr(p, "__iter__")
    q = iter(p)                        # q = p.__iter__()
    assert q is p

    assert next(p) == 2 # p.__next__()
    assert next(p) == 3
    assert next(p) == 4

    try :
        assert next(p) == 5 # p.__next__()
        assert False
    except StopIteration :
        pass

def f () :
	print("abc")
	yield 2
	print("def")
	yield 3
	print("ghi")

x = f() # builds a generator!!!!

def my_iterator () :
    for v in range(2, 5) :
        yield v

x = my_iterator() # for is not running, my_iterator is not running, builds a generator

class my_iterator :
	def __init__ (self) :
		self.a = [2, 3, 4]
		self.p = iter(self.a)

	def __next__ (self) :
		return next(self.p)

	def __iter__ (self) :
		return self

def test1 () :
    test_iterator(iter([2, 3, 4]))                      # list
    test_iterator(iter((2, 3, 4)))                      # tuple
    test_iterator(iter({2, 3, 4}))                      # set
    test_iterator(iter({2: "abc", 3: "def", 4: "ghi"})) # dict
    test_iterator(iter([v for v in [2, 3, 4]]))         # list comprehension
    test_iterator(iter(range(2, 5)))
    test_iterator(v for v in [2, 3, 4])                 # generator
    test_iterator(   map(lambda v : v,    [2, 3, 4]))
    test_iterator(filter(lambda v : True, [2, 3, 4]))
    test_iterator(my_iterator())

def test_container (x: typing.Iterable[int]) :
    assert not hasattr(x, "__next__")
    assert     hasattr(x, "__iter__")
    p = iter(x)                         # p = x.__iter__()
    assert p is not x
    test_iterator(p)

class my_container :
    def __iter__ (self) :
        for v in range(2, 5) :
            yield v

class my_container :
	class my_iterator :
		def __init__ (self) :
			self.a = [2, 3, 4]
			self.p = iter(self.a)

		def __next__ (self) :
			return next(self.p)

		def __iter__ (self) :
			return self

	def __iter__ (self) :
		return my_container.my_iterator()

def test2 () :
    test_container([2, 3, 4])                      # list
    test_container((2, 3, 4))                      # tuple
    test_container({2, 3, 4})                      # set
    test_container({2: "abc", 3: "def", 4: "ghi"}) # dict
    test_container([v for v in [2, 3, 4]])         # list comprehension
    test_container(range(2, 5))
    test_container(my_container())

def main () :
    print("Iterables.py")
    for i in range(2) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()




#!/usr/bin/env python3

# pylint: disable = cell-var-from-loop
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# ------------
# Functions.py
# ------------

def square1 (v) :
    return v ** 2

def test1 () :
    a = [2, 3, 4]
    m = map(square1, a)
    assert list(m) == [4, 9, 16]
    assert list(m) == []





square2 = lambda v : v ** 2

def test2 () :
    a = [2, 3, 4]
    m = map(square2, a)
    assert list(m) == [4, 9, 16]
    assert list(m) == []





class square3 :
    def __call__ (self, v) :
        return v ** 2

x = square3(5) # no
x = square3()  # building an instance of square3
v = x(5)       # v = x.__call__(5)
print(v)       # 25

def test3 () :
    a = [2, 3, 4]
    m = map(square3,   a)        # no
    m = map(square3(), a)
    assert list(m) == [4, 9, 16]
    assert list(m) == []


a  = [2, 3, 4]
g  = (v ** 2 for v in a) # captures the object that a points to
a += [5]
print(list(g)) # [4, 9, 16, 25]

def pow1 (p) :
    def f (v) :
        return v ** p # this is called a closure, it must capture p!!!
    return f

x = pow1(2)
v = x(5)
print(v)    # 25

def test4 () :
    a = [2, 3, 4]
    m = map(pow1(2), a)
    assert list(m) == [4, 9, 16]
    assert list(m) == []





def pow2 (p) :
    return lambda v : v ** p # p must be captured, a closure

def test5 () :
    a = [2, 3, 4]
    m = map(pow2(2), a)
    assert list(m) == [4, 9, 16]
    assert list(m) == []





class pow3 :
    def __init__ (self, p) :
        self.p = p

    def __call__ (self, v) :
        return v ** self.p

x = pow3(2) # building an instance of pow3
v = x(5)    # v = x.__call__(5)
print(v)    # 25

def test6 () :
    a = [2, 3, 4]
    m = map(pow3, a)             # a generator over pow3 objects!!!
    m = map(pow3(2), a)
    assert list(m) == [4, 9, 16]
    assert list(m) == []


"""
generators and map and filter capture objects!!!
lambdas capture names!!!
"""


def test7 () :
    a     = [2, 3, 4]
    n     = [1]
    m     = map(lambda v : v ** next(iter(n)), a)
    a    += [5]
    n[0]  = 2
    assert list(m) == [4, 9, 16, 25]
    assert list(m) == []

def test8 () :
    a = [2, 3, 4]
    n = [1]
    m = map(lambda v : v ** next(iter(n)), a)
    a = [2, 3, 4, 5]
    n = [2]
    assert list(m) == [4, 9, 16]
    assert list(m) == []

def test9 () :
    a  = [2, 3, 4]
    fs = [lambda v : v ** n for n in range(3)]
    ms = [map(f, a) for f in fs]
    assert [list(m) for m in ms] == [[4, 9, 16], [4, 9, 16], [4, 9, 16]]
    assert [list(m) for m in ms] == [[],         [],         []]





def main () :
    print("Functions.py")
    for i in range(9) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
