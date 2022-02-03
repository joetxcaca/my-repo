# -----------
# Fri, 28 Jan
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
Academic Integrity Quiz
"""

n + (n >> 1) + 1

# cycle length
# even, divide   by 2
# odd,  multiply by 3 and add 1

3n + 1 # always produces an even

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

(3n + 1) / 2
3n/2 + 1/2 # but, n is odd
3/2  + 1
n + n/2 + 1
n + (n >> 1) + 1

mcl(10, 100)
b = 10
e = 100
m = (e/2 + 1) = 51
# m > b
mcl(10, 100) = mcl(51, 100)
# we need to be convinced that
mcl(10, 50) # doesn't matter

mcl(200,300)
b = 200
e = 300
m = 151
# m is not > b
# no claim

mcl(1, 10)

"""
always start with the simplest solution
always take small simple steps in improving
"""

"""
first step
simplest possible solution
NO optimizations
NO caching
"""

"""
you can use checktestdata to produce random pairs
you can then run your simple solution locally, to produce the correct corresponding triples
"""

"""
second step
implement the optimizations from the quiz
rerun the tests
"""

"""
third step
implement caching
"""

"""
three kinds of caching
	1. lazy cache; we are caching as a result of reading in the test case
		an array, a Python list
		a. only store the direct numbers
		b. store the intermediate numbers
		how big should the cache be?
			1,000,000: store every possible case
			it's not obvious that this is the best choice
			try different sizes
	2. eager cache: caching before the first read
		how big should the cache be?
			1,000,000: store every possible case
			it's not obvious that this is the best choice
			try different sizes
	3. meta cache: caching outside of the HackerRank computation
		HackerRank has a limit of 50k
"""
