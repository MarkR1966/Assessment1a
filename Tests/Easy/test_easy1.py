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

def test7():
    assert easy7(0, 2, True) == "2222222222"
    assert easy7(1, 0, False) == "1111111111"
    assert easy7(2, 5, False) == "10101010101010101010"
    assert easy7(2, 5, True) == "7777777777"
    assert easy7(-1, 3, True) == "2222222222"
    assert easy7(-1, 3, False) == "-3-3-3-3-3-3-3-3-3-3"
    assert easy7(0, 0, False) == ""
    assert easy7(0, 0, True) == ""


def test8():
    assert easy8("1,2,3,4,5,6,7,8,9,10") == "1"
    assert easy8("9,54,3,4,7,6,1,8,7,10") == "9"

def test9():
    assert easy9("1,2,3,4,5,6,7,8,9,10") == "12345678910"
    assert easy9("9,54,3,4,7,6,1,8,7,10") == "954347618710"
    assert easy9("-1,100,4,87,43,23,94,4,1,2") == "-1100487432394412"
    assert easy9("1,2,3") == "Wrong number of inputs"
    assert easy9("-1,100,4,87,43,23,94,4,1,2,5") == "Wrong number of inputs"

def test10():
    assert easy10("1,2,3,4,5,6,7,8,9,10") == "12345678910102030405060708090100"
    assert easy10("9,54,3,4,7,6,1,8,7,10") == "9543476187109054030407060108070100"
#    assert easy10("-1,100,4,87,43,23,94,4,1,2") == "-1100487432394412-1001000040870430230940401020"
    assert easy10("1,2,3") == "Wrong number of inputs"
    assert easy10("-1,100,4,87,43,23,94,4,1,2,5") == "Wrong number of inputs"

def test11():
    assert easy11("3,1,2,3") == "123102030"
    assert easy11("10,9,54,3,4,7,6,1,8,7,10") == "9543476187109054030407060108070100"
    assert easy11("4,1,2,3") == "Wrong number of inputs"
    assert easy11("10,-1,100,4,87,43,23,94,4,1,2,5") == "Wrong number of inputs"

def test12():
    assert easy12(3,"Double") == 6
    assert easy12(-3, "Triple") == -9
    assert easy12(0, "Double") == 0

def test_grade():
    assert easy_grade(50, 55, 55) == "53% - C Grade"
    assert easy_grade(75, 80, 93) == "83% - A Grade"
    assert easy_grade(59, 63, 65) == "62% - B Grade"
    assert easy_grade(45, 43, 47) == "45% - D Grade"
    assert easy_grade(33, 33, 33) == "You Failed"

def test_isbn():
    assert easy_isbn("978-0-306-40615-") == "978-0-306-40615-9"
    assert easy-isbn("123-4-421-12345-") == "123-4-421-12345-6"

#def test_near():

def test_ttable():
    assert easy_ttable(1) == "0,1,2,3,4,5,6,7,8,9,10,11,12"
    assert easy_ttable(3) == "0,3,6,9,12,15,18,21,24,27,30,33,36"
    assert easy_ttable(10) == "0,10,20,30,40,50,60,70,80,90,100,110,120"
