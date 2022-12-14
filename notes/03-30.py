# -----------
# Wed, 30 Mar
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
Paper #9: Paper #10: Why getter and setter methods are evil
remember to go to Perusall THROUGH Canvas
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
regexps
select
"""

"""
regular expressions
	1. editors
	2. grep, a Linux command
	3. in programming languages
"""

#!/usr/bin/env python3

# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = no-member
# pylint: disable = no-name-in-module
# pylint: disable = redefined-builtin

# ----------
# RegExps.py
# ----------

# https://docs.python.org/3/library/re.html

import re # split, compile, M, Pattern, search, Match

def test1 () :
    s = "b ab\naab 123"
    a = re.split("ab", s)
    assert isinstance(a, list)
    assert a == ['b ', '\na', ' 123']

def test2 () :
    s = "b ab\naab 123"
    a = re.split("ba", s)
    assert isinstance(a, list)
    assert a == [s]

def test3 () :
    s = "b ab\naab 123"
    a = re.split("^b", s)            # start of string
    assert isinstance(a, list)
    assert a == ['', ' ab\naab 123']

def test4 () :
    s = "b ab\naab 123"
    a = re.split("^a", s)      # start of string
    assert isinstance(a, list)
    assert a == [s]

def test5 () :
    s = "b ab\naab 123"
    r = re.compile("^a", re.M)       # multiline
    assert isinstance(r, re.Pattern)
    a = r.split(s)                   # re.Pattern.split(), NO re.split()
    assert isinstance(a,      list)
    assert a == ['b ab\n', 'ab 123']

def test6 () :
    s = "b ab\naab 123"
    a = re.split("3$", s)            # end of string
    assert isinstance(a, list)
    assert a == ['b ab\naab 12', '']

def test7 () :
    s = "b ab\naab 123"
    a = re.split("b$", s)      # end of string
    assert isinstance(a, list)
    assert a == [s]

def test8 () :
    s = "b ab\naab 123"
    r = re.compile("b$", re.M)       # multiline
    assert isinstance(r, re.Pattern)
    a = r.split(s)
    assert isinstance(a,      list)
    assert a == ['b a', '\naab 123']

def test9 () :
    s = "b ab\naab 123"
    a = re.split(".", s)                                           # any character, BUT specials
    assert isinstance(a, list)
    assert a == ['', '', '', '', '\n', '', '', '', '', '', '', '']

def test10 () :
    s = "b ab\naab 123"
    a = re.split(r"\d", s)                 # any digit
    assert isinstance(a, list)
    assert a == ['b ab\naab ', '', '', '']

def test11 () :
    s = "b ab\naab 123"
    a = re.split(r"\D", s)                                  # any non-digit
    assert isinstance(a, list)
    assert a == ['', '', '', '', '', '', '', '', '', '123']

def test12 () :
    s = "b ab\naab 123"
    a = re.split(r"\w", s)                                   # any alphanumeric
    assert isinstance(a, list)
    assert a == ['', ' ', '', '\n', '', '', ' ', '', '', '']

def test13 () :
    s = "b ab\naab 123"
    a = re.split(r"\W", s)                # any non-alphanumeric
    assert isinstance(a, list)
    assert a == ['b', 'ab', 'aab', '123']

[afg]
[a-z]
[^a]  # ^ means NOT

def test14 () :
    s = "b ab\naab 123"
    m = re.search("(a*)b([^a]*)(a*)b", s) # * is zero or more
    assert isinstance(m, re.Match)
    assert m.group(0) == "b ab"    # re.Match.group()
    assert m.group(1) == ""
    assert m.group(2) == " "
    assert m.group(3) == "a"
    try :
        m.group(4)
        assert False
    except IndexError :
        pass

def test15 () :
    s = "b ab\naab 123"
    m = re.search("(a+)b([^a]*)(a+)b", s) # + is one or more
    assert isinstance(m, re.Match)
    assert m.group(0) == "ab\naab"
    assert m.group(1) == "a"
    assert m.group(2) == "\n"
    assert m.group(3) == "aa"
    try :
        m.group(4)
        assert False
    except IndexError :
        pass

def test16 () :
    s = "b ab\naab 123"
    m = re.search("((a?)b([^a]*))(a?)b", s) # ? is zero or one
    assert isinstance(m, re.Match)
    assert m.group(0) == "b ab"
    assert m.group(1) == "b "
    assert m.group(2) == ""
    assert m.group(3) == " "
    assert m.group(4) == "a"
