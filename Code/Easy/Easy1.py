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

def easy7(x, y, z):
    s = ""
    for i in range(10):
        s += str(easy6(x, y, z))
    return s

def easy8(a):
    list = a.split(",")
    return list[0]

def easy9(a):
    list = a.split(",")
    if len(list) != 10:
        return "Wrong number of inputs"
    x = ""
    for i in list:
        x += i
    return x

def easy10(a):
    list = a.split(",")
    if len(list) != 10:
        return "Wrong number of inputs"
    output = ""
    nlist = []
    for i in range(len(list)):
        nlist.append(int(list[i]))
        output += list[i]
    for i in range(len(nlist)):
        nlist[i] *= 10
        output += str(nlist[i])
    return output

def easy11(a):
    list = a.split(",")
    if len(list) != int(list[0]) + 1:
        return "Wrong number of inputs"
    output = ""
    nlist = []
    for i in range(1, int(list[0]) + 1):
        nlist.append(int(list[i]))
        output += list[i]
    for i in range(len(nlist)):
        nlist[i] *= 10
        output += str(nlist[i])
    return output

def easy12(num, action):
    if action.lower() != "double"and action.lower() != "triple":
        return "Incorrect Action"
    if action.lower() == "double":
        return num * 2
    if action.lower() == "triple":
        return num * 3

def easy_grade(maths, chemistry, physics):
    tscore = maths + chemistry + physics
    pscore = round((tscore * 100) / 300)
    if pscore >= 70:
        return str(pscore) + "% - A Grade"
    if pscore >= 60:
        return str(pscore) + "% - B Grade"
    if pscore >= 50:
        return str(pscore) + "% - C Grade"
    if pscore >=40:
        return str(pscore) + "% - A Grade"
    else:
        return "You Failed"

def easy_isbn(isbn):
    a = isbn.replace("-", "")
    idx = 1
    cdigit = 0
    for v in a:
        if idx % 2 == 0:
            cdigit += (int(v) * 3)
        else:
            cdigit += int(v)
        idx +=1
    cdigit = int(cdigit / 10)
    return isbn + str(cdigit)

#def easy_near(a)

def easy_ttable(num):
    a = ""
    for i in range(13):
        if i == 0:
            a = "0"
        else:
            a += ";"+str(num * i)
        return a