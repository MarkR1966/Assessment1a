a = input("Enter number 1 : ")
b = input("Enter number 2 : ")
f = input("Enter True/False")
if f == "True":
    print(a, " + ", b, " = ", int(a) + int(b))
elif f=="False":
    print(a, " * ", b, " = ", int(a) * int(b))
else:
    print("Not True or False")