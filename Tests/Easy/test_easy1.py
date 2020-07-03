import pytest
from Code.Easy.Easy1 import *

def test1():
    assert easy1() == "Hello World"


def test2():
    assert easy2() == "Hello World"

def test3():
    assert easy3("Hello World") == "Hello World"
    assert easy3("This is Python") == "This is Python"

def test4():
    assert easy4(1,2) == 3
    assert easy4(5,6) == 11

def test5():
    assert easy5(1,2,True) == 3
    assert easy5(1,2,False) == 2
    assert easy5(2,5,False) == 10
    assert easy5(2,5,True) == 7
    assert easy5(-1,3,True) == 2
    assert easy5(-1,3,False) == -3

def test6():
    assert easy6(0, 2, True) == 2
    assert easy6(1, 0, False) == 1
    assert easy6(2, 5, False) == 10
    assert easy6(2, 5, True) == 7
    assert easy6(-1, 3, True) == 2
    assert easy6(-1, 3, False) == -3
    assert easy6(0, 0, False) == ""
    assert easy6(0, 0, True) == ""

#def test7():

def test8():
    assert easy8("1,2,3,4,5,6,7,8,9,10") == "1"
    assert easy8("9,54,3,4,7,6,1,8,7,10") == "9"
