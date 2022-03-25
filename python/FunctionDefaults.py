#!/usr/bin/env python3

# pylint: disable = dangerous-default-value
# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------------------
# FunctionDefaults.py
# -------------------

def f (x, y, z) :
    return [x, y, z]

def test1 () :
    # f(2, 3)                      # TypeError: f() missing 1 required positional argument: 'z'
    assert f(2, 3, 4) == [2, 3, 4]
    # f(2, 3, 4, 5)                # TypeError: f() takes 3 positional arguments but 4 were given





def g1 (x, y, z=5) :
    return [x, y, z]

def test2 () :
    assert g1(2, 3)    == [2, 3, 5]
    assert g1(2, 3, 4) == [2, 3, 4]

# def g2 (x, y=5, z) : # SyntaxError: non-default argument follows default argument
#     return [x, y, z]





def h1 (x=[]) : # mutable default
    x += [2]
    return x

def test3 () :
    assert h1()    == [2]
    assert h1()    == [2, 2]
    assert h1([1]) == [1, 2]
    assert h1()    == [2, 2, 2]
    assert h1([1]) == [1, 2]





def h2 (x=()) : # immutable default
    x += (2,)
    return x

def test4 () :
    assert h2()     == (2,)
    assert h2()     == (2,)
    assert h2((1,)) == (1, 2)
    assert h2()     == (2,)
    assert h2((1,)) == (1, 2)





def h3 (x=None) :
    if x is None :
        x = []
    x += [2]
    return x

def test5 () :
    assert h3()     == [2]
    assert h3()     == [2]
    assert h3([1])  == [1, 2]
    assert h3()     == [2]
    assert h3([1])  == [1, 2]
    assert h3(None) == [2]





def main () :
    print("FunctionDefaults.py")
    for i in range(5) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
