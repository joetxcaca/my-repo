#!/usr/bin/env python3

# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# -------------
# UnitTests1.py
# -------------

# https://docs.python.org/3/library/unittest.html
# https://docs.python.org/3/library/unittest.html#assert-methods

import unittest # main, TestCase

def cycle_length (n: int) -> int :
    assert n > 0
    c = 0
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
% ./UnitTests1T.py
FFF
======================================================================
FAIL: test0 (__main__.MyUnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/downing/Dropbox/examples/python/./UnitTests1.py", line 30, in test0
    self.assertEqual(cycle_length( 1), 1)
  File "/Users/downing/Dropbox/examples/python/./UnitTests1.py", line 25, in cycle_length
    assert c > 0
AssertionError

======================================================================
FAIL: test1 (__main__.MyUnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/downing/Dropbox/examples/python/./UnitTests1.py", line 33, in test1
    self.assertEqual(cycle_length( 5), 6)
AssertionError: 5 != 6

======================================================================
FAIL: test2 (__main__.MyUnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/downing/Dropbox/examples/python/./UnitTests1.py", line 36, in test2
    self.assertEqual(cycle_length(10), 7)
AssertionError: 6 != 7

----------------------------------------------------------------------
Ran 3 tests in 0.002s

FAILED (failures=3)
"""
