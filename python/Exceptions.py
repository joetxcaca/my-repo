#!/usr/bin/env python3

# pylint: disable = eval-used
# pylint: disable = invalid-name
# pylint: disable = line-too-long
# pylint: disable = literal-comparison
# pylint: disable = missing-docstring

# -------------
# Exceptions.py
# -------------

# https://docs.python.org/3/library/exceptions.html

def f (b: bool) -> int :
    if b :
        raise NameError("abc")
    return 0

def test1 () -> None :
    try :
        assert f(False) == 0
    except NameError :       # pragma: no cover
        assert False
    else :                   # no exception vs. raised and handled, but not with break, continue, return
        pass
    finally :                # always, even with break, continue, return
        pass

def test2 () -> None :
    try :
        assert f(True) == 1
        assert False                         # pragma: no cover
    except NameError as e :
        assert isinstance(e,      NameError)
        assert isinstance(e.args, tuple)
        assert len(e.args)  ==     1
        assert e.args       is not ("abc",)
        assert e.args       ==     ("abc",)
    else :                                   # no exception vs. raised and handled, but not with break, continue, return
        assert False                         # pragma: no cover
    finally :                                # always, even with break, continue, return
        pass

def test3 () -> None :
    assert issubclass(NameError,     Exception)
    assert issubclass(Exception,     BaseException)
    assert issubclass(BaseException, object)

def main () -> None :
    print("Exceptions.py")
    for i in range(3) :
        eval("test" + str(i + 1) + "()")
    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    main()
