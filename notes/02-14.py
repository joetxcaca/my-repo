# -----------
# Mon, 14 Feb
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
"""

"""
cold calling
specifications grading
huge disconnect between lectures and Web project
"""

"""
Paper #4: 2022-02-13: Pair Programming
you MUST go to Perusall THROUGH Canvas
"""

#!/usr/bin/env python3

# pylint: disable = duplicate-key
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = literal-comparison
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# --------
# Types.py
# --------

# https://docs.python.org/3.6/library/types.html

from collections import deque
from types       import FunctionType

def test1 () :
    b: bool = bool()
    c: bool = False
    assert b is c
    assert isinstance(b,    bool)
    assert isinstance(bool, type)

def test2 () :
    i: int = int()
    j: int = 0
    assert i is j
    i  = 2
    i += 1
    j  = 3
    assert i is j
    i  = 255
    i +=   1
    j  = 256
    assert i is j                # value caching
    i  = 256
    i +=   1
    j  = 257
    assert i is not j            # cache: [-5, 256]
    assert i ==     j
    i = 257
    j = 257
    assert i is j                # literal caching
    i =  -4
    i -=  1
    j =  -5
    assert i is j
    i =  -5
    i -=  1
    j =  -6
    assert i is not j            # cache: [-5, 256]
    assert i ==     j
    assert isinstance(i,   int)
    assert isinstance(int, type)

def test3 () :
    f: float = float()
    g: float = 0.0
    assert f is not g
    assert f ==     g
    assert isinstance(f,     float)
    assert isinstance(float, type)

def test4 () :
    c: complex = complex()
    d: complex = 0 + 0j
    assert c is not d
    assert c ==     d
    assert isinstance(c,       complex)
    assert isinstance(complex, type)

"""
str is immutable, both in content and structure
str is homogeneous
"""

def test5 () :
    s: str = str() # no arg constructor
    t: str = ""    # ' ', ''' ''', """ """, can also add "r"
    assert s is t
    assert isinstance(s,   str)
    assert isinstance(str, type)

"""
list is mutable, both in content and structure
list is heterogeneous
ordered
cost of operations
add to the front  of a list: O(n)
add to the middle of a list: O(n)
add to the back   of a list: amortized O(1)
remove from the front  of a list: O(n)
remove from the middle of a list: O(n)
remove from the back   of a list: O(1)
indexing: O(1)
"""

def test6 () :
    a: list = list() # no arg constructor
    b: list = []
    assert a is not b
    assert a ==     b
    a = [2, "abc", 3.45]
    assert a == [2, "abc", 3.45]
    assert a != ["abc", 2, 3.45]
    assert isinstance(a,    list)
    assert isinstance(list, type)

"""
tuple is immutable, both in content and structure
in every other way, it's like list
"""

def test7 () :
    u: tuple = tuple() # no arg constructor
    v: tuple = ()
    assert u is v
    u = (2, "abc", 3.45)
    assert u == (2, "abc", 3.45)
    assert u != ("abc", 2, 3.45)
    assert isinstance(u,     tuple)
    assert isinstance(tuple, type)

"""
set shares "{" and "}" with dict
{} means an empty dict, NOT an empty set
set is   mutable, only in structure
set is immutable, in content
sets have keys
elements must be unique
sets are unordered
Java's   sets are available has a hashtable (HashSet) and a binary search tree (TreeSet)
Python's set  is a hastable
elements must hashable
in Python the types are hashable are the types that are immutable
mutable
	list
	set
	dict
immutable
	str
	tuple
	frozenset
cost of adding:   amortized O(1)
cost of removing: O(1)
indexing: not available
"""

def test8 () :
    x: set = set() # no arg constructor
    y: set = set()
    assert x is not y
    assert x ==     y
    x = {2, 2, "abc", 3.45}
    assert x == {2, "abc", 3.45}
    assert x == {"abc", 2, 3.45}
    assert isinstance(x,   set)
    assert isinstance(set, type)

"""
frozenset is an immutable set, both in content and structure
"""

def test9 () :
    x: frozenset = frozenset() # no arg constructor
    y: frozenset = frozenset()
    assert x is y
    y = frozenset((2, 2, "abc", 3.45))
    assert y == frozenset([2, "abc", 3.45])
    assert y == frozenset(["abc", 2, 3.45])
    assert isinstance(y,         frozenset)
    assert isinstance(frozenset, type)

"""
dict has key value pairs
dict is mutable, in content (only the values of the key value pairs), in structure
cost of adding:   amortized O(1)
cost of removing: O(1)
indexing: not available
"""

def test10 () :
    d: dict = dict() # no arg constructor
    e: dict = {}
    assert d is not e
    assert d ==     e
    d = {2: "xxx", 2: "abc", 3: "def", 4: "ghi"}
    assert d == {2: "abc", 3: "def", 4: "ghi"}
    assert d == {3: "def", 2: "abc", 4: "ghi"}
    assert isinstance(d,    dict)
    assert isinstance(dict, type)

"""
deque a linked list
add to the front  of a deque: O(1)
add to the middle of a deque: O(1), if I was given a reference to the middle
add to the back   of a deque: O(1)
remove from the front  of a deque: O(1)
remove from the middle of a deque: O(1), if I was given a reference to the middle
remove from the back   of a deque: O(1)
indexing: O(n)
"""

def test11 () :
    q = deque()
    r = deque()
    assert q is not r
    assert q ==     r
    q = deque((2, "abc", 3.45))
    assert q == deque((2, "abc", 3.45))
    assert q != deque(("abc", 2, 3.45))
    assert isinstance(q,     deque)
    assert isinstance(deque, type)

def test12 () :
    def f (v) :
        return v + 1
    assert isinstance(f,            FunctionType)
    assert isinstance(FunctionType, type)

def test13 () :
    f: FunctionType = lambda v : v + 1
    assert isinstance(f,            FunctionType)
    assert isinstance(FunctionType, type)

def test14 () :
    class A :
        def __init__ (self, i, s, f) :
            self.i = i
            self.s = s
            self.f = f

    x = A(2, "abc", 3.45)
    y = A(2, "abc", 3.45)
    assert x is not y
    assert x !=     y
    assert isinstance(x,    A)
    assert isinstance(x,    object)
    assert isinstance(A,    type)
    assert isinstance(type, type)

    assert issubclass(A, A)
    assert issubclass(A, object)

    assert issubclass(type, type)
    assert issubclass(type, object)

    assert issubclass(object, object)

def test15 () :
    class A :
        def __init__ (self, i, s, f) :
            self.i = i
            self.s = s
            self.f = f

        def __eq__ (self, rhs) :
            return (self.i == rhs.i) and (self.s == rhs.s) and (self.f == rhs.f)

    x = A(2, "abc", 3.45)
    y = A(2, "abc", 3.45)
    assert x is not y
    assert x ==     y

def main () :
    print("Types.py")
    for i in range(15) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
