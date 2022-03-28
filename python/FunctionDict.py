#!/usr/bin/env python3

# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ---------------
# FunctionDict.py
# ---------------

def f (x, y, **d) :
    return [x, y, d]

def test1 () :
    assert f(2, 3)           == [2, 3, {}]
    assert f(2, 3, a=4)      == [2, 3, {'a': 4}]
    assert f(2, 3, a=4, b=5) == [2, 3, {'a': 4, 'b': 5}]

def test2 () :
    d = {"b": 4, "a": 3}
    assert f(2, 5,   **d)  == [2, 5, {'a': 3, 'b': 4}]
    assert f(2, y=5, **d)  == [2, 5, {'a': 3, 'b': 4}]
    u = (2,)
    assert f(y=5, *u,  **d) == [2, 5, {'a': 3, 'b': 4}]
    assert f(*u,  y=5, **d) == [2, 5, {'a': 3, 'b': 4}]

def test3 () :
    d = {"y": 3, "a": 2}
    assert f(2,   **d) == [2, 3, {'a': 2}]
    assert f(x=2, **d) == [2, 3, {'a': 2}]

def main () :
    print("FunctionDict.py")
    for i in range(3) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
