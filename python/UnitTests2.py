#!/usr/bin/env python3

# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# -------------
# UnitTests2.py
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
        self.assertEqual(cycle_length( 5), 5)

    def test2 (self) :
        self.assertEqual(cycle_length(10), 7)

if __name__ == "__main__" : # pragma: no cover
    unittest.main()

""" #pragma: no cover
% ./UnitTests2T.py
.F.
======================================================================
FAIL: test1 (__main__.MyUnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/downing/Dropbox/examples/python/./UnitTests2.py", line 33, in test1
    self.assertEqual(cycle_length( 5), 5)
AssertionError: 6 != 5

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
"""
