import random

x=1
ukupan_broj=int(input("Koliko brojeva zelite"))
suma=0
while x<11:
    slucajan_broj=random.uniform(1,100)
    suma=suma+slucajan_broj
    print(slucajan_broj)
    x+=1

srednja_vrednost=suma/ukupan_broj
print("Srednja vrednost:",srednja_vrednost)
