# -----------
# Wed, 26 Jan
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
"""

# sample input

1 10
100 200
201 210
900 1000

# sample output

1 10 20
100 200 125
201 210 89
900 1000 174

"""
read a pair
compute the answer
output a triple: the original pair and the answer

compute the cycle length on all the numbers in the range specified by the pair
the answer is the max cycle length
"""

"""
read eval print (REPL)
"""

# sample input (alternative)

4
1 10
100 200
201 210
900 1000

# sample input (alternative)

1 10 -> "1 10" -> ["1", "10"] -> [1, 10]
100 200
201 210
900 1000
<sentinel>

"""
three styles of specifying the amount of input
	1. simply give the input, expect a read to eventually fail
	2. specify the amount beforehand
	3. a sentinel at the end
"""

"""
the skeleton comes in three parts
	1. Collatz.py,     the kernel, the computation of the solution
	2. TestCollatz.py, the test harness, using Python's unittest, a unit test framework
	3. RunCollatz.py,  the run  harness, which runs the program the way HackerRank wants
"""

"""
to submit to HackerRank
you need to MERGE Collatz.py and RunCollatz.py -> MyHackerRank.py
"""

#!/usr/bin/env python3

# --------------
# TestCollatz.py
# --------------

# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------
# imports
# -------

import unittest # main, TestCase
import Collatz  # max_cycle_length, the kernel

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # eval
    # ----

    def test_max_cycle_length_0 (self) :
        self.assertEqual(Collatz.max_cycle_length(1, 10), 20)

    def test_max_cycle_length_1 (self) :
        self.assertEqual(Collatz.max_cycle_length(100, 200), 125)

    def test_max_cycle_length_2 (self) :
        self.assertEqual(Collatz.max_cycle_length(201, 210), 89)

    def test_max_cycle_length_3 (self) :
        self.assertEqual(Collatz.max_cycle_length(900, 1000), 174)

# ----
# main
# ----

if __name__ == "__main__" : #pragma: no cover
    unittest.main()

#!/usr/bin/env python3

# -------------
# RunCollatz.py
# -------------

# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------
# imports
# -------

import sys
import Collatz # the kernel

# ----
# main
# ----

def main () :
    for s in sys.stdin : # what is the type of s? string
        # ----
        # read
        # ----

        a = [int(v) for v in s.split()] # what is the return type of split()? list of strings
										# build another list with the int constructor applied to each string
        # ----
        # eval
        # ----

        v = Collatz.max_cycle_length(*a) # how many args does max_cycle_length()? 2 args

        # -----
        # print
        # -----

        print(*a, v) # how many args are we feeding print()? 3

if __name__ == "__main__" :
    main()



#!/usr/bin/env python3

# ----------
# Collatz.py
# ----------

# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ----------------
# max_cycle_length
# ----------------

def max_cycle_length (i: int, j: int) -> int :
    assert i > 0
    assert j > 0

    # <your code>
    v = i + j     # replace!

    assert v > 0
    return v
