def easy1():
    return "Hello World"

def easy2():
    a = "Hello World"
    return a

def easy3(a):
    return a

def easy4(a, b):
    return a + b

def easy5(a, b, l):
    if l:
        return a + b
    else:
        return a * b

def easy6(a, b, l):
    if a == 0 and b == 0:
        return ""
    if a == 0:
        return b
    if b == 0:
        return a
    if l:
        return a + b
    else:
        return a * b

#def easy7():

def easy8(a):
    list = a.split(",")
    return list[0]

