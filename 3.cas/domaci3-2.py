import math

x=int(input("Unesite vrednost x:"))

if x>0:
    y=(2*x-x**(1/3))/5+math.sqrt(x)-(x**3/4)
    print(y)

else:
    print("Vrednost x mora biti veca od 0.")
