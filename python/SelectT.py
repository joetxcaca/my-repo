#!/usr/bin/env python3

# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ----------
# SelectT.py
# ----------

# http://en.wikipedia.org/wiki/Selection_(relational_algebra)

import typing
import unittest

class select_class_while :
    def __init__ (self,
            r: typing.Iterable[typing.Dict[str, int]],
            f: typing.Callable[[typing.Dict[str, int]], bool]) -> None :
        self.p = iter(r)
        self.f = f

    def __iter__ (self) -> typing.Iterator[typing.Dict[str, int]] :
        return self

    def __next__ (self) -> typing.Dict[str, int] :
        while True :
            d = next(self.p)
            if self.f(d) :
                return d

class select_class_recursion :
    def __init__ (self,
            r: typing.Iterable[typing.Dict[str, int]],
            f: typing.Callable[[typing.Dict[str, int]], bool]) -> None :
        self.p = iter(r)
        self.f = f

    def __iter__ (self) -> typing.Iterator[typing.Dict[str, int]] :
        return self

    def __next__ (self) -> typing.Dict[str, int] :
        d = next(self.p)
        if self.f(d) :
            return d
        return next(self)

def select_function_yield (
        r: typing.Iterable[typing.Dict[str, int]],
        f: typing.Callable[[typing.Dict[str, int]], bool]) \
        -> typing.Iterator[typing.Dict[str, int]]          :
    for d in r :
        if f(d) :
            yield d

def select_function_generator (
        r: typing.Iterable[typing.Dict[str, int]],
        f: typing.Callable[[typing.Dict[str, int]], bool]) \
        -> typing.Iterator[typing.Dict[str, int]]          :
    return (d for d in r if f(d))

def select_function_filter (
        r: typing.Iterable[typing.Dict[str, int]],
        f: typing.Callable[[typing.Dict[str, int]], bool]) \
        -> typing.Iterator[typing.Dict[str, int]]          :
    return filter(f, r)

class MyUnitTests (unittest.TestCase) :
    def setUp (self) :
        self.a = [
            select_class_while,
            select_class_recursion,
            select_function_yield,
            select_function_generator,
            select_function_filter]

        self.r = [
            {"A" : 1, "B" : 4, "C" : 3},
            {"A" : 2, "B" : 5, "C" : 2},
            {"A" : 3, "B" : 6, "C" : 1}]

    def test0 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(self.r, lambda d : False)
                self.assertFalse(list(x))
                self.assertFalse(list(x))

    def test1 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(self.r, lambda d : True)
                self.assertEqual(
                    list(x),
                    [{"A" : 1, "B" : 4, "C" : 3},
                     {"A" : 2, "B" : 5, "C" : 2},
                     {"A" : 3, "B" : 6, "C" : 1}])
                self.assertFalse(list(x))

    def test2 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(self.r, lambda d : d["B"] > 4)
                self.assertEqual(
                    list(x),
                    [{'A': 2, 'B': 5, 'C': 2},
                     {'A': 3, 'B': 6, 'C': 1}])
                self.assertFalse(list(x))

    def test3 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(self.r, lambda d : d["A"] > d["C"])
                self.assertEqual(
                    list(x),
                    [{'A': 3, 'B': 6, 'C': 1}])
                self.assertFalse(list(x))

if __name__ == "__main__" :
    unittest.main()
