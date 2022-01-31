#!/usr/bin/env python3

# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# ------------
# Coverage2.py
# ------------

# https://coverage.readthedocs.org

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
    def test (self) :
        self.assertEqual(cycle_length(2), 2)

if __name__ == "__main__" : # pragma: no cover
    unittest.main()

""" #pragma: no cover
% coverage run --branch Coverage2T.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK



% coverage report -m
Name           Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------------
Coverage2.py      14      1      4      1    89%   22
----------------------------------------------------------
TOTAL             14      1      4      1    89%
"""
