# -----------
# Mon,  4 Apr
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
select
	a relation (list of dicts)
	unary predicate (a one-arg function that returns a bool)

return a generator that iterates over only the rows that satisfy the predicate
"""

"""
select as a function
"""

def select (r, up) :
	... # must use yield, which automatically raise StopIteration
	    # can NOT assume that r is indexable
	    # must NOT raise StopIteration


"""
select as a class
"""

class select :
# can NOT assume that r is indexable
# must NOT raise StopIteration
	__iter__
	__next__
	__init__

def test0 () :
    r = [
        {"A" : 1, "B" : 4, "C" : 3},
        {"A" : 2, "B" : 5, "C" : 2},
        {"A" : 3, "B" : 6, "C" : 1}]
    x = select(r, lambda d : False)
    assert list(x) == []

def test1 () :
    r = [
        {"A" : 1, "B" : 4, "C" : 3},
        {"A" : 2, "B" : 5, "C" : 2},
        {"A" : 3, "B" : 6, "C" : 1}]
    x = select(r, lambda d : True)
    assert                            \
        list(x)                       \
        ==                            \
        [{"A" : 1, "B" : 4, "C" : 3},
         {"A" : 2, "B" : 5, "C" : 2},
         {"A" : 3, "B" : 6, "C" : 1}]
    assert list(x) == []

def test2 () :
    r = [
        {"A" : 1, "B" : 4, "C" : 3},
        {"A" : 2, "B" : 5, "C" : 2},
        {"A" : 3, "B" : 6, "C" : 1}]
    x = select(r, lambda d : d["B"] > 4)
    assert                               \
        list(x)                          \
        ==                               \
        [{'A': 2, 'B': 5, 'C': 2},
         {'A': 3, 'B': 6, 'C': 1}]
    assert list(x) == []

def test3 () :
    r = [
        {"A" : 1, "B" : 4, "C" : 3},
        {"A" : 2, "B" : 5, "C" : 2},
        {"A" : 3, "B" : 6, "C" : 1}]
    x = select(r, lambda d : d["A"] > d["C"])
    assert                                    \
        list(x)                               \
        ==                                    \
        [{'A': 3, 'B': 6, 'C': 1}]
    assert list(x) == []




class select_class_while :
    def __init__ (self, r, f) :
        self.p = iter(r)
        self.f = f

    def __iter__ (self) :
        return self

    def __next__ (self) :
        while True :
            d = next(self.p)
            if self.f(d) :
                return d


class select_class_recursion :
    def __init__ (self, r, f) :
        self.p = iter(r)
        self.f = f

    def __iter__ (self) :
        return self

    def __next__ (self) :
        d = next(self.p)
        if self.f(d) :
            return d
        return next(self)


def select_function_yield (r, f) :
    for d in r :
        if f(d) :
            yield d

def select_function_generator (r, f) :
    return (d for d in r if f(d))

def select_function_filter (r, f) :
    return filter(f, r)
