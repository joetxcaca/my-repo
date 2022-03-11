#!/usr/bin/env python3

# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods
# pylint: disable = unnecessary-comprehension

# ------------
# Iterables.py
# ------------

import typing

def test_iterator (p: typing.Iterator[int]) :
    assert hasattr(p, "__next__")
    assert hasattr(p, "__iter__")
    q = iter(p)                        # q = p.__iter__()
    assert q is p

    assert next(p) == 2 # p.__next__()
    assert next(p) == 3
    assert next(p) == 4

    try :
        assert next(p) == 5 # p.__next__()
        assert False
    except StopIteration :
        pass

def my_iterator () :
    for v in range(2, 5) :
        yield v

def test1 () :
    test_iterator(iter([2, 3, 4]))                      # list
    test_iterator(iter((2, 3, 4)))                      # tuple
    test_iterator(iter({2, 3, 4}))                      # set
    test_iterator(iter({2: "abc", 3: "def", 4: "ghi"})) # dict
    test_iterator(iter([v for v in [2, 3, 4]]))         # list comprehension
    test_iterator(iter(range(2, 5)))
    test_iterator(v for v in [2, 3, 4])                 # generator
    test_iterator(   map(lambda v : v,    [2, 3, 4]))
    test_iterator(filter(lambda v : True, [2, 3, 4]))
    test_iterator(my_iterator())

def test_container (x: typing.Iterable[int]) :
    assert not hasattr(x, "__next__")
    assert     hasattr(x, "__iter__")
    p = iter(x)                         # p = x.__iter__()
    assert p is not x
    test_iterator(p)

class my_container :
    def __iter__ (self) :
        for v in range(2, 5) :
            yield v

def test2 () :
    test_container([2, 3, 4])                      # list
    test_container((2, 3, 4))                      # tuple
    test_container({2, 3, 4})                      # set
    test_container({2: "abc", 3: "def", 4: "ghi"}) # dict
    test_container([v for v in [2, 3, 4]])         # list comprehension
    test_container(range(2, 5))
    test_container(my_container())

def main () :
    print("Iterables.py")
    for i in range(2) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
