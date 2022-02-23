#!/usr/bin/env python3

# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ----------
# ReduceT.py
# ----------

# https://docs.python.org/3.6/library/functools.html

import functools
import operator
import typing
import unittest

T = typing.TypeVar("T")

def reduce_for (bf: typing.Callable[[T, T], T], a: typing.Iterable[T], v: T) -> T :
    for w in a :
        v = bf(v, w)
    return v

def reduce_while (bf: typing.Callable[[T, T], T], a: typing.Iterable[T], v: T) -> T :
    p = iter(a)
    try :
        while True :
            w = next(p)
            v = bf(v, w)
    except StopIteration :
        pass
    return v

class MyUnitTests (unittest.TestCase) :
    def setUp (self) :
        self.a = [
            reduce_for,
            reduce_while,
            functools.reduce]

    def test0 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(operator.add, [2, 3, 4], 0), 9)

    def test1 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(operator.mul, (2, 3, 4), 1), 24)

    def test2 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(operator.sub, {2, 3, 4}, 2), -7)

    def test3 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(None, [], 3),  3)

if __name__ == "__main__" : # pragma: no cover
    unittest.main()
