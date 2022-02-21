#!/usr/bin/env python3

# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# -------------
# FactorialT.py
# -------------

# https://docs.python.org/3.6/library/math.html

import functools
import math
import operator
import timeit
import unittest

# recursive procedure
# linear recursive process
# 15 milliseconds
def factorial_recursion (n: int) -> int :
    assert n >= 0
    if n < 2 :
        return 1
    return n * factorial_recursion(n - 1)





# recursive procedure
# linear iterative process
# 20 milliseconds
def factorial_tail_recursion (n: int, v: int = 1) -> int :
    assert n >= 0
    assert v >= 1
    if n < 2 :
        return v
    return factorial_tail_recursion(n - 1 , n * v)





# iterative procedure
# linear iterative process
# 10 milliseconds
def factorial_while (n: int) -> int :
    assert n >= 0
    v = 1
    while n > 1 :
        v *= n
        n -= 1
    return v





# iterative procedure
# linear iterative process
# 7 milliseconds
def factorial_range_for (n: int) -> int :
    assert n >= 0
    v = 1
    for i in range(1, n + 1) :
        v *= i
    return v





# iterative procedure
# linear iterative process
# 10 milliseconds
def factorial_range_iterator (n: int) -> int :
    assert n >= 0
    v = 1
    p = iter(range(1, n + 1))
    try :
        while True :
            i  = next(p)
            v *= i
    except StopIteration :
        pass
    return v





def my_mul (x, y) :
    return x * y

# iterative procedure
# linear iterative process
# 9 milliseconds
def factorial_range_reduce_1 (n: int) -> int :
    assert n >= 0
    return functools.reduce(my_mul, range(1, n + 1), 1)





# iterative procedure
# linear iterative process
# 10 milliseconds
def factorial_range_reduce_2 (n: int) -> int :
    assert n >= 0
    return functools.reduce(lambda x, y : x * y, range(1, n + 1), 1)





# iterative procedure
# linear iterative process
# 6 milliseconds
def factorial_range_reduce_3 (n: int) -> int :
    assert n >= 0
    return functools.reduce(operator.mul, range(1, n + 1), 1)





class MyUnitTests (unittest.TestCase) :
    def setUp (self) :
        self.a = [
            factorial_recursion,
            factorial_tail_recursion,
            factorial_while,
            factorial_range_for,
            factorial_range_iterator,
            factorial_range_reduce_1,
            factorial_range_reduce_2,
            factorial_range_reduce_3,
            math.factorial]

    def test0 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(0), 1)

    def test1 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(1), 1)

    def test2 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(2), 2)

    def test3 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(3), 6)

    def test4 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(4), 24)

    def test5 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(5), 120)

    def test6 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                print()
                print(f.__name__)
                if f.__name__ == "factorial" :
                    t = timeit.timeit(
                        "math." + f.__name__ + "(100)",
                        "import math",
                        number = 1000)
                else :
                    t = timeit.timeit(
                        "__main__." + f.__name__ + "(100)",
                        "import __main__",
                        number = 1000)
                print(f"{t*1000:.2f} milliseconds")

if __name__ == "__main__" : # pragma: no cover
    unittest.main()

""" #pragma: no cover
% FactorialT.py
......
factorial_recursion
14.66 milliseconds

factorial_tail_recursion
19.34 milliseconds

factorial_while
9.47 milliseconds

factorial_range_for
6.42 milliseconds

factorial_range_iterator
9.66 milliseconds

factorial_range_reduce_1
9.31 milliseconds

factorial_range_reduce_2
9.97 milliseconds

factorial_range_reduce_3
5.61 milliseconds

factorial
0.88 milliseconds
.
----------------------------------------------------------------------
Ran 7 tests in 0.086s

OK
"""
