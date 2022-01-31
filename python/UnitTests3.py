#!/usr/bin/env python3

# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# -------------
# UnitTests3.py
# -------------

# https://docs.python.org/3/library/unittest.html
# https://docs.python.org/3/library/unittest.html#assert-methods

import unittest # main, TestCase

def cycle_length (n: int) -> int :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

class MyUnitTests (unittest.TestCase) :
    def test0 (self) :
        self.assertEqual(cycle_length( 1), 1)

    def test1 (self) :
        self.assertEqual(cycle_length( 5), 6)

    def test2 (self) :
        self.assertEqual(cycle_length(10), 7)

if __name__ == "__main__" : # pragma: no cover
    unittest.main()

""" #pragma: no cover
% ./UnitTests3T.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
"""
