# -----------
# Mon, 31 Jan
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
Paper #02: 2022-01-30: Makefile
you MUST go to Perusall THROUGH Canvas
"""

"""
Project #1: Collatz
Poll: Project #1: Collatz
Academic Integrity Quiz
"""

"""
lazy cache
	on HackerRank, caching as result of reading the input
eager cache
	on HackerRank, caching is done before the first read
meta cache
	NOT on HackerRank, hardwiring the source code with the cache, < 50 K
"""

"""
what if explored caching max cycle lenghts
what if we cached max cycle lengths certain ranges

1-1000
1001-2000
2001-3000
...
999,001-1,000,000
"""

"""
mcl(500, 2500)
lookup
	1001-2000
compute
	500-1000
	2001-2500
"""

"""
I want a range size that produces the most ranges that still into 50K
"""

#!/usr/bin/env python3

# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# -------------
# UnitTests1.py
# -------------

# https://docs.python.org/3/library/unittest.html
# https://docs.python.org/3/library/unittest.html#assert-methods

import unittest # main, TestCase

def cycle_length (n: int) -> int :
    assert n > 0
    c = 0
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

class MyUnitTests (unittest.TestCase) :
    def test0 (self) :
        self.assertEqual(cycle_length( 1), 1)

    def test1 (self) :
        self.assertEqual(cycle_length( 5), 6)

    def test2 (self) :
        self.assertEqual(cycle_length(10), 7)

if __name__ == "__main__" : # pragma: no cover
    unittest.main()

""" #pragma: no cover
% ./UnitTests1T.py
FFF
======================================================================
FAIL: test0 (__main__.MyUnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/downing/Dropbox/examples/python/./UnitTests1.py", line 30, in test0
    self.assertEqual(cycle_length( 1), 1)
  File "/Users/downing/Dropbox/examples/python/./UnitTests1.py", line 25, in cycle_length
    assert c > 0
AssertionError

======================================================================
FAIL: test1 (__main__.MyUnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/downing/Dropbox/examples/python/./UnitTests1.py", line 33, in test1
    self.assertEqual(cycle_length( 5), 6)
AssertionError: 5 != 6

======================================================================
FAIL: test2 (__main__.MyUnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/downing/Dropbox/examples/python/./UnitTests1.py", line 36, in test2
    self.assertEqual(cycle_length(10), 7)
AssertionError: 6 != 7

----------------------------------------------------------------------
Ran 3 tests in 0.002s

FAILED (failures=3)
"""



#!/usr/bin/env python3

# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# -------------
# UnitTests2.py
# -------------

# https://docs.python.org/3/library/unittest.html
# https://docs.python.org/3/library/unittest.html#assert-methods

import unittest # main, TestCase

def cycle_length (n: int) -> int :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

class MyUnitTests (unittest.TestCase) :
    def test0 (self) :
        self.assertEqual(cycle_length( 1), 1)

    def test1 (self) :
        self.assertEqual(cycle_length( 5), 5)

    def test2 (self) :
        self.assertEqual(cycle_length(10), 7)

if __name__ == "__main__" : # pragma: no cover
    unittest.main()

""" #pragma: no cover
% ./UnitTests2T.py
.F.
======================================================================
FAIL: test1 (__main__.MyUnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/downing/Dropbox/examples/python/./UnitTests2.py", line 33, in test1
    self.assertEqual(cycle_length( 5), 5)
AssertionError: 6 != 5

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
"""




#!/usr/bin/env python3

# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# -------------
# UnitTests3.py
# -------------

# https://docs.python.org/3/library/unittest.html
# https://docs.python.org/3/library/unittest.html#assert-methods

import unittest # main, TestCase

def cycle_length (n: int) -> int :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

class MyUnitTests (unittest.TestCase) :
    def test0 (self) :
        self.assertEqual(cycle_length( 1), 1)

    def test1 (self) :
        self.assertEqual(cycle_length( 5), 6)

    def test2 (self) :
        self.assertEqual(cycle_length(10), 7)

if __name__ == "__main__" : # pragma: no cover
    unittest.main()

""" #pragma: no cover
% ./UnitTests3T.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
"""

#!/usr/bin/env python3

# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# ------------
# Coverage1.py
# ------------

# https://coverage.readthedocs.org

import unittest # main, TestCase

def cycle_length (n: int) -> int :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

class MyUnitTests (unittest.TestCase) :
    def test (self) :
        self.assertEqual(cycle_length(1), 1)

if __name__ == "__main__" : # pragma: no cover
    unittest.main()

""" #pragma: no cover
% which coverage
/usr/local/bin/coverage



% coverage --version
Coverage.py, version 5.5 with C extension
Full documentation is at https://coverage.readthedocs.io



% coverage --help
...



% coverage run --branch Coverage1.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK



% ls -al .coverage
-rw-r--r--@ 1 downing  staff  53248 Jan 27 14:25 .coverage



% coverage report -m
Name           Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------------
Coverage1.py      14      4      4      1    61%   19-23
----------------------------------------------------------
TOTAL             14      4      4      1    61%
"""



#!/usr/bin/env python3

# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# ------------
# Coverage2.py
# ------------

# https://coverage.readthedocs.org

import unittest # main, TestCase

def cycle_length (n: int) -> int :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

class MyUnitTests (unittest.TestCase) :
    def test (self) :
        self.assertEqual(cycle_length(2), 2)

if __name__ == "__main__" : # pragma: no cover
    unittest.main()

""" #pragma: no cover
% coverage run --branch Coverage2T.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK



% coverage report -m
Name           Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------------
Coverage2.py      14      1      4      1    89%   22
----------------------------------------------------------
TOTAL             14      1      4      1    89%
"""



#!/usr/bin/env python3

# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# ------------
# Coverage3.py
# ------------

# https://coverage.readthedocs.org

import unittest # main, TestCase

def cycle_length (n: int) -> int :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

class MyUnitTests (unittest.TestCase) :
    def test (self) :
        self.assertEqual(cycle_length(3), 8)

if __name__ == "__main__" : # pragma: no cover
    unittest.main()

""" #pragma: no cover
% coverage run --branch Coverage3T.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK



% coverage report -m
Name           Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------------
Coverage3.py      14      0      4      0   100%
----------------------------------------------------------
TOTAL             14      0      4      0   100%
"""

docker run --rm -i -t -v $(PWD):/usr/python -w /usr/python python
