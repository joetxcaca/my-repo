#!/usr/bin/env python3

# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# -------------
# Decorators.py
# -------------

import types

def f1 (n) :
    return n + 1

def test1 () :
    assert f1(2) == 3

assert isinstance(f1, types.FunctionType)
assert hasattr(f1, "__call__")

def debug_function (f) :
    assert hasattr(f, "__call__")
    def g (n) : # must be a closure that captures f
        print(f.__name__, ":", end=" ")
        print("input =", n, ";", end=" ")
        m = f(n)
        print("output =", m, ";")
        return m
    assert isinstance(g, types.FunctionType)
    assert hasattr(g, "__call__")
    return g

assert isinstance(debug_function, types.FunctionType)
assert hasattr(debug_function, "__call__")

f1 = debug_function(f1)
assert isinstance(f1, types.FunctionType)
assert hasattr(f1, "__call__")

def test2 () :
    assert f1(2) == 3 # f2 : input = 2 ; output = 3 ;

@debug_function
def f2 (n) :
    return n + 1

assert isinstance(f2, types.FunctionType)
assert hasattr(f2, "__call__")

def test3 () :
    assert f2(2) == 3 # f3 : input = 2 ; output = 3 ;





def f4 (n) :
    return n + 1

assert isinstance(f4, types.FunctionType)
assert hasattr(f4, "__call__")

def test4 () :
    assert f4(2) == 3

class debug_class :
    def __init__ (self, f) :
        assert hasattr(f, "__call__")
        self.f = f

    def __call__ (self, n) :
        print(self.f.__name__, ":", end=" ")
        print("input =", n, ";", end=" ")
        m = self.f(n)
        print("output =", m, ";")
        return m

assert not isinstance(debug_class, types.FunctionType)
assert hasattr(debug_class, "__call__")

f4 = debug_class(f4) # invoking constructor
assert not isinstance(f4, types.FunctionType)
assert isinstance(f4, debug_class)
assert hasattr(f4, "__call__")

def test5 () :
    assert f4(2) == 3 # f4 : input = 2 ; output = 3 ;

@debug_class
def f5 (n) :
    return n + 1

assert not isinstance(f5, types.FunctionType)
assert isinstance(f5, debug_class)
assert hasattr(f5, "__call__")

def test5 () :
    assert f5(2) == 3 # f5 : input = 2 ; output = 3 ;





def repeat_three (f) :
    def g () :
        for _ in range(3) :
            f()
    return g

@repeat_three
def f6 () :
    print("Hi")

def test6 () :
    f6()                        # Hi Hi Hi




def repeat_N (n) :
    def h (f) :
        def g () :
            for _ in range(n) :
                f()
        return g
    return h

@repeat_N(3)
def f7 () :
    print("Bob")

def test7 () :
    f7()                        # Bob Bob Bob



def main () :
    print("Decorators.py")
    for n in range(7) :
        eval("test" + str(n + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
