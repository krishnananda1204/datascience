from math import sqrt

a = float(input("a : "))
b = float(input("b : "))
c = float(input("c : "))

d = (b**2) - (4*a*c)

if d>0:

    sol1 = (((-b) - sqrt(d))/(2*a))
    sol2 = (((-b) + sqrt(d))/(2*a))
    print("The solution are: %f and %f" % (sol1,sol2))
else:
    print("No Roots")
    exit()