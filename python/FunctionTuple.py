#!/usr/bin/env python3

# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ----------------
# FunctionTuple.py
# ----------------

def f (x, y, *t) :
    return [x, y, t]

def test1 () :
    assert f(2, 3)       == [2, 3, ()]
    assert f(2, 3, 4)    == [2, 3, (4,)]
    assert f(2, 3, 4, 5) == [2, 3, (4, 5)]

def test2 () :
    t = (3, 4)
    assert f(2, 5,  t)  == [2, 5, ((3, 4),)]
    assert f(2, 5, *t)  == [2, 5, (3, 4)]
    assert f(2, *t)     == [2, 3, (4,)]
    assert f(*t)        == [3, 4, ()]

def main () :
    print("FunctionTuple.py")
    for i in range(2) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
