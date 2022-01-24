# -----------
# Mon, 24 Jan
# -----------

"""
Class Modality
	first two weeks on Zoom, you're welcome to go to physical room (PAR 301)

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
	5.9.1
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
	https://docs.google.com/forms/d/1JHbXAC3itO-6L9bRFdT7e0ELwg9V70DGFkfnK3GHFdI/
"""

"""
cold calling
specifications grading
huge disconnect between lectures and Web project
"""

"""
Google Sheet: grades tracker
Google Form: virtual tokens
Twitter: #utcsoopswe
"""

#!/usr/bin/env python3

# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# --------
# Hello.py
# --------

# https://www.python.org
# https://docs.python.org/3.9/
# https://docs.python.org/3.9/library/
# https://www.pylint.org
# https://www.python.org/dev/peps/pep-0008/

# compared to Java's line  comment: //
# compared to Java's block comment: /* */

"""
a python scripts has
	1. definitions
	2. top-level code

two ways to run a python script
	1. directly
		I want the definitions AND the top-level code to run
		__name__ will be set to "__main__"
	2. importing it from another script (NOT from the interpreter)
		I do NOT want top-level code, I only want definitions
		__name__ will be set to the name of the importing script
"""

if __name__ == "__main__" :      # pragma: no cover
    print("Nothing to be done.")

""" #pragma: no cover
Developed in 1989 by Guido van Rossum of the Netherlands, now at Dropbox.
Python is procedural, object-oriented, dynamically typed, and garbage collected.

Python 2: 2000
Python 3: 2008



% which python3
/usr/local/bin/python3



% python3 --version
Python 3.9.10



% python3 -- help
...



% python3 Hello.py
Nothing to be done.



% chmod ugo+x Hello.py
% ./Hello.py
Nothing to be done.



% python3
Python 3.9.10 (main, Jan 15 2022, 11:48:04)
[Clang 13.0.0 (clang-1300.0.29.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

>>> import Hello
Nothing to be done.

>>> quit()



% python3
Python 3.9.10 (main, Jan 15 2022, 11:48:04)
[Clang 13.0.0 (clang-1300.0.29.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

>>> help()

Welcome to Python 3.9's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.9/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> range
...

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.

>>> quit()



% python3
Python 3.9.10 (main, Jan 15 2022, 11:48:04)
[Clang 13.0.0 (clang-1300.0.29.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!



>>> from __future__ import braces
  File "<stdin>", line 1
SyntaxError: not a chance



>>> import antigravity
...



>>> quit()
"""

"""
assertions
	validating the state of a computation
"""

"""
Collatz Conjecture (1930s)

take a pos int
if even, divide   it by 2
if odd,  multiply it by 3 and add 1
repeat until 1

in 90 years no one has been able to mathematically prove that this is true for integers
"""

5 16 8 4 2 1

"""
cycle length of  5 is 6
cycle length of 10 is 7
"""

#!/usr/bin/env python3

# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# -------------
# Assertions.py
# -------------

# https://docs.python.org/3/reference/simple_stmts.html#grammar-token-assert_stmt

def cycle_length (n: int) -> int : # mypy enables type annotation
    assert n > 0 # precondition
    c = 0
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)  # what's different between // and /
            			  # //, floor division, it always return an int, 5.0 // 2 => 2
            			  # /,  true  division, 5.0 / 2 -> 2.5, 4 / 2 -> 2
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0 # post condition
    return c

def test () -> None :
    assert cycle_length( 1) == 1 # using assert for testing
    assert cycle_length( 5) == 6
    assert cycle_length(10) == 7

if __name__ == "__main__" : # pragma: no cover
    print("Assertions.py")
    test()
    print("Done.")

""" #pragma: no cover
% Assertions.py
Assertions.py
Traceback (most recent call last):
  File "./Assertions.py", line 32, in <module>
    test()
  File "./Assertions.py", line 26, in test
    assert cycle_length( 1) == 1
  File "./Assertions.py", line 22, in cycle_length
    assert c > 0
AssertionError



% python3 -O Assertions.py # -O disables all assertions
Assertions.py
Done.
"""

"""
assertions
	good preconditions, post conditions, loop invariants
	BAD  at testing
	(what is good for testing is a unit test framework, like JUnit)
	good at programmer errors
	BAD  at user       errors
"""
