#!/usr/bin/env python3

# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = line-too-long

# -------------------
# FunctionKeywords.py
# -------------------

def f (x, y, z) :
    return [x, y, z]

def test1 () :
    assert f(2, z=4, y=3) == [2, 3, 4]
    # f(z=4, 2,   y=3)                 # SyntaxError: non-keyword arg after keyword arg
    # f(2,   x=2, y=3)                 # TypeError: f() got multiple values for argument 'x'
    # f(2,   a=4, y=3)                 # TypeError: f() got an unexpected keyword argument 'a'





def g (x, *, y, z) :
    return [x, y, z]

def test2 () :
    # g(2, 3, 4)                         # TypeError: f() takes 1 positional argument but 3 were given
    assert g(2,   z=4, y=3) == [2, 3, 4]
    assert g(x=2, z=4, y=3) == [2, 3, 4]





def main () :
    print("FunctionKeywords.py")
    for i in range(2) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
