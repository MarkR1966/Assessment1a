import time

def inter1(card1, card2):
    if card1 < 0 or card2 < 0:
        return "Input less than zero"
    if card1 >21 and card2 > 21:
        return "0"
    if card1 > 21:
        return str(card2)
    if card2 > 22:
        return str(card1)
    if card1 >= card2:
        return str(card1)
    if card2 >= card1:
        return str(card2)

def inter2(values):
    list = values.split(",")
    nlist=[]
    for i in list:
        if list.count(i) == 1:
            nlist.append(int(i))
    return sum(nlist)

def inter3(temperature,issummer):
    if issummer:
        maxtemp = 100
    else:
        maxtemp = 90
    if temperature >= 60 and temperature <= maxtemp:
        return True
    else:
        return False

def inter4(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return str(year)+" is a leap year"
            else:
                return str(year)+" is not a leap year"
        else:
            return str(year) + " is a leap year"
    else:
        return str(year)+" is not a leap year"

tic = time.perf_counter()
count = 2
for num in range(1, 3000000):
    for i in range(2, num):
        if num % i == 0:
            break
        else:
            count += 1
            break
toc = time.perf_counter()
print("There are "+str(count)+" prime numbers - calculated in ",{toc-tic}," seconds")

