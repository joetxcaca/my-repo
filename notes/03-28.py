# -----------
# Mon, 28 Mar
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
function tuple
function dict
regexps
"""

"""
three tokens:   =, *, **
two   contexts: function definition, function call
"""

def f (x, y, z=5) : # has to be the last arguments
	...

def f (x, y, z) :
	...

f(2, 3, z=4) # has to be the last arguments

def f (x, y, *, z) # only once, it must NOT be last
	...

f(2, 3, 4)   # no
f(2, 3, z=4) # yes

f(2, 3, *u, *v) # iterable unpacking

def f (x, y, z, t) :
	...

d1 = {"z":5}
d2 = {"t":6}

f(2, 3, **d1, **d2) # dict unpacking, keys must match arg names


#!/usr/bin/env python3

# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ----------------
# FunctionTuple.py
# ----------------

def f (x, y, *t) : # tuple packing, only once, must be last or next to last
    return [x, y, t]

def test1 () :
    assert f(2, 3)       == [2, 3, ()]
    assert f(2, 3, 4)    == [2, 3, (4,)]
    assert f(2, 3, 4, 5) == [2, 3, (4, 5)]

def test2 () :
    t = (3, 4)
    assert f(2, 5,  t)  == [2, 5, ((3, 4),)]
    assert f(2, 5, *t)  == [2, 5, (3, 4)]
    assert f(2, *t)     == [2, 3, (4,)]
    assert f(*t)        == [3, 4, ()]

def main () :
    print("FunctionTuple.py")
    for i in range(2) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()


#!/usr/bin/env python3

# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ---------------
# FunctionDict.py
# ---------------

def f (x, y, **d) : # dict packing, only once, must be last
    return [x, y, d]

def test1 () :
    assert f(2, 3)           == [2, 3, {}]
    assert f(2, 3, a=4)      == [2, 3, {'a': 4}]
    assert f(2, 3, a=4, b=5) == [2, 3, {'a': 4, 'b': 5}]

def test2 () :
    d = {"b": 4, "a": 3}
    assert f(2, 5,   **d)  == [2, 5, {'a': 3, 'b': 4}]
    assert f(2, y=5, **d)  == [2, 5, {'a': 3, 'b': 4}]
    u = (2,)
    assert f(y=5, *u,  **d) == [2, 5, {'a': 3, 'b': 4}]
    assert f(*u,  y=5, **d) == [2, 5, {'a': 3, 'b': 4}]

def test3 () :
    d = {"y": 3, "a": 2}
    assert f(2,   **d) == [2, 3, {'a': 2}]
    assert f(x=2, **d) == [2, 3, {'a': 2}]

def main () :
    print("FunctionDict.py")
    for i in range(3) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()

def f (*t, **d) :
	...

f(2, 3, x=4, y=5, *u, *v, **d1, **d2)


"""
regular expressions
	1. editors
	2. grep, a Linux command
	3. in programming languages
"""

john smith
jane doe
...

# search for
(.*) (.*)

# replace with
\2 \1
