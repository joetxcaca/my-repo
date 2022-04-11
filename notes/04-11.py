# -----------
# Mon, 11 Apr
# -----------

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
12. Python, C, Java are procedural; SQL is declarative
"""

"""
theta join
natural join
"""

class cross_join_class :
    def __init__ (self, r, s) :
        self.p = iter(r)
        self.u = next(self.p)
        self.s = s
        self.q = iter(s)

    def __iter__ (self) :
        return self

    def __next__ (self) :
        try :
            v = next(self.q)
        except StopIteration :
            self.u = next(self.p)
            self.q = iter(self.s)
            v      = next(self.q)
        return {**self.u, **v}

def cross_join_function_yield (r, s) :
    for u in r :
        for v in s :
            yield {**u, **v}

def theta_join_function_yield (r, s, bp) :
    for u in r :
        for v in s :
        	if bp(u, v) :
	            yield {**u, **v}

def cross_join_function_generator (r, s) :
    return ({**u, **v} for u in r for v in s) # generator comprehension

def theta_join_function_generator (r, s, bp) :
    return ({**u, **v} for u in r for v in s if bp(u, v)) # generator comprehension

def naturual_join (r, s) :
	def bp (u, v) :
		... # you're going to define the binary predicate
	return theta_join(r, s, bp)

def test0 () :
    r = [
        {"A" : 1, "B" : 4},
        {"A" : 2, "B" : 5},
        {"A" : 3, "B" : 6}]

    s = [
        {"C" : 2, "D" : 7},
        {"C" : 3, "D" : 5},
        {"C" : 3, "D" : 6},
        {"C" : 4, "D" : 6}]

    x = cross_join(r, s)
    assert                                 \
        list(x)                            \
        ==                                 \
        [{'A': 1, 'B': 4, 'C': 2, 'D': 7},
         {'A': 1, 'B': 4, 'C': 3, 'D': 5},
         {'A': 1, 'B': 4, 'C': 3, 'D': 6},
         {'A': 1, 'B': 4, 'C': 4, 'D': 6},
         {'A': 2, 'B': 5, 'C': 2, 'D': 7},
         {'A': 2, 'B': 5, 'C': 3, 'D': 5},
         {'A': 2, 'B': 5, 'C': 3, 'D': 6},
         {'A': 2, 'B': 5, 'C': 4, 'D': 6},
         {'A': 3, 'B': 6, 'C': 2, 'D': 7},
         {'A': 3, 'B': 6, 'C': 3, 'D': 5},
         {'A': 3, 'B': 6, 'C': 3, 'D': 6},
         {'A': 3, 'B': 6, 'C': 4, 'D': 6}]
    assert list(x) == []



"""
student table

sID sName GPA sizeHS
...
"""

"""
college table

cName state enrollment
...
"""

"""
apply table

sID cName major decision
...
"""


def test0 () :
    r = [
        {"A" : 1, "B" : 4},
        {"A" : 2, "B" : 5},
        {"A" : 3, "B" : 6}]

    s = [
        {"C" : 2, "D" : 7},
        {"C" : 3, "D" : 5},
        {"C" : 3, "D" : 6},
        {"C" : 4, "D" : 6}]

    x = theta_join(r, s, lambda u, f : False)
    assert list(x) == []

def test1 () :
    r = [
        {"A" : 1, "B" : 4},
        {"A" : 2, "B" : 5},
        {"A" : 3, "B" : 6}]

    s = [
        {"C" : 2, "D" : 7},
        {"C" : 3, "D" : 5},
        {"C" : 3, "D" : 6},
        {"C" : 4, "D" : 6}]

    x = theta_join(r, s, lambda u, f : True)
    assert                                 \
        list(x)                            \
        ==                                 \
        [{'A': 1, 'B': 4, 'C': 2, 'D': 7},
         {'A': 1, 'B': 4, 'C': 3, 'D': 5},
         {'A': 1, 'B': 4, 'C': 3, 'D': 6},
         {'A': 1, 'B': 4, 'C': 4, 'D': 6},
         {'A': 2, 'B': 5, 'C': 2, 'D': 7},
         {'A': 2, 'B': 5, 'C': 3, 'D': 5},
         {'A': 2, 'B': 5, 'C': 3, 'D': 6},
         {'A': 2, 'B': 5, 'C': 4, 'D': 6},
         {'A': 3, 'B': 6, 'C': 2, 'D': 7},
         {'A': 3, 'B': 6, 'C': 3, 'D': 5},
         {'A': 3, 'B': 6, 'C': 3, 'D': 6},
         {'A': 3, 'B': 6, 'C': 4, 'D': 6}]
    assert list(x) == []

"""
theta join
	a relation
	another relation
	binary predicate (two-arg function that returns a bool)
