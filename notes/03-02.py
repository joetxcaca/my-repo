# -----------
# Wed,  2 Mar
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
Paper #7: Liskov Substitution Principle
you MUST go to Perusall THROUGH Canvas

this is the third of a 5-paper series
SOLID design
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
"""

"""
CATME peer review
operators
iteration
"""

def test48 () :
    i = 3
    j = 5
    k = 7
    l = 8
    assert (i < j) and (j < k) and (k < l)
    assert i < j < k < l

def test49 () :
    i = 10
    j = 12
    i, j = j, i    # parallel assignment
    i, j = f(...), g(...)
    i, j, k = 2, 3, 4
    assert i == 12
    assert j == 10

def test50 () :
    a = [2, 3]
    i, j = a      # what has to be true about a? iterable of length 2
    assert i == 2
    assert j == 3


# Java

class A {
	static int k = 4; # class    variable
	int i;            # instance variable
	int j;
}

def test51 () :
    class A :
        k = 4 # class variable

        def __init__ (self, i, j) :
            self.i = i # instance variables
            self.j = j

    x = A(2, 3)
    assert x.i == 2 # instance variable
    assert x.j == 3
    assert A.k == 4 # class variable
	assert x.k == 4 # yes, misleading

a = [2, 3, 4]
print(type(a)) # list

p = iter(a)    # a.__iter__()
print(type(p)) # list iterator

print(a is p)  # false

q = iter(p)    # !!! returns p!!!
print(q is p)  # true!!!

a = deque([2, 3, 4]) # linked list, can't index

"""
we have two functions, f and g
invoke f() on the first two elements of a
invoke g() on the remaining elements of a
"""

p = iter(a)
print(type(p)) # deque iterator

f(next(p))     # p.__next__(), 1st elem
f(next(p))     # 2nd elem

try :
	while True :
		g(next(p))
except StopIteration :
	pass

for v in p :
	g(v)     # !!!!!

q = iter(p)  # q is p!!!!

try :
	while True :
		g(next(q))
except StopIteration :
	pass
