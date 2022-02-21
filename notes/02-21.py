# -----------
# Mon, 21 Feb
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
Paper #5: Single Responsibility Principle
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

#!/usr/bin/env python3

# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# -------------
# FactorialT.py
# -------------

# https://docs.python.org/3.6/library/math.html

import functools
import math
import operator
import timeit
import unittest

# recursive procedure
# linear recursive process
# 15 milliseconds
def factorial_recursion (n: int) -> int :
    assert n >= 0
    if n < 2 :
        return 1
    return n * factorial_recursion(n - 1)





# recursive procedure
# linear iterative process
# 20 milliseconds
def factorial_tail_recursion (n: int, v: int = 1) -> int :
    assert n >= 0
    assert v >= 1
    if n < 2 :
        return v
    return factorial_tail_recursion(n - 1 , n * v)




# iterative procedure
# linear iterative process
# 10 milliseconds
def factorial_while (n: int) -> int :
    assert n >= 0
    v = 1
    while n > 1 :
        v *= n
        n -= 1
    return v





# iterative procedure
# linear iterative process
# 7 milliseconds
def factorial_range_for (n: int) -> int :
    assert n >= 0
    v = 1
    for i in range(1, n + 1) :
        v *= i
    return v

x = range(10)      # O(1)
x = range(1000000) # O(1)

a = [2, 3, 4]
print(type(a)) # list

for v in a :
	print(v)

# 2 3 4

# requirements on a?

v = next(a) # no

# Java

ArrayList x = new ArrayList(...);
System.out.println(x.next());     # no

Iterator p = x.iterator();        # iterator object
System.out.println(p.next());     # first element

# use p.hasNext() to see if there are elements left

# Python

a = [2, 3, 4]
print(type(a)) # list

p = iter(a)
print(type(p)) # list iterator

print(next(p)) # 2
print(next(p)) # 3
...

# raise StopIteration when it's done

"""
why can't i invoke next on a Python list or a Java container?
to accommodate multiple clients iterating over the same container simultaneously
"""

for v in a :
	print(v)

# requirements on a? a must be iterable

"""
to be iterable
	1. respond to iter() by returning an iterator
	2. the iterator responds to next()
	3. next() eventually raises StopIteration
"""

"""
how can I rewrite a for loop without using for
"""

p = iter(a)
try :
	while True :
		v = next(p)
		print(v)
except StopIteration
	pass




# iterative procedure
# linear iterative process
# 7 milliseconds
def factorial_range_for (n: int) -> int :
    assert n >= 0
    v = 1
    for i in range(1, n + 1) :
        v *= i
    return v

# iterative procedure
# linear iterative process
# 10 milliseconds
def factorial_range_iterator (n: int) -> int :
    assert n >= 0
    v = 1
    p = iter(range(1, n + 1))
    try :
        while True :
            i  = next(p)
            v *= i
    except StopIteration :
        pass
    return v





def my_mul (x, y) :
    return x * y

# iterative procedure
# linear iterative process
# 9 milliseconds
def factorial_range_reduce_1 (n: int) -> int :
    assert n >= 0
    return functools.reduce(my_mul, range(1, n + 1), 1)

"""
reduce takes three arguments
	1. a binary function
	2. an iterable
	3. a seed
"""

"""
this is what reduce does:
	seed <bf> 1st <bf> 2nd <bf> ... <bf> nth
"""

"""
binary function: addition
iterator: a set of ints
seed: 0

result: sum
"""

"""
binary function: multiplication
iterator: a set of ints
seed: 0

result: 0
"""

"""
binary function: multiplication
iterator: a set of ints
seed: 1

result: product
"""

"""
binary function: multiplication
iterator: [1..n]
seed: 1

result: factorial
"""



# iterative procedure
# linear iterative process
# 10 milliseconds
def factorial_range_reduce_2 (n: int) -> int :
    assert n >= 0
    return functools.reduce(lambda x, y : x * y, range(1, n + 1), 1)



# iterative procedure
# linear iterative process
# 6 milliseconds
def factorial_range_reduce_3 (n: int) -> int :
    assert n >= 0
    return functools.reduce(operator.mul, range(1, n + 1), 1)





class MyUnitTests (unittest.TestCase) :
    def setUp (self) : # runs 7 times, once before every test
        self.a = [
            factorial_recursion,
            factorial_tail_recursion,
            factorial_while,
            factorial_range_for,
            factorial_range_iterator,
            factorial_range_reduce_1,
            factorial_range_reduce_2,
            factorial_range_reduce_3,
            math.factorial]

    def test0 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(0), 1)

    def test1 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(1), 1)

    def test2 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(2), 2)

    def test3 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(3), 6)

    def test4 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(4), 24)

    def test5 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(5), 120)

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

if __name__ == "__main__" : # pragma: no cover
    unittest.main()

""" #pragma: no cover
% FactorialT.py
......
factorial_recursion
14.66 milliseconds

factorial_tail_recursion
19.34 milliseconds

factorial_while
9.47 milliseconds

factorial_range_for
6.42 milliseconds

factorial_range_iterator
9.66 milliseconds

factorial_range_reduce_1
9.31 milliseconds

factorial_range_reduce_2
9.97 milliseconds

factorial_range_reduce_3
5.61 milliseconds

factorial
0.88 milliseconds
.
----------------------------------------------------------------------
Ran 7 tests in 0.086s

OK
"""