"""

def test2 () :
    r = [
        {"A" : 1, "B" : 4},
        {"A" : 2, "B" : 5},
        {"A" : 3, "B" : 6}]

    s = [
        {"C" : 2, "D" : 7},
        {"C" : 3, "D" : 5},
        {"C" : 3, "D" : 6},
        {"C" : 4, "D" : 6}]

    x = theta_join(r, s, lambda u, v : u["A"] == v["C"])
    assert                                 \
        list(x)                            \
        ==                                 \
        [{'A': 2, 'B': 5, 'C': 2, 'D': 7},
         {'A': 3, 'B': 6, 'C': 3, 'D': 5},
         {'A': 3, 'B': 6, 'C': 3, 'D': 6}]




def test0 () :
    r = [
        {"A" : 1, "B" : 4},
        {"A" : 2, "B" : 5},
        {"A" : 3, "B" : 6}]

    s = [
        {"C" : 2, "D" : 7},
        {"C" : 3, "D" : 5},
        {"C" : 3, "D" : 6},
        {"C" : 4, "D" : 6}]

    x = natural_join(r, s)
    assert                                 \
        list(x)                            \
        ==                                 \
        [{'A': 1, 'B': 4, 'C': 2, 'D': 7},
         {'A': 1, 'B': 4, 'C': 3, 'D': 5},
         {'A': 1, 'B': 4, 'C': 3, 'D': 6},
         {'A': 1, 'B': 4, 'C': 4, 'D': 6},
         {'A': 2, 'B': 5, 'C': 2, 'D': 7},
         {'A': 2, 'B': 5, 'C': 3, 'D': 5},
         {'A': 2, 'B': 5, 'C': 3, 'D': 6},
         {'A': 2, 'B': 5, 'C': 4, 'D': 6},
         {'A': 3, 'B': 6, 'C': 2, 'D': 7},
         {'A': 3, 'B': 6, 'C': 3, 'D': 5},
         {'A': 3, 'B': 6, 'C': 3, 'D': 6},
         {'A': 3, 'B': 6, 'C': 4, 'D': 6}]
    assert list(x) == []

def test1 () :
    r = [
        {"A" : 1, "B" : 4, "C" : 7},
        {"A" : 2, "B" : 5, "C" : 8},
        {"A" : 3, "B" : 6, "C" : 9}]

    s = [
        {"A" : 4, "B" : 4, "D" : 7},
        {"A" : 5, "B" : 5, "D" : 5},
        {"A" : 6, "B" : 6, "D" : 6},
        {"A" : 7, "B" : 7, "D" : 6}]

    x = natural_join(r, s)
    assert list(x) == []

def test2 () :
    r = [
        {"A" : 1, "B" : 4, "C" : 7},
        {"A" : 2, "B" : 5, "C" : 8},
        {"A" : 3, "B" : 6, "C" : 9}]

    s = [
        {"A" : 2, "B" : 4, "D" : 7},
        {"A" : 3, "B" : 5, "D" : 5},
        {"A" : 3, "B" : 6, "D" : 6},
        {"A" : 4, "B" : 7, "D" : 6}]

    x = natural_join(r, s)
    assert                                 \
        list(x)                            \
        ==                                 \
        [{'A': 3, 'B': 6, 'C': 9, 'D': 6}]
    assert list(x) == []



def natural_join_1 (r, s) :
    def bp (u, v) :
        for k in u :
            if (k in v) and (u[k] != v[k]) :
                return False
        return True
    return theta_join(r, s, bp)

def natural_join_2 (r, s) :
    def bp (u, v) :
        return all( u[k] == v[k] for k in u if k in v )
    return theta_join(r, s, bp)

def natural_join_3 (r, s)  :
    return theta_join(r, s, lambda u, v : all(u[k] == v[k] for k in u if k in v))

all([false, true, false]) -> false

def all (a) :
	for v in a :
		if not v :
			return False
	return True
