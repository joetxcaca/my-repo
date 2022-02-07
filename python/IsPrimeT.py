#!/usr/bin/env python3

# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -----------
# IsPrimeT.py
# -----------

import math
import unittest

def is_prime (n: int) -> bool :
    assert n > 0
    if n == 2 :
        return True
    if (n == 1) or ((n % 2) == 0) :
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2) :
        if (n % i) == 0 :
            return False
    return True

class MyUnitTests (unittest.TestCase) :
    def test0 (self) :
        self.assertFalse(is_prime( 1))

    def test1 (self) :
        self.assertTrue(is_prime( 2))

    def test2 (self) :
        self.assertTrue(is_prime( 3))

    def test3 (self) :
        self.assertFalse(is_prime( 4))

    def test4 (self) :
        self.assertTrue(is_prime( 5))

    def test5 (self) :
        self.assertTrue(is_prime( 7))

    def test6 (self) :
        self.assertFalse(is_prime( 9))

    def test7 (self) :
        self.assertFalse(is_prime(27))

    def test8 (self) :
        self.assertTrue(is_prime(29))

if __name__ == "__main__" : # pragma: no cover
    unittest.main()
