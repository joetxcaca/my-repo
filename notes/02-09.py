# -----------
# Wed,  9 Feb
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
	https://forms.gle/evXiWYUc6wqHzffb6
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

"""
Quiz #7
"""

"""
first competitive programming contest
Fri, 11 Feb, 5:30 - 8 pm CT
Zoom or GDC auditorium
free food!
"""

#!/usr/bin/env python3

# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = line-too-long
# pylint: disable = literal-comparison
# pylint: disable = missing-docstring

# -------------
# Exceptions.py
# -------------

# https://docs.python.org/3/library/exceptions.html

def f (b: bool) -> int :
    if b :
        raise NameError("abc") # creating a NameError object, one-arg constructor
    return 0

def test1 () -> None :
    try :
        assert f(False) == 0
    except NameError :       # pragma: no cover
        assert False
    else :                   # no exception vs. raised and handled, but not with break, continue, return
        pass
    finally :                # always, even with break, continue, return
        pass

def test2 () -> None :
    try :
        assert f(True) == 1
        assert False                         # pragma: no cover
    except NameError as e : # e is a reference (address) to the NameError object
        assert isinstance(e,      NameError)
        assert isinstance(e.args, tuple)
        assert len(e.args)  ==     1
        assert e.args       is not ("abc",)
        assert e.args       ==     ("abc",)
    else :                                   # no exception vs. raised and handled, but not with break, continue, return
        assert False                         # pragma: no cover
    finally :                                # always, even with break, continue, return
        pass

def test3 () -> None :
    assert issubclass(NameError,     Exception)
    assert issubclass(Exception,     BaseException)
    assert issubclass(BaseException, object)

def main () -> None :
    print("Exceptions.py")
    for i in range(3) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()

a = [2, 3, 4]
b = [2, 3, 4]
print(a == b) # value    comparison, true, NOT like Java's ==, it is like Java's .equal()
print(a is b) # identity comparison, false

a = [2, 3, 4]
b = a
print(a == b) # true
print(a is b) # true

# this is Java

class A {}

x = new A();
y = new A();
System.out.println(x.equals(y)) # identity comparison, false

a = [2, 3, 4]
print(type(a)) # list

a = [2, 3]
print(type(a)) # list

a = [2]
print(type(a)) # list

a = (2, 3, 4)
print(type(a)) # tuple, immutable list, BOTH in content and structure

a = (2, 3)
print(type(a)) # tuple

a = (2)
print(type(a)) # int!!!

a = (2,)
print(type(a)) # tuple
