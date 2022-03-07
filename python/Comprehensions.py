#!/usr/bin/env python3

# pylint: disable = consider-using-dict-items
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = no-member

# -----------------
# Comprehensions.py
# -----------------

# https://docs.python.org/3.9/tutorial/datastructures.html

import types

def test1 () :
    a = [2, 3, 4]
    b = []
    for v in a :
        b += [v * v]
    assert isinstance(b, list)
    assert a       == [2, 3,  4]
    assert b       == [4, 9, 16]

def test2 () :
    a = [2, 3, 4]
    b = [v * v for v in a]       # list comprehension, O(n), eager
    assert isinstance(b, list)
    assert a       == [2, 3,  4]
    assert b       == [4, 9, 16]

def test3 () :
    a = [2, 3, 4]
    g = (v * v for v in a)                    # generator, O(1), lazy
    assert isinstance(g, types.GeneratorType)
    assert     hasattr(g, "__next__")
    assert     hasattr(g, "__iter__")
    assert not hasattr(g, "__getitem__")
    assert not hasattr(g, "__len__")
    assert iter(g) is g
    assert a       == [2, 3,  4]
    assert list(g) == [4, 9, 16]
    assert list(g) == []

def test4 () :
    a  = [2, 3, 4]
    g  = (v * v for v in a)          # capture the list, NOT a
    a += [5]                         # change  the list, NOT a
    assert a       == [2, 3,  4,  5]
    assert list(g) == [4, 9, 16, 25]
    assert list(g) == []
    a += [5]
    assert list(g) == []

def test5 () :
    a = [2, 3, 4]
    g = (v * v for v in a)           # capture the list, NOT a
    a = [2, 3, 4, 5]                 # change a,         NOT the list
    assert a       == [2, 3,  4,  5]
    assert list(g) == [4, 9, 16]
    assert list(g) == []

def test6 () :
    a = [2, 3, 4]
    m = map(lambda v : v * v, a)
    assert isinstance(m, map)
    assert     hasattr(m, "__next__")
    assert     hasattr(m, "__iter__")
    assert not hasattr(m, "__getitem__")
    assert not hasattr(m, "__len__")
    assert iter(m) is m
    assert a       == [2, 3,  4]
    assert list(m) == [4, 9, 16]
    assert list(m) == []

def test7 () :
    a = [2, 3, 4]
    m = map(lambda v : v * v, a)     # capture the list, NOT a
    a += [5]                         # change  the list, NOT a
    assert a       == [2, 3,  4,  5]
    assert list(m) == [4, 9, 16, 25]
    assert list(m) == []
    a += [5]
    assert list(m) == []

def test8 () :
    a = [2, 3, 4]
    b = [5, 6, 7]
    m = map(lambda x, y : x + y, a, b)
    assert list(m) == [7, 9, 11]
    assert list(m) == []

def test9 () :
    a = [2, 3, 4]
    b = [5, 6, 7]
    m = (x + y for x, y in zip(a, b))
    assert list(m) == [7, 9, 11]
    assert list(m) == []

def test10 () :
    a = [2, 3, 4, 5, 6]
    b = []
    for v in a :
        if v % 2 :
            b += [v * v]
    assert a == [2, 3, 4,  5,  6]
    assert b == [   9,    25]

def test11 () :
    a = [2, 3, 4, 5, 6]
    b = [v * v for v in a if v % 2]
    assert a == [2, 3, 4,  5,  6]
    assert b == [   9,    25]

def test12 () :
    a = [2, 3, 4, 5, 6]
    g = (v * v for v in a if v % 2)
    assert a       == [2,  3,  4,  5,  6]
    assert list(g) == [    9,     25]
    assert list(g) == []

def test13 () :
    a = [2, 3, 4, 5, 6]
    f = filter(lambda v : v % 2, a)
    assert isinstance(f, filter)
    assert     hasattr(f, "__next__")
    assert     hasattr(f, "__iter__")
    assert not hasattr(f, "__getitem__")
    assert not hasattr(f, "__len__")
    assert iter(f) is f
    m = map(lambda v : v * v, f)
    assert a       == [2,  3,  4,  5,  6]
    assert list(m) == [    9,     25]
    assert list(f) == []
    assert list(m) == []

def test14 () :
    a = [2, 3, 4, 5, 6]
    f = (v for v in a if v % 2)
    m = (v * v for v in f)
    assert a       == [2,  3,  4,  5,  6]
    assert list(m) == [    9,     25]
    assert list(f) == []
    assert list(m) == []

def test15 () :
    a = [2, 3, 4]
    b = [4, 5]
    c = []
    for v in a :
        for w in b :
            c += [v + w]
    assert a == [2, 3, 4]
    assert b == [4, 5]
    assert c == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5]
    assert c == [  6,   7,   7,   8,   8,   9]

def test16 () :
    a = [2, 3, 4]
    b = [4, 5]
    c = [v + w for v in a for w in b]
    assert a == [2, 3, 4]
    assert b == [4, 5]
    assert c == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5]
    assert c == [  6,   7,   7,   8,   8,   9]

def test17 () :
    a = [2, 3, 4]
    b = [4, 5]
    g = (v + w for v in a for w in b)
    assert a       == [2, 3, 4]
    assert b       == [4, 5]
    assert list(g) == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5]
    assert list(g) == []

def test18 () :
    s = {2, 3, 4}
    t = set()
    for v in s :
        t |= {v * v}
    assert s == {2, 3,  4}
    assert t == {4, 9, 16}

def test19 () :
    s = {2, 3, 4}
    t = {v * v for v in s} # set comprehension, O(n), eager
    assert s == {2, 3,  4}
    assert t == {4, 9, 16}

def test20 () :
    d = {2: "abc", 3: "def", 4: "ghi"}
    e = {}
    for k in d :
        e[k + 1] = d[k] + "xyz"
    assert d == {2: "abc",    3: "def",    4: "ghi"}
    assert e == {3: "abcxyz", 4: "defxyz", 5: "ghixyz"}

def test21 () :
    d = {2: "abc", 3: "def", 4: "ghi"}
    e = {k + 1: d[k] + "xyz" for k in d}                # dict comprehension, O(n), eager
    assert d == {2: "abc",    3: "def",    4: "ghi"}
    assert e == {3: "abcxyz", 4: "defxyz", 5: "ghixyz"}

def main () :
    print("Comprehensions.py")
    for i in range(21) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
