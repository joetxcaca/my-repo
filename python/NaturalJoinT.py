#!/usr/bin/env python3

# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ---------------
# NaturalJoinT.py
# ---------------

# https://en.wikipedia.org/wiki/Relational_algebra#Natural_join

import typing
import unittest

def theta_join (
        r: typing.Iterable[typing.Dict[str, int]],
        s: typing.Iterable[typing.Dict[str, int]],
        f: typing.Callable[[typing.Dict[str, int], typing.Dict[str, int]], bool]) \
        -> typing.Iterator[typing.Dict[str, int]]                          :
    return ({**u, **v} for u in r for v in s if f(u, v))

def natural_join_for (
        r: typing.Iterable[typing.Dict[str, int]],
        s: typing.Iterable[typing.Dict[str, int]]) \
        -> typing.Iterator[typing.Dict[str, int]]  :
    def bp (u, v) :
        for k in u :
            if (k in v) and (u[k] != v[k]) :
                return False
        return True
    return theta_join(r, s, bp)

def natural_join_all (
        r: typing.Iterable[typing.Dict[str, int]],
        s: typing.Iterable[typing.Dict[str, int]]) \
        -> typing.Iterator[typing.Dict[str, int]]  :
    def bp (u, v) :
        return all(u[k] == v[k] for k in u if k in v)
    return theta_join(r, s, bp)

def natural_join_lambda (
        r: typing.Iterable[typing.Dict[str, int]],
        s: typing.Iterable[typing.Dict[str, int]]) \
        -> typing.Iterator[typing.Dict[str, int]]  :
    return theta_join(r, s, lambda u, v : all(u[k] == v[k] for k in u if k in v))

class MyUnitTests (unittest.TestCase) :
    def setUp (self) :
        self.a = [
            natural_join_for,
            natural_join_all,
            natural_join_lambda]
        self.r = []
        self.s = []

    def test0 (self) :
        self.r = [
            {"A" : 1, "B" : 4},
            {"A" : 2, "B" : 5},
            {"A" : 3, "B" : 6}]

        self.s = [
            {"C" : 2, "D" : 7},
            {"C" : 3, "D" : 5},
            {"C" : 3, "D" : 6},
            {"C" : 4, "D" : 6}]

        for f in self.a :
            with self.subTest() :
                x = f(self.r, self.s)
                self.assertEqual(
                    list(x),
                    [{'A': 1, 'B': 4, 'C': 2, 'D': 7},
                     {'A': 1, 'B': 4, 'C': 3, 'D': 5},
                     {'A': 1, 'B': 4, 'C': 3, 'D': 6},
                     {'A': 1, 'B': 4, 'C': 4, 'D': 6},
                     {'A': 2, 'B': 5, 'C': 2, 'D': 7},
                     {'A': 2, 'B': 5, 'C': 3, 'D': 5},
                     {'A': 2, 'B': 5, 'C': 3, 'D': 6},
                     {'A': 2, 'B': 5, 'C': 4, 'D': 6},
                     {'A': 3, 'B': 6, 'C': 2, 'D': 7},
                     {'A': 3, 'B': 6, 'C': 3, 'D': 5},
                     {'A': 3, 'B': 6, 'C': 3, 'D': 6},
                     {'A': 3, 'B': 6, 'C': 4, 'D': 6}])
                self.assertFalse(list(x))

    def test1 (self) :
        self.r = [
            {"A" : 1, "B" : 4, "C" : 7},
            {"A" : 2, "B" : 5, "C" : 8},
            {"A" : 3, "B" : 6, "C" : 9}]

        self.s = [
            {"A" : 4, "B" : 4, "D" : 7},
            {"A" : 5, "B" : 5, "D" : 5},
            {"A" : 6, "B" : 6, "D" : 6},
            {"A" : 7, "B" : 7, "D" : 6}]

        for f in self.a :
            with self.subTest() :
                x = f(self.r, self.s)
                self.assertFalse(list(x))

    def test2 (self) :
        self.r = [
            {"A" : 1, "B" : 4, "C" : 7},
            {"A" : 2, "B" : 5, "C" : 8},
            {"A" : 3, "B" : 6, "C" : 9}]

        self.s = [
            {"A" : 2, "B" : 4, "D" : 7},
            {"A" : 3, "B" : 5, "D" : 5},
            {"A" : 3, "B" : 6, "D" : 6},
            {"A" : 4, "B" : 7, "D" : 6}]

        for f in self.a :
            with self.subTest() :
                x = f(self.r, self.s)
                self.assertEqual(
                    list(x),
                    [{'A': 3, 'B': 6, 'C': 9, 'D': 6}])
                self.assertFalse(list(x))

if __name__ == "__main__" :
    unittest.main()
