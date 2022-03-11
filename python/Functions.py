#!/usr/bin/env python3

# pylint: disable = cell-var-from-loop
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# ------------
# Functions.py
# ------------

def square1 (v) :
    return v ** 2

def test1 () :
    a = [2, 3, 4]
    m = map(square1, a)
    assert list(m) == [4, 9, 16]
    assert list(m) == []





square2 = lambda v : v ** 2

def test2 () :
    a = [2, 3, 4]
    m = map(square2, a)
    assert list(m) == [4, 9, 16]
    assert list(m) == []





class square3 :
    def __call__ (self, v) :
        return v ** 2

def test3 () :
    a = [2, 3, 4]
    m = map(square3(), a)
    assert list(m) == [4, 9, 16]
    assert list(m) == []





def pow1 (p) :
    def f (v) :
        return v ** p
    return f

def test4 () :
    a = [2, 3, 4]
    m = map(pow1(2), a)
    assert list(m) == [4, 9, 16]
    assert list(m) == []





def pow2 (p) :
    return lambda v : v ** p

def test5 () :
    a = [2, 3, 4]
    m = map(pow2(2), a)
    assert list(m) == [4, 9, 16]
    assert list(m) == []





class pow3 :
    def __init__ (self, p) :
        self.p = p

    def __call__ (self, v) :
        return v ** self.p

def test6 () :
    a = [2, 3, 4]
    m = map(pow3(2), a)
    assert list(m) == [4, 9, 16]
    assert list(m) == []





def test7 () :
    a     = [2, 3, 4]
    n     = [1]
    m     = map(lambda v : v ** next(iter(n)), a)
    a    += [5]
    n[0]  = 2
    assert list(m) == [4, 9, 16, 25]
    assert list(m) == []

def test8 () :
    a = [2, 3, 4]
    n = [1]
    m = map(lambda v : v ** next(iter(n)), a)
    a = [2, 3, 4, 5]
    n = [2]
    assert list(m) == [4, 9, 16]
    assert list(m) == []

def test9 () :
    a  = [2, 3, 4]
    fs = [lambda v : v ** n for n in range(3)]
    ms = [map(f, a) for f in fs]
    assert [list(m) for m in ms] == [[4, 9, 16], [4, 9, 16], [4, 9, 16]]
    assert [list(m) for m in ms] == [[],         [],         []]





def main () :
    print("Functions.py")
    for i in range(9) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
