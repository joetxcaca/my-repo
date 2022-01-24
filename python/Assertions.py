#!/usr/bin/env python3

# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# -------------
# Assertions.py
# -------------

# https://docs.python.org/3/reference/simple_stmts.html#grammar-token-assert_stmt

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

def test () -> None :
    assert cycle_length( 1) == 1
    assert cycle_length( 5) == 6
    assert cycle_length(10) == 7

if __name__ == "__main__" : # pragma: no cover
    print("Assertions.py")
    test()
    print("Done.")

""" #pragma: no cover
% Assertions.py
Assertions.py
Traceback (most recent call last):
  File "./Assertions.py", line 32, in <module>
    test()
  File "./Assertions.py", line 26, in test
    assert cycle_length( 1) == 1
  File "./Assertions.py", line 22, in cycle_length
    assert c > 0
AssertionError



% python3 -O Assertions.py
Assertions.py
Done.
"""
