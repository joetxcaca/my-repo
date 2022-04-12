#/usr/bin/env python3

# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -----------
# ProjectT.py
# -----------

# http://en.wikipedia.org/wiki/Projection_(relational_algebra)

import typing
import unittest

class project_class_1 :
    def __init__ (self, r, *t) :
        self.p = iter(r)
        self.t = t

    def __iter__ (self) :
        return self

    def __next__ (self) :
        d = next(self.p)
        x = {}
        for k in self.t :
            if k in d :
                x[k] = d[k]
        return x

class project_class_2 :
    def __init__ (self, r, *t) -> None :
        self.p = iter(r)
        self.t = t

    def __iter__ (self) -> typing.Iterator[typing.Dict[str, int]] :
        return self

    def __next__ (self) -> typing.Dict[str, int] :
        d = next(self.p)
        return {k : d[k] for k in self.t if k in d}

def project_function_yield_1 (r: typing.Iterable[typing.Dict[str, int]], *t: str) \
        -> typing.Iterator[typing.Dict[str, int]] :
    for d in r :
        x = {}
        for k in t :
            if k in d :
                x[k] = d[k]
        yield x

def project_function_yield_2 (r: typing.Iterable[typing.Dict[str, int]], *t: str) \
        -> typing.Iterator[typing.Dict[str, int]]  :
    for d in r :
        yield {k : d[k] for k in t if k in d}

def project_function_generator (r: typing.Iterable[typing.Dict[str, int]], *t: str) \
        -> typing.Iterator[typing.Dict[str, int]]  :
    return ({k : d[k] for k in t if k in d} for d in r)

class MyUnitTests (unittest.TestCase) :
    def setUp (self) :
        self.a = [
            project_class_1,
            project_class_2,
            project_function_yield_1,
            project_function_yield_2,
            project_function_generator]

        self.r = [
            {"A" : 1, "B" : 4, "C" : 3},
            {"A" : 2, "B" : 5, "C" : 2},
            {"A" : 3, "B" : 6, "C" : 1}]

    def test0 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(self.r, "D")
                self.assertEqual(
                    list(x),
                    [{}, {}, {}])
                self.assertFalse(list(x))

    def test1 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(self.r, "B")
                self.assertEqual(
                    list(x),
                    [{'B': 4},
                     {'B': 5},
                     {'B': 6}])
                self.assertFalse(list(x))

    def test2 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(self.r, "A", "C")
                self.assertEqual(
                    list(x),
                    [{'A': 1, 'C': 3},
                     {'A': 2, 'C': 2},
                     {'A': 3, 'C': 1}])
                self.assertFalse(list(x))

if __name__ == "__main__" :
    unittest.main()
