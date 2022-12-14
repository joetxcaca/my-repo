# -----------
# Fri,  8 Apr
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
relational algebra
	select
		a relation
		a unary predicate (a one-arg function that returns a bool)
		return a relation with less than or equal rows, same cols
	project
		a relation
		names of the cols
		return a relation with less than or equal cols, same rows
	cross join
		a relation
		a relation
		returns every combination of rows in the first and rows in the second
"""


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

class cross_join
	# no yield
	# can't assume indexable
	init (r, s)
	iter
	next

def cross_join (r, s)
	# yield
