# -----------
# Fri, 25 Mar
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
Paper #9: Dependency Inversion Principle
remember to go to Perusall THROUGH Canvas

this is the fifth of a 5-paper series
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
10. avoid mutable defaults
"""

"""
Integrated 5-Year CS BS/MS Program
https://www.cs.utexas.edu/undergraduate/academics/curriculum-degree-plans/5-year-cs-bsms/
Info Session
Tue, 29 Mar, 6 pm
Zoom
"""

"""
P3 moved to Tue, 29 Mar
"""

"""
function defaults
function keywords
function unpacking
function tuple
function dict
"""

"""
three tokens:   =, *, **
two   contexts: a function definition, a function call
"""


#!/usr/bin/env python3

# pylint: disable = dangerous-default-value
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------------------
# FunctionDefaults.py
# -------------------

def f (x, y, z) :
    return [x, y, z]

def test1 () :
    # f(2, 3)                      # TypeError: f() missing 1 required positional argument: 'z'
    assert f(2, 3, 4) == [2, 3, 4]
    # f(2, 3, 4, 5)                # TypeError: f() takes 3 positional arguments but 4 were given





def g1 (x, y, z=5) :
    return [x, y, z]

def test2 () :
    assert g1(2, 3)    == [2, 3, 5]
    assert g1(2, 3, 4) == [2, 3, 4]

# def g2 (x, y=5, z) : # SyntaxError: non-default argument follows default argument
#     return [x, y, z]





def h1 (x=[]) : # mutable default
    x += [2]
    return x

def test3 () :
    assert h1()    == [2]
    assert h1()    == [2, 2]
    assert h1([1]) == [1, 2]
    assert h1()    == [2, 2, 2]
    assert h1([1]) == [1, 2]





def h2 (x=()) : # immutable default
    x += (2,)
    return x

def test4 () :
    assert h2()     == (2,)
    assert h2()     == (2,)
    assert h2((1,)) == (1, 2)
    assert h2()     == (2,)
    assert h2((1,)) == (1, 2)





def h3 (x=None) :
    if x is None :
        x = []
    x += [2]
    return x

def test5 () :
    assert h3()     == [2]
    assert h3()     == [2]
    assert h3([1])  == [1, 2]
    assert h3()     == [2]
    assert h3([1])  == [1, 2]
    assert h3(None) == [2]





def main () :
    print("FunctionDefaults.py")
    for i in range(5) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()








#!/usr/bin/env python3

# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = line-too-long

# -------------------
# FunctionKeywords.py
# -------------------

"""
call name
pros:
1. the arguments can be specified in any order
2. readability

cons:
1. function names must not change over time
"""

def f (x, y, z) :
    return [x, y, z]

def test1 () :
	f(2, 3, 4)
    assert f(2, z=4, y=3) == [2, 3, 4]
    # f(z=4, 2,   y=3)                 # SyntaxError: non-keyword arg after keyword arg
    # f(2,   x=2, y=3)                 # TypeError: f() got multiple values for argument 'x'
    # f(2,   a=4, y=3)                 # TypeError: f() got an unexpected keyword argument 'a'


def h (monemtum, velocity, acceleration) :
	...

h(24, 5.6, 9.4556)
h(momentum=24, velocity=5.6)

    def test6 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                print()
                print(f.__name__)
                if f.__name__ == "factorial" :
                    t = timeit.timeit(
                        "math." + f.__name__ + "(100)",
                        "import math",
                        number = 1000)
                else :
                    t = timeit.timeit(
                        "__main__." + f.__name__ + "(100)",
                        "import __main__",
                        number = 1000)
                print(f"{t*1000:.2f} milliseconds")


def g (x, *, y, z) : # * can only occur once, and it can NOT be last
    return [x, y, z]

def test2 () :
    # g(2, 3, 4)                         # TypeError: f() takes 1 positional argument but 3 were given
    assert g(2,   z=4, y=3) == [2, 3, 4]
    assert g(x=2, z=4, y=3) == [2, 3, 4]

def timeit (s1, s2, *, number) :
	...



def main () :
    print("FunctionKeywords.py")
    for i in range(2) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()




#!/usr/bin/env python3

# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = line-too-long
# pylint: disable = missing-docstring

# --------------------
# FunctionUnpacking.py
# --------------------

"""
* is an iterable unpacking
* and pass by position have the same precedence, processed left to right
* and pass by name do NOT have the same precedence, * goes first
"""

def f (x, y, z) :
    return [x, y, z]

def test1 () :
    t = (3, 4)
    assert f(2, 5, t) == [2, 5, (3, 4)]
    assert f(2, *t)   == [2, 3, 4]      # order matters
    assert f(*t,  2)  == [3, 4, 2]
    assert f(z=2, *t) == [3, 4, 2]      # unpacking goes first, order doesn't matter
    assert f(*t, z=2) == [3, 4, 2]
    # f(x=2, *t)                        # TypeError: f() got multiple values for argument 'x'
    # f(*t,  x=2)                       # TypeError: f() got multiple values for argument 'x'

def test2 () :
    u = (2, 3)
    v = (4,)
    d = {2:"abc", 3:"def"}

    for x in d :
    	print(x) # 2 3

    assert f(*u, *v) == [2, 3, 4]
    assert  [*u, *v] == [2, 3, 4]
    assert  (*u, *v) == (2, 3, 4)
    assert  {*u, *v} == {2, 3, 4}
    print([*d]) # [2, 3], but I'm not sure about the order
    print((*d)) # (2, 3), but I'm not sure about the order
    print({*d}) # {2, 3}

"""
** is a dict unpacking
** MUST follow any pass by position
** MUST follow *
** and pass by name have the same precedence, but there has to be NO conflict
"""

def f (x, y, z) :
    return [x, y, z]

def test3 () :
    d = {"x" : 4, "y" : 3, "x" : 2}
    assert f(**d) == [2, 3, 4]

def test4 () :
    d = {"z" : 4, "y" : 3}
    assert f(2,   **d) == [2, 3, 4]
    # f(**d, 2)                       # SyntaxError: invalid syntax
    assert f(x=2, **d) == [2, 3, 4]
    assert f(**d, x=2) == [2, 3, 4]
    # assert f(z=2, **d) == [2, 3, 4] # TypeError: f() got multiple values for keyword argument 'z'
    # assert f(**d, z=2) == [2, 3, 4] # TypeError: f() got multiple values for keyword argument 'z'

def test5 () :
    t = (2, 3)
    d = {"z" : 4}
    assert f(*t, **d) == [2, 3, 4]
    # f(**d, *t)                      # SyntaxError: iterable argument unpacking follows keyword argument unpacking

def test6 () :
    u = {"x":2, "y":3}
    v = {"z":4}
    assert f(**u, **v) == [2, 3, 4]
    assert {**u, **v}  == {"x": 2, "y": 3, "z": 4}

def main () :
    print("FunctionUnpacking.py")
    for i in range(6) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
