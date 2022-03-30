#!/usr/bin/env python3

# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = no-member
# pylint: disable = no-name-in-module
# pylint: disable = redefined-builtin

# ----------
# RegExps.py
# ----------

# https://docs.python.org/3/library/re.html

import re

def test1 () :
    s = "b ab\naab 123"
    a = re.split("ab", s)
    assert isinstance(a, list)
    assert a == ['b ', '\na', ' 123']

def test2 () :
    s = "b ab\naab 123"
    a = re.split("ba", s)
    assert isinstance(a, list)
    assert a == [s]

def test3 () :
    s = "b ab\naab 123"
    a = re.split("^b", s)            # start of string
    assert isinstance(a, list)
    assert a == ['', ' ab\naab 123']

def test4 () :
    s = "b ab\naab 123"
    a = re.split("^a", s)      # start of string
    assert isinstance(a, list)
    assert a == [s]

def test5 () :
    s = "b ab\naab 123"
    r = re.compile("^a", re.M)       # multiline
    assert isinstance(r, re.Pattern)
    a = r.split(s)
    assert isinstance(a,      list)
    assert a == ['b ab\n', 'ab 123']

def test6 () :
    s = "b ab\naab 123"
    a = re.split("3$", s)            # end of string
    assert isinstance(a, list)
    assert a == ['b ab\naab 12', '']

def test7 () :
    s = "b ab\naab 123"
    a = re.split("b$", s)      # end of string
    assert isinstance(a, list)
    assert a == [s]

def test8 () :
    s = "b ab\naab 123"
    r = re.compile("b$", re.M)       # multiline
    assert isinstance(r, re.Pattern)
    a = r.split(s)
    assert isinstance(a,      list)
    assert a == ['b a', '\naab 123']

def test9 () :
    s = "b ab\naab 123"
    a = re.split(".", s)                                           # any character
    assert isinstance(a, list)
    assert a == ['', '', '', '', '\n', '', '', '', '', '', '', '']

def test10 () :
    s = "b ab\naab 123"
    a = re.split(r"\d", s)                 # any digit
    assert isinstance(a, list)
    assert a == ['b ab\naab ', '', '', '']

def test11 () :
    s = "b ab\naab 123"
    a = re.split(r"\D", s)                                  # any non-digit
    assert isinstance(a, list)
    assert a == ['', '', '', '', '', '', '', '', '', '123']

def test12 () :
    s = "b ab\naab 123"
    a = re.split(r"\w", s)                                   # any alphanumeric
    assert isinstance(a, list)
    assert a == ['', ' ', '', '\n', '', '', ' ', '', '', '']

def test13 () :
    s = "b ab\naab 123"
    a = re.split(r"\W", s)                # any non-alphanumeric
    assert isinstance(a, list)
    assert a == ['b', 'ab', 'aab', '123']

def test14 () :
    s = "b ab\naab 123"
    m = re.search("(a*)b([^a]*)(a*)b", s) # * is zero or more
    assert isinstance(m, re.Match)
    assert m.group(0) == "b ab"
    assert m.group(1) == ""
    assert m.group(2) == " "
    assert m.group(3) == "a"
    try :
        m.group(4)
        assert False
    except IndexError :
        pass

def test15 () :
    s = "b ab\naab 123"
    m = re.search("(a+)b([^a]*)(a+)b", s) # + is one or more
    assert isinstance(m, re.Match)
    assert m.group(0) == "ab\naab"
    assert m.group(1) == "a"
    assert m.group(2) == "\n"
    assert m.group(3) == "aa"
    try :
        m.group(4)
        assert False
    except IndexError :
        pass

def test16 () :
    s = "b ab\naab 123"
    m = re.search("((a?)b([^a]*))(a?)b", s) # ? is zero or one
    assert isinstance(m, re.Match)
    assert m.group(0) == "b ab"
    assert m.group(1) == "b "
    assert m.group(2) == ""
    assert m.group(3) == " "
    assert m.group(4) == "a"

def test17 () :
    s = "b ab\naab 123"
    t = re.sub("b ", "xx", s)
    assert s == "b ab\naab 123"
    assert t == "xxab\naaxx123"

def test18 () :
    s = "b ab\naab 123"
    t = re.sub("b.", "xx", s)
    assert s == "b ab\naab 123"
    assert t == "xxab\naaxx123"

def test19 () :
    s = "b ab\naab 123"
    t = re.sub("", "z", s)
    assert s == "b ab\naab 123"
    assert t == "zbz zazbz\nzazazbz z1z2z3z"

def main () :
    for n in range(19) :
        eval("test" + str(n + 1) + "()")

if __name__ == "__main__" : # pragma: no cover
    print("RegExps.py")
    main()
    print("Done.")
