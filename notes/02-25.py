# -----------
# Fri, 25 Feb
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

"""
programming contest, teams
"""

# Types.py

def test15 () :
    class A :
        def bar (foo, i, s, f) :
            foo.i = i
            foo.s = s
            foo.f = f

        def __eq__ (self, rhs) :
            return (self.i == rhs.i) and (self.s == rhs.s) and (self.f == rhs.f)

	x = A()
	x.bar(2, "abc", 3.45)
	delete x.i
	y = A()
#    x = A(2, "abc", 3.45)
#    y = A(2, "abc", 3.45)
    assert x is not y
    assert x ==     y # x.__eq__(y), also like A.__eq__(x, y)

# self in Python is like this in Java

reduce(operator.add, [2, 3, 4], 0) -> 9

# reduce is an example of a higher-order function, that is a function that either takes or returns another function

reduce(A.__eq__, ...)

"""
Python exhibits an open   object model
Java   exhibits a  closed object model
"""

# Java

class A {
	int    i;
	string s;
	float  f;}

# Factorial.py

    def test6 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                print()
                print(f.__name__)
                if f.__name__ == "factorial" :
                    t = timeit.timeit(
                        "math." + f.__name__ + "(100)", # "math.factorial(100)"
                        "import math",
                        number = 1000)
                else :
                    t = timeit.timeit(
                        "__main__." + f.__name__ + "(100)", # "__main__.factorial_recursion(100)"
                        "import __main__",
                        number = 1000)
                print(f"{t*1000:.2f} milliseconds")

# 1.23 milliseconds

T = typing.TypeVar("T")

def f (a, b) : # a function that is callable
	...

lambda (a, b) : ... # a lambda that is callable

class A :
	def __len__ (...) # len(x)

	def __eq__ (...)  # x == y

	def __call__ (...) # x(), an instance of A is now callable!!!

def reduce_for (bf: typing.Callable[[T, T], T], a: typing.Iterable[T], v: T) -> T :
    for w in a :
        v = bf(v, w)
    return v

def reduce_while (bf: typing.Callable[[T, T], T], a: typing.Iterable[T], v: T) -> T :
    p = iter(a)
    try :
        while True :
            w = next(p)
            v = bf(v, w)
    except StopIteration :
        pass
    return v

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
# https://graphics.stanford.edu/~seander/bithacks.html

from copy     import copy, deepcopy
from operator import add

def test1 () :
    i = 2
    j = -i         # negation
    assert i ==  2
    assert j == -2

def test2 () :
    i = 2
    j = 3
    k = i + j     # addition
    assert i == 2
    assert j == 3
    assert k == 5

def test3 () :
    i = 2
    j = 3
    k = operator.add(i, j) # addition
    assert i == 2
    assert j == 3
    assert k == 5

reduce(+,            ...) # no
reduce(operator.add, ...) # yes

def test4 () :
    i = 2
    j = 3
    i += j        # in-place addition
    assert i == 5
    assert j == 3

def test5 () :
    i = 4
    j = 2
    f = i / j                   # true division
    assert i == 4
    assert j == 2
    assert isinstance(f, float)
    assert f == 2.0

def test6 () :
    i = 5
    j = 2
    k = i // j                # floor division
    assert i == 5
    assert j == 2
    assert isinstance(k, int)
    assert k == 2

def test7 () :
    f = 5.0
    j = 2
    g = f // j                  # floor division
    assert f == 5.0
    assert j == 2
    assert isinstance(g, float)
    assert g == 2.0

def test8 () :
    i = 5
    j = 2
    k = i % j     # mod
    assert i == 5
    assert j == 2
    assert k == 1

def test9 () :
    i = 5
    j = 2
    i %= j        # in-place mod
    assert i == 1
    assert j == 2

def test10 () :
    i = 2
    j = 3
    k = i ** j    # exponentiation
    assert i == 2
    assert j == 3
    assert k == 8

def test11 () :
    i = 2
    j = 3
    i **= j       # in-place exponentiation
    assert i == 8
    assert j == 3

def test12 () :
    i = 2
    j = ~i         # bit complement
    k = ~j
    assert i ==  2
    assert j == -3
    assert k ==  2

def test13 () :
    i = 2
    j = 3
    k = i << j     # bit shift left
    assert i ==  2
    assert j ==  3
    assert k == 16

def test14 () :
    i = 2
    j = 3
    i <<= j        # in-place bit shift left
    assert i == 16
    assert j ==  3

def test15 () :
    i = 10         # 1010
    j = 12         # 1100
    k = i & j      # 1000: bit and
    assert i == 10
    assert j == 12
    assert k ==  8

def test16 () :
    i = 10
    j = 12
    i &= j         # in-place bit and
    assert i ==  8
    assert j == 12

def test17 () :
    i = 10         # 1010
    j = 12         # 1100
    k = i | j      # 1110: bit or
    assert i == 10
    assert j == 12
    assert k == 14

def test18 () :
    i = 10
    j = 12
    i |= j         # in-place bit or
    assert i == 14
    assert j == 12

def test19 () :
    i = 10         # 1010
    j = 12         # 1100
    k = i ^ j      # 0110: bit exclusive or
    assert i == 10
    assert j == 12
    assert k ==  6

def test20 () :
    i = 10
    j = 12
    i ^= j         # in-place bit exclusive or
    assert i ==  6
    assert j == 12

def test21 () : # only ints
    i = 10
    j = 12
    i ^= j
    j ^= i
    i ^= j
    assert i == 12
    assert j == 10

	i, j = j, i # for anything

def test22 () :
    a = True
    b = True
    c = False
    assert a and b
    assert not (a and c)
    assert a or b
    assert a or c

def test23 () :
    s = "abc"
    assert s[1]             == "b" # str index
    assert s.__getitem__(1) == "b"
    assert str.__getitem__(s, 1) == "b"
    #s[1] = "d"                    # TypeError: 'str' object does not support item assignment

def test24 () :
    a = [2, 3, 4]
    assert a[1]             == 3 # list index
    assert a.__getitem__(1) == 3 # list.__getitem__(a, 1)
    a[1] = 5
    assert a == [2, 5, 4]

def test25 () :
    u = (2, 3, 4)
    assert u[1]             == 3 # tuple index
    assert u.__getitem__(1) == 3 # tuple.__getitem__(u, i)
    #u[1] = 5                    # TypeError: 'tuple' object does not support item assignment
