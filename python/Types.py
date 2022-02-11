#!/usr/bin/env python3

# pylint: disable = duplicate-key
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = literal-comparison
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# --------
# Types.py
# --------

# https://docs.python.org/3.6/library/types.html

from collections import deque
from types       import FunctionType

def test1 () :
    b: bool = bool()
    c: bool = False
    assert b is c
    assert isinstance(b,    bool)
    assert isinstance(bool, type)

def test2 () :
    i: int = int()
    j: int = 0
    assert i is j
    i  = 2
    i += 1
    j  = 3
    assert i is j
    i  = 255
    i +=   1
    j  = 256
    assert i is j
    i  = 256                     # cache: [-5, 256]
    i +=   1
    j  = 257
    assert i is not j
    assert i ==     j
    i =  -4
    i -=  1
    j =  -5
    assert i is j
    i =  -5                      # cache: [-5, 256]
    i -=  1
    j =  -6
    assert i is not j
    assert i ==     j
    assert isinstance(i,   int)
    assert isinstance(int, type)

def test3 () :
    f: float = float()
    g: float = 0.0
    assert f is not g
    assert f ==     g
    assert isinstance(f,     float)
    assert isinstance(float, type)

def test4 () :
    c: complex = complex()
    d: complex = 0 + 0j
    assert c is not d
    assert c ==     d
    assert isinstance(c,       complex)
    assert isinstance(complex, type)

def test5 () :
    s: str = str()
    t: str = ""
    assert s is t
    assert isinstance(s,   str)
    assert isinstance(str, type)

def test6 () :
    a: list = list()
    b: list = []
    assert a is not b
    assert a ==     b
    a = [2, "abc", 3.45]
    assert a == [2, "abc", 3.45]
    assert a != ["abc", 2, 3.45]
    assert isinstance(a,    list)
    assert isinstance(list, type)

def test7 () :
    u: tuple = tuple()
    v: tuple = ()
    assert u is v
    u = (2, "abc", 3.45)
    assert u == (2, "abc", 3.45)
    assert u != ("abc", 2, 3.45)
    assert isinstance(u,     tuple)
    assert isinstance(tuple, type)

def test8 () :
    x: set = set()
    y: set = set()
    assert x is not y
    assert x ==     y
    x = {2, 2, "abc", 3.45}
    assert x == {2, "abc", 3.45}
    assert x == {"abc", 2, 3.45}
    assert isinstance(x,   set)
    assert isinstance(set, type)

def test9 () :
    x: frozenset = frozenset()
    y: frozenset = frozenset()
    assert x is y
    y = frozenset((2, 2, "abc", 3.45))
    assert y == frozenset([2, "abc", 3.45])
    assert y == frozenset(["abc", 2, 3.45])
    assert isinstance(y,         frozenset)
    assert isinstance(frozenset, type)

def test10 () :
    d: dict = dict()
    e: dict = {}
    assert d is not e
    assert d ==     e
    d = {2: "xxx", 2: "abc", 3: "def", 4: "ghi"}
    assert d == {2: "abc", 3: "def", 4: "ghi"}
    assert d == {3: "def", 2: "abc", 4: "ghi"}
    assert isinstance(d,    dict)
    assert isinstance(dict, type)

def test11 () :
    q = deque()
    r = deque()
    assert q is not r
    assert q ==     r
    q = deque((2, "abc", 3.45))
    assert q == deque((2, "abc", 3.45))
    assert q != deque(("abc", 2, 3.45))
    assert isinstance(q,     deque)
    assert isinstance(deque, type)

def test12 () :
    def f (v) :
        return v + 1
    assert isinstance(f,            FunctionType)
    assert isinstance(FunctionType, type)

def test13 () :
    f: FunctionType = lambda v : v + 1
    assert isinstance(f,            FunctionType)
    assert isinstance(FunctionType, type)

def test14 () :
    class A :
        def __init__ (self, i, s, f) :
            self.i = i
            self.s = s
            self.f = f

    x = A(2, "abc", 3.45)
    y = A(2, "abc", 3.45)
    assert x is not y
    assert x !=     y
    assert isinstance(x,    A)
    assert isinstance(x,    object)
    assert isinstance(A,    type)
    assert isinstance(type, type)

    assert issubclass(A, A)
    assert issubclass(A, object)

    assert issubclass(type, type)
    assert issubclass(type, object)

    assert issubclass(object, object)

def test15 () :
    class A :
        def __init__ (self, i, s, f) :
            self.i = i
            self.s = s
            self.f = f

        def __eq__ (self, rhs) :
            return (self.i == rhs.i) and (self.s == rhs.s) and (self.f == rhs.f)

    x = A(2, "abc", 3.45)
    y = A(2, "abc", 3.45)
    assert x is not y
    assert x ==     y

def main () :
    print("Types.py")
    for i in range(15) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
