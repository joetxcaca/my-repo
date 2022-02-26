#!/usr/bin/env python3

# pylint: disable = chained-comparison
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = literal-comparison
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# ------------
# Operators.py
# ------------

# https://docs.python.org/3/library/operator.html
# https://docs.python.org/3/reference/datamodel.html
# https://graphics.stanford.edu/~seander/bithacks.html

import copy
import operator

def test1 () :
    i = 2
    j = -i         # negation
    assert i ==  2
    assert j == -2

def test2 () :
    i = 2
    j = 3
    k = i + j     # addition
    assert i == 2
    assert j == 3
    assert k == 5

def test3 () :
    i = 2
    j = 3
    k = operator.add(i, j) # addition
    assert i == 2
    assert j == 3
    assert k == 5

def test4 () :
    i = 2
    j = 3
    i += j        # in-place addition
    assert i == 5
    assert j == 3

def test5 () :
    i = 4
    j = 2
    f = i / j                   # true division
    assert i == 4
    assert j == 2
    assert isinstance(f, float)
    assert f == 2.0

def test6 () :
    i = 5
    j = 2
    k = i // j                # floor division
    assert i == 5
    assert j == 2
    assert isinstance(k, int)
    assert k == 2

def test7 () :
    f = 5.0
    j = 2
    g = f // j                  # floor division
    assert f == 5.0
    assert j == 2
    assert isinstance(g, float)
    assert g == 2.0

def test8 () :
    i = 5
    j = 2
    k = i % j     # mod
    assert i == 5
    assert j == 2
    assert k == 1

def test9 () :
    i = 5
    j = 2
    i %= j        # in-place mod
    assert i == 1
    assert j == 2

def test10 () :
    i = 2
    j = 3
    k = i ** j    # exponentiation
    assert i == 2
    assert j == 3
    assert k == 8

def test11 () :
    i = 2
    j = 3
    i **= j       # in-place exponentiation
    assert i == 8
    assert j == 3

def test12 () :
    i = 2
    j = ~i         # bit complement
    k = ~j
    assert i ==  2
    assert j == -3
    assert k ==  2

def test13 () :
    i = 2
    j = 3
    k = i << j     # bit shift left
    assert i ==  2
    assert j ==  3
    assert k == 16

def test14 () :
    i = 2
    j = 3
    i <<= j        # in-place bit shift left
    assert i == 16
    assert j ==  3

def test15 () :
    i = 10         # 1010
    j = 12         # 1100
    k = i & j      # 1000: bit and
    assert i == 10
    assert j == 12
    assert k ==  8

def test16 () :
    i = 10
    j = 12
    i &= j         # in-place bit and
    assert i ==  8
    assert j == 12

def test17 () :
    i = 10         # 1010
    j = 12         # 1100
    k = i | j      # 1110: bit or
    assert i == 10
    assert j == 12
    assert k == 14

def test18 () :
    i = 10
    j = 12
    i |= j         # in-place bit or
    assert i == 14
    assert j == 12

def test19 () :
    i = 10         # 1010
    j = 12         # 1100
    k = i ^ j      # 0110: bit exclusive or
    assert i == 10
    assert j == 12
    assert k ==  6

def test20 () :
    i = 10
    j = 12
    i ^= j         # in-place bit exclusive or
    assert i ==  6
    assert j == 12

def test21 () :
    i = 10
    j = 12
    i ^= j
    j ^= i
    i ^= j
    assert i == 12
    assert j == 10

def test22 () :
    a = True
    b = True
    c = False
    assert a and b
    assert not (a and c)
    assert a or b
    assert a or c

def test23 () :
    s = "abc"
    assert s[1]                 == "b" # str index
    assert s.__getitem__(1)     == "b"
    assert str.__getitem__(s,1) == "b"
    #s[1] = "d"                        # TypeError: 'str' object does not support item assignment

def test24 () :
    a = [2, 3, 4]
    assert a[1]                   == 3 # list index
    assert a.__getitem__(1)       == 3
    assert list.__getitem__(a, 1) == 3
    a[1] = 5
    a.__setitem__(1, 5)
    assert a == [2, 5, 4]

def test25 () :
    u = (2, 3, 4)
    assert u[1]                    == 3 # tuple index
    assert u.__getitem__(1)        == 3
    assert tuple.__getitem__(u, 1) == 3
    #u[1] = 5                           # TypeError: 'tuple' object does not support item assignment

def test26 () :
    a = [2, 3, 4]
    assert a[ 1] == 3
    assert a[-1] == 4

    assert a[1 : 2] == [3] # list slicing

    s = slice(1, 2)
    assert s.start                == 1
    assert s.stop                 == 2
    assert a[s]                   == [3]
    assert a.__getitem__(s)       == [3]
    assert list.__getitem__(a, s) == [3]

    assert a[ 1 : 3] == [3, 4]
    assert a[-2 : 3] == [3, 4]
    assert a[ 0 : 3] == [2, 3, 4]

    assert a[0 : 3 : 2] == [2, 4]

    s = slice(0, 3, 2)
    assert s.start                == 0
    assert s.stop                 == 3
    assert s.step                 == 2
    assert a[s]                   == [2, 4]
    assert a.__getitem__(s)       == [2, 4]
    assert list.__getitem__(a, s) == [2, 4]

    assert a[2 : -4 : -2] == [4, 2]
    assert a[:]           == [2, 3, 4]

