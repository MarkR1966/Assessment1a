import pytest
from Code.Intermediate.Intermediate import *

def test_inter1():
    assert inter1(1,15) == "15"
    assert inter1(21,10) == "21"
    assert inter1(22,22) == "0"
    assert inter1(-1,10) == "Input less than zero"

def test_inter2():
    assert inter2("1,2,3") == 6
    assert inter2("2,2,3") == 3
    assert inter2("2,2,2") == 0
    assert inter2("7,2,3") == 12
    assert inter2("-1,2,3") == 4

def test_inter3():
    assert inter3(65,True) == True
    assert inter3(50, True) == False
    assert inter3(95, False) == False
    assert inter3(95, True) == True

def test_inter4():
    assert inter4(2017) == "2017 is not a leap year"
    assert inter4(2000) == "2000 is a leap year"
    assert inter4(1900) == "1900 is not a leap year"

