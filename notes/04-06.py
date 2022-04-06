# -----------
# Wed,  6 Apr
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
Paper #11: More getters and setters
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
11. relational algebra is closed on all operations
"""

"""
relational algebra
	select
		a relation
		a unary predicate (one-arg function that returns a bool)
		returns a relation with same number of cols, less than or equal the number of rows

	project
		a relation
		the col names
		returns a relation with same number of rows, less than or equal the number of cols
"""

"""
movie table (movies)

title       genre     director         year
"star wars" "sci-fi"  "george lucas"   1977
"shane"     "western" "george stevens" 1954
...
"""

movies = \
	[
	{"title":"star wars", "genre":"sci-fi", "director":"george lucas", "year":1977}
	...
	]

def select (r, up) :
	...

select(movies, lambda d : d["year"] > 1970 and d["year"] < 2000)

# r is iterable, but NOT indexable
# do NOT raise StopIteration

class project :
	# NO yield
	init (self, r, *t)
	next
	iter

def project (r, *t) :
	... # use yield

project(movies, "genre", "year")

def test0 () :
    r = [
        {"A" : 1, "B" : 4, "C" : 3},
        {"A" : 2, "B" : 5, "C" : 2},
        {"A" : 3, "B" : 6, "C" : 1}]
    x = project(r, "D")
    assert           \
        list(x)      \
        ==           \
        [{}, {}, {}]
    assert list(x) == []

def test1 () :
    r = [
        {"A" : 1, "B" : 4, "C" : 3},
        {"A" : 2, "B" : 5, "C" : 2},
        {"A" : 3, "B" : 6, "C" : 1}]
    x = project(r, "B")
    assert         \
        list(x)    \
        ==         \
        [{'B': 4},
         {'B': 5},
         {'B': 6}]
    assert list(x) == []

def test2 () :
    r = [
        {"A" : 1, "B" : 4, "C" : 3},
        {"A" : 2, "B" : 5, "C" : 2},
        {"A" : 3, "B" : 6, "C" : 1}]
    x = project(r, "A", "C")
    assert                           \
        list(x)                      \
        ==                           \
        [{'A': 1, 'C': 3},
         {'A': 2, 'C': 2},
         {'A': 3, 'C': 1}]
    assert list(x) == []


class project_class :
    def __init__ (self, r, *t) :
        self.p = iter(r)
        self.t = t

    def __iter__ (self) :
        return self

    def __next__ (self) :
        d = next(self.p)
        return {k : d[k] for k in self.t if k in d}

def project_function_yield_1 (r, *t) :
    for d in r :
        x = {}
        for k in t :
            if k in d :
                x[k] = d[k]
        yield x

def project_function_yield_2 (r, *t) :
    for d in r :
        yield {k : d[k] for k in t if k in d}

def project_function_generator (r, *t) :
    return ({k : d[k] for k in t if k in d} for d in r)
