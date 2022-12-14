# -----------
# Mon, 21 Mar
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
Integrated 5-Year CS BS/MS Program
https://www.cs.utexas.edu/undergraduate/academics/curriculum-degree-plans/5-year-cs-bsms/
Info Session
Tue, 29 Mar, 6 pm
Zoom
"""

"""
P3 moved to Tue, 29 Mar
decorators
"""

#!/usr/bin/env python3

# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# -------------
# Decorators.py
# -------------

import types

def f1 (n) :
    return n + 1

assert isinstance(f1, types.FunctionType)
assert hasattr(f1, "__call__")

def test1 () :
    assert f1(2) == 3

f1 = 2
f1 = 3.45





def f2 (n) :
    return n + 1

assert isinstance(f2, types.FunctionType)
assert hasattr(f2, "__call__")

def debug_function (f) :
    assert hasattr(f, "__call__")
    def g (n) :                              # must be a closure that captures f
        print(f.__name__, ":", end=" ")
        print("input =", n, ";", end=" ")
        m = f(n)
        print("output =", m, ";")
        return m
    assert isinstance(g, types.FunctionType)
    assert hasattr(g, "__call__")
    return g

assert isinstance(debug_function, types.FunctionType)
assert hasattr(debug_function, "__call__")

f2 = debug_function(f2)
assert isinstance(f2, types.FunctionType)
assert hasattr(f2, "__call__")

def test2 () :
    assert f2(2) == 3 # f2 : input = 2 ; output = 3 ;

@debug_function
def f3 (n) :
    return n + 1

"""
1. define f3
2. call debug_function on f3
3. put the result back into f3
"""

assert isinstance(f3, types.FunctionType)
assert hasattr(f3, "__call__")

def test3 () :
    assert f3(2) == 3 # f3 : input = 2 ; output = 3 ;


@foo            # foo better be callable, it will be called with bar
def bar (...) : # result back into bar
    ...




def f4 (n) :
    return n + 1

assert isinstance(f4, types.FunctionType)
assert hasattr(f4, "__call__")

class debug_class :
    def __init__ (self, f) :
        assert hasattr(f, "__call__")
        self.f = f

    def __call__ (self, n) :
        print(self.f.__name__, ":", end=" ")
        print("input =", n, ";", end=" ")
        m = self.f(n)
        print("output =", m, ";")
        return m

assert not isinstance(debug_class, types.FunctionType)
assert hasattr(debug_class, "__call__")

f4 = debug_class(f4)                          # invoking constructor
assert not isinstance(f4, types.FunctionType)
assert isinstance(f4, debug_class)
assert hasattr(f4, "__call__")

def test4 () :
    assert f4(2) == 3 # f4 : input = 2 ; output = 3 ;

@debug_class
def f5 (n) :
    return n + 1

assert not isinstance(f5, types.FunctionType)
assert isinstance(f5, debug_class)
assert hasattr(f5, "__call__")

def test5 () :
    assert f5(2) == 3 # f5 : input = 2 ; output = 3 ;



def repeat_three (f) :
    def g () :
        for _ in range(3) :
            f()
    return g

@repeat_three
def f6 () :
    print("Hi")

def test6 () :
    f6()       # Hi Hi Hi




def repeat_N (n) :
    def h (f) :
        def g () :
            for _ in range(n) :
                f()
        return g
    return h

@repeat_N(5)
def f7 () :
    print("Bob")

"""
1. def f7
2. call repeat_N() produces h()
3. call the result of repeat_N(), which is h(), on f7
4. put that result, which is g, back into f7
"""

def test7 () :
    f7()       # Bob Bob Bob Bob Bob



def main () :
    print("Decorators.py")
    for n in range(7) :
        eval("test" + str(n + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()



n = 5
print(n) # 5

def f (n) :
	return n

print(f(5)) # 5