def test27 () :
    a = [2, 3, 4]
    b = a[:]
    assert a is not b
    assert a ==     b
    b[1] += 1
    assert a == [2, 3, 4]
    assert b == [2, 4, 4]

def test28 () :
    u = (2, 3, 4)
    v = u[:]
    assert u is v

def test29 () :
    a = [2, 3, 4]
    b = copy.copy(a)
    assert a is not b
    assert a ==     b
    b[1] += 1
    assert a == [2, 3, 4]
    assert b == [2, 4, 4]

def test30 () :
    u = (2, 3, 4)
    v = copy.copy(u)
    assert u is v

def test31 () :
    a = [2, 3, 4]
    b = [1, a, 5]
    c = b[:]
    assert b    is not c
    assert b    ==     c
    assert b[1] is     c[1]

def test32 () :
    a = [2, 3, 4]
    b = [1, a, 5]
    c = copy.copy(b)
    assert b    is not c
    assert b    ==     c
    assert b[1] is     c[1]

def test33 () :
    a = [2, 3, 4]
    b = [1, a, 5]
    c = copy.deepcopy(b)
    assert b    is not c
    assert b    ==     c
    assert b[1] is not c[1]
    assert b[1] ==     c[1]

def test34 () :
    s = "a"
    t = "bc"
    u = s + t             # string concatenation
    u = s.__add__(t)
    u = str.__add__(s, t)
    assert u is not "abc"
    assert u ==     "abc"

def test35 () :
    a = [2]
    b = [3, 4]
    c = a + b                 # list concatenation
    c = a.__add__(b)
    c = list.__add__(a, b)
    assert c is not [2, 3, 4]
    assert c ==     [2, 3, 4]
    assert c !=     (2, 3, 4)

def test36 () :
    u = (2,)
    v = (3, 4)
    w = (u + v)               # tuple concatenation
    w = u.__add__(v)
    w = tuple.__add__(u, v)
    assert w is not (2, 3, 4)
    assert w ==     (2, 3, 4)
    assert w !=     [2, 3, 4]

def test37 () :
    s = "abc"
    t = s * 2                # string replication
    t = s.__mul__(2)
    t = str.__mul__(s, 2)
    assert t is not "abcabc"
    assert t ==     "abcabc"

def test38 () :
    a = [2, 3, 4]
    b = a * 2                          # list replication
    b = a.__mul__(2)
    b = list.__mul__(a, 2)
    assert b is not [2, 3, 4, 2, 3, 4]
    assert b ==     [2, 3, 4, 2, 3, 4]

def test39 () :
    u = (2, 3, 4)
    v = u * 2                          # tuple replication
    v = u.__mul__(2)
    v = tuple.__mul__(u, 2)
    assert u is not (2, 3, 4, 2, 3, 4)
    assert v ==     (2, 3, 4, 2, 3, 4)

def test40 () :
    a = [2, 3, 4]
    b = a
    assert a is b
    b += [5]
    b.__iadd__([6])
    list.__iadd__(b, [7])
    assert a == [2, 3, 4, 5, 6, 7]
    assert a is b

def test41 () :
    a = [2, 3, 4]
    b = a
    assert a is b
    b += (5,)
    b.__iadd__((6,))
    list.__iadd__(b, (7,))
    assert a == [2, 3, 4, 5, 6, 7]
    assert a is b

def test42 () :
    a = [2, 3, 4]
    b = a
    assert a is b
    b = b + [5]
    b = b.__add__([6])
    b = list.__add__(b, [7])
    assert a == [2, 3, 4]
    assert b == [2, 3, 4, 5, 6, 7]

def test43 () :
    a = [2, 3, 4]
    b = a
    assert a is b
    #b = b + (5,) # TypeError: can only concatenate list (not "tuple") to list

def test44 () :
    x = (2, 3, 4)
    y = x
    assert x is y
    y += (5,)
#   y.iadd((6,))             # AttributeError: 'tuple' object has no attribute 'iadd'
    assert x == (2, 3, 4)
    assert y == (2, 3, 4, 5)

def test45 () :
    u = (2, 3, 4)
    v = u
    assert u is v
    #v += [5]     # TypeError: can only concatenate tuple (not "list") to tuple

def test46 () :
    x = (2, 3, 4)
    y = x
    assert x is y
    y = y + (5,)
    y = y.__add__((6,))
    y = tuple.__add__(y, (7,))
    assert x == (2, 3, 4)
    assert y == (2, 3, 4, 5, 6, 7)

def test47 () :
    u = (2, 3, 4)
    v = u
    assert u is v
    #v = v + [5]  # TypeError: can only concatenate tuple (not "list") to tuple

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
    i, j = j, i
    assert i == 12
    assert j == 10

def test50 () :
    a = [2, 3]
    i, j = a
    assert i == 2
    assert j == 3

def test51 () :
    class A :
        k = 4

        def __init__ (self, i, j) :
            self.i = i
            self.j = j

    x = A(2, 3)
    assert x.i == 2
    assert x.j == 3
    assert A.k == 4

def main () :
    print("Operators.py")
    for i in range(51) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
