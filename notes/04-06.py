# -----------
# Wed,  6 Apr
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
