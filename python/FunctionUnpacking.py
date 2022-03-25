#!/usr/bin/env python3

# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = line-too-long
# pylint: disable = missing-docstring

# --------------------
# FunctionUnpacking.py
# --------------------

def f (x, y, z) :
    return [x, y, z]

def test1 () :
    t = (3, 4)
    assert f(2, 5, t) == [2, 5, (3, 4)]
    assert f(2, *t)   == [2, 3, 4]      # order matters
    assert f(*t,  2)  == [3, 4, 2]
    assert f(z=2, *t) == [3, 4, 2]      # unpacking goes first, order doesn't matter
    assert f(*t, z=2) == [3, 4, 2]
    # f(x=2, *t)                        # TypeError: f() got multiple values for argument 'x'
    # f(*t,  x=2)                       # TypeError: f() got multiple values for argument 'x'

def test2 () :
    u = (2, 3)
    v = (4,)
    assert f(*u, *v) == [2, 3, 4]
    assert  [*u, *v] == [2, 3, 4]
    assert  (*u, *v) == (2, 3, 4)
    assert  {*u, *v} == {2, 3, 4}

def test3 () :
    d = {"z" : 4, "y" : 3, "x" : 2}
    assert f(**d) == [2, 3, 4]

def test4 () :
    d = {"z" : 4, "y" : 3}
    assert f(2,   **d) == [2, 3, 4]
    # f(**d, 2)                       # SyntaxError: invalid syntax
    assert f(x=2, **d) == [2, 3, 4]
    assert f(**d, x=2) == [2, 3, 4]
    # assert f(z=2, **d) == [2, 3, 4] # TypeError: f() got multiple values for keyword argument 'z'
    # assert f(**d, z=2) == [2, 3, 4] # TypeError: f() got multiple values for keyword argument 'z'

def test5 () :
    t = (2, 3)
    d = {"z" : 4}
    assert f(*t, **d) == [2, 3, 4]
    # f(**d, *t)                      # SyntaxError: iterable argument unpacking follows keyword argument unpacking

def test6 () :
    u = {"x":2, "y":3}
    v = {"z":4}
    assert f(**u, **v) == [2, 3, 4]
    assert {**u, **v}  == {"x": 2, "y": 3, "z": 4}

def main () :
    print("FunctionUnpacking.py")
    for i in range(6) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
