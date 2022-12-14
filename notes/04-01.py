# -----------
# Fri,  1 Apr
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
Paper #9: Why getter and setter methods are evil
remember to go to Perusall THROUGH Canvas
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
CATME
IDB3
regexps, 17
relational algebra
select
"""

import re # sub

def test17 () :
    s = "b ab\naab 123"
    t = re.sub("b ", "xx", s)
    assert s == "b ab\naab 123"
    assert t == "xxab\naaxx123"

def test18 () :
    s = "b ab\naab 123"
    t = re.sub("b.", "xx", s)
    assert s == "b ab\naab 123"
    assert t == "xxab\naaxx123"

def test19 () :
    s = "b ab\naab 123"
    t = re.sub("", "z", s)
    assert s == "b ab\naab 123"
    assert t == "zbz zazbz\nzazazbz z1z2z3z"

"""
relational algebra
"""

"""
algebra
	a set of elements
	a set of operations
	open or closed
"""

"""
integer arithmetic
	the integers
	+ (closed), - (closed), / (open), * (closed), % (closed)
"""

"""
relational algebra
	relations (tables)
	select, project, join (many flavors)
"""

"""
movie table (movies)

title       genre     director         year
"star wars" "sci-fi"  "george lucas"   1977
"shane"     "western" "george stevens" 1954
...
"""

"""
select
	a relation
	a unary predicate (a unary function that returns a bool)
	results in another relation ONLY with rows that satisfy the predicate
"""

select(movies, <((year > 1970) and (year < 2000))>)

movies = \
	[
	{"title":"star wars", "genre":"sci-fi", "director":"george lucas", "year":1977}
	...
	]

select(movies, lambda d : d["year"] > 1970 and d["year"] < 2000)

def select (r, up) :
	...
