#!/usr/bin/env python3

# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement
# pylint: disable = unnecessary-comprehension

# ------------------
# DigitsIteratorT.py
# ------------------

import typing
import unittest

T = typing.TypeVar("T")

class digits_iterator (typing.Iterator[T]):
    def __init__ (self, v) -> None :
        self.v = v

    def __iter__ (self) -> typing.Iterator[T] :
        return self

    def __next__ (self) -> T :
        if self.v == 0 :
            raise StopIteration
        w = self.v % 10
        self.v //= 10
        return w

def digits_iterator_2 (v) :
    while v != 0 :
        yield v % 10
        v //= 10

class MyUnitTests (unittest.TestCase) :
    def test0 (self) :
        p = digits_iterator(0)
        self.assertTrue(hasattr(p, "__next__"))
        self.assertTrue(hasattr(p, "__iter__"))
        self.assertIs(iter(p), p)
        try :
            next(p)
            assert False
        except StopIteration :
            pass

    def test1 (self) :
        p = digits_iterator(2)
        self.assertEqual(next(p), 2)
        try :
            next(p)
            assert False
        except StopIteration :
            pass

    def test2 (self) :
        p = digits_iterator(23)
        self.assertEqual(next(p), 3)
        self.assertEqual(next(p), 2)
        try :
            next(p)
            assert False
        except StopIteration :
            pass

    def test3 (self) :
        p = digits_iterator(234)
        a = [v for v in p]
        self.assertEqual(a, [4, 3, 2])
        a = [v for v in p]
        self.assertEqual(a, [])

    def test4 (self) :
        p = digits_iterator(234)
        self.assertEqual(list(p), [4, 3, 2])
        self.assertEqual(list(p), [])

if __name__ == "__main__" : # pragma: no cover
    unittest.main()
