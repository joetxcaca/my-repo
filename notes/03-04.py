# -----------
# Fri,  4 Mar
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
"""

"""
iteration
"""

#!/usr/bin/env python3

# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ------------
# Iteration.py
# ------------

# https://docs.python.org/3.9/tutorial/controlflow.html
# https://docs.python.org/3.9/library/itertools.html

import itertools

def test1 () :
    a = [2, 3, 4]
    assert isinstance(a, list)
    assert not hasattr(a, "__next__")    # list is a container, NOT an iterator
    assert     hasattr(a, "__iter__")    # responds with a list iterator
    assert     hasattr(a, "__getitem__")
    assert     hasattr(a, "__len__")
    s = 0
    for v in a :
        s += v
    assert s == 9

def test2 () :
    a = [2, 3, 4]
    for v in a :
        v += 1            # ?
    assert a == [2, 3, 4]

def test3 () :
    a = [[2], [3], [4]]
    for v in a :
        v += (5,)                        # ?
    assert a == [[2, 5], [3, 5], [4, 5]]

def test4 () :
    a = [(2,), (3,), (4,)]
    for v in a :
        v += (5,)                  # ?
    assert a == [(2,), (3,), (4,)]

def test5 () :
    a = ["abc", "def", "ghi"]
    for v in a :
        v += "x"                      # ?
    assert a == ["abc", "def", "ghi"]

for v in a : # a needs to be an iterable
	...

for u, v in a : # a needs to be iterable over iterables of length 2
	...

for u, v, w in a : # a needs to be iterable over iterables of length 3
	...

def test6 () :
    a = [[2, "abc"], (3, "def"), [4, "ghi"]]
    s = 0
    for u, _ in a :
        s += u
    assert s == 9

def test7 () :
    x = {2, 3, 4}
    assert isinstance(x, set)
    assert not hasattr(x, "__next__")    # set is NOT an iterator, IS a container
    assert     hasattr(x, "__iter__")    # respond with a set iterator
    assert not hasattr(x, "__getitem__") # can't index, it's a hash table
    assert     hasattr(x, "__len__")
    s = 0
    for v in x :                         # order not guaranteed
        s += v
    assert s == 9

def test8 () :
    d = {2: "abc", 3: "def", 4: "ghi"}   # dict
    assert isinstance(d, dict)
    assert not hasattr(d, "__next__")
    assert     hasattr(d, "__iter__")
    assert     hasattr(d, "__getitem__") # can index with the key
    assert     hasattr(d, "__len__")
    s = 0
    for k in d :                         # order not guaranteed
        s += k                           # for in iterates over keys
    assert s == 9

def test9 () :
    d = {2: "abc", 3: "def"}
    k1 = d.keys() # O(1), lazy machinery
    assert str(type(k1)) == "<class 'dict_keys'>"
    assert not hasattr(k1, "__next__")    # dict_keys is NOT an iterator, IS a container
    assert     hasattr(k1, "__iter__")    # dick_keys iterator
    assert not hasattr(k1, "__getitem__") # can't index
    assert     hasattr(k1, "__len__")
    assert set(k1) == {2, 3}              # set's constructor takes an iterable
    assert set(k1) == {3, 2}
    k2 = d.keys()
    assert k1 is not k2
    d[4] = "ghi"
    assert d == {2: "abc", 3: "def", 4: "ghi"}
    assert set(k1) == {2, 3, 4}
    assert set(k2) == {2, 3, 4}

def test10 () :
    d = {2: "abc", 3: "def", 4: "ghi"}
    v = d.values() # O(1), lazy
    assert str(type(v)) == "<class 'dict_values'>"
    assert set(v) == {"abc", "def", "ghi"}

def test11 () :
    d = {2: "abc", 3: "def", 4: "ghi"}
    kv = d.items() # O(1), lazy
    assert str(type(kv)) == "<class 'dict_items'>"
    assert set(kv) == {(2, "abc"), (3, "def"), (4, "ghi")}

def test12 () :
    r = range(10) # stop, exclusive
    assert isinstance(r, range)
    assert not hasattr(r, "__next__")    # range is NOT an iterator, IS a container
    assert     hasattr(r, "__iter__")    # range iterator
    assert     hasattr(r, "__getitem__")
    assert     hasattr(r, "__len__")
    assert list(r) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # list's constructor takes an iterable
    assert list(r) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def test13 () :
    r = range(2, 10) # start, inclusive; stop, exclusive
    assert list(r) == [2, 3, 4, 5, 6, 7, 8, 9]

def test14 () :
    r = range(2, 10, 2) # start, stop, step
    assert list(r) == [2, 4, 6, 8]

def test15 () :
    r = range(10, 2, -2) # backwards
    assert list(r) == [10, 8, 6, 4]

def test16 () :
    r = range(10)
    assert r[0] == 0
    assert r[9] == 9
    try :
        assert r[10] == 10 # error: out of range
        assert False
    except IndexError :
        pass
    #r[0] = 2              # TypeError: 'range' object does not support item assignment

# range is like tuple in that neither the content nor the size can be changed

def test17 () :
    r = range(15)
    s = 0
    for v in r :
        if v == 10 :
            break
        s += v
    else :           # else clause in a for loop
        assert False # executes when the loop terminates normally
    assert s == 45

"""
if for in is being used to search for someting
getting to the end of the loop means you didn't find it
then run the else clause
"""

def test18 () :
    c = itertools.count()                 # 0, 1, 2, ... # O(1), lazy
    assert isinstance(c, itertools.count)
    assert     hasattr(c, "__next__")     # count IS an iterator, NOT a container
    assert     hasattr(c, "__iter__")
    assert not hasattr(c, "__getitem__")  # can't index
    assert not hasattr(c, "__len__")
    assert iter(c) is c
    s = 0
    for v in c :
        if v > 4 :
            break
        s += v
    assert s == 10                        # 0+1+2+3+4 = 10
    s = 0
    for v in c : # start where it left off
        if v > 9 :
            break
        s += v
    assert s == 30                        # 6+7+8+9 = 30

def test19 () :
    c = itertools.count(3, 2)  # 3, 5, 7, 9, ...
    s = 0
    for v in c :
        if v > 7 :
            break
        s += v       # 3+5+7 = 15
    assert s == 15

def test20 () :
    c = itertools.count(3, -2) # 3, 1, -1, -3, ...
    s = 0
    for v in c :
        if v < -1 :
            break
        s += v
    assert s == 3    # 3+1-1 = 3

def test21 () :
    z = zip([2, 3], (4, 5, 6))  # zip takes any number of iterables, the rows of a matrix, O(1), lazy
    assert isinstance(z, zip)
    assert     hasattr(z, "__next__")    # zip is an iterator, NOT a container
    assert     hasattr(z, "__iter__")
    assert not hasattr(z, "__getitem__")
    assert not hasattr(z, "__len__")
    assert iter(z) is z
    assert list(z) == [(2, 4), (3, 5)] # tuples of the cols of the matrix
    assert list(z) == []

def test22 () :
    z = zip([2, 3], itertools.count()) # O(1), lazy
    assert list(z) == [(2, 0), (3, 1)]
    assert list(z) == []

def main () :
    print("Iteration.py")
    for i in range(22) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
