pitanje=input("Ovaj program radi, jel vam jasno?")

while pitanje.lower() not in ['d','n']:
    pitanje=input("Uneli ste pogresno slovo pokusajte ponovo.")

while pitanje=="n":
    pitanje=input("Ponovo objasnjenje, jel razumete?")
    while pitanje.lower() not in ['d','n']:
        pitanje=input("Uneli ste pogresno slovo pokusajte ponovo.")



datum=input("Unesite datum u gramaticki ispravnom obliku:").rstrip(".")

podaci=datum.split(".")

print(podaci)

#1. nacin
'''
if podaci[1]=="1":
    print("Mesec: januar")
elif podaci[1]=="2":
    print("Mesec: februar")
elif podaci[1]=="3":
    print("Mesec: mart")
elif podaci[1]=="4":
    print("Mesec: april")
elif podaci[1]=="5":
    print("Mesec: maj")
elif podaci[1]=="6":
    print("Mesec: jun")
elif podaci[1]=="7":
    print("Mesec: jul")
elif podaci[1]=="8":
    print("Mesec: avgust")
elif podaci[1]=="9":
    print("Mesec: septembar")
elif podaci[1]=="10":
    print("Mesec: oktobar")
elif podaci[1]==11"":
    print("Mesec: novembar")
elif podaci[1]=="12":
    print("Mesec: decembar")

'''
#2. nacin
mesec=[
    ['1','januar'],
    ['2','februar'],
    ['3','mart'],
    ['4','april'],
    ['5','maj'],
    ['6','jun'],
    ['7','jul'],
    ['8','avgust'],
    ['9','septembar'],
    ['10','oktobar'],
    ['11','novembar'],
    ['12','decembar']
]

x=0
while x<len(mesec):
    if podaci[1].lstrip("0")==mesec[x][0]:
        print("Mesec:",mesec[x][1])
        break
    x=x+1

#deljiva sa 400
#deljiva sa 4 i nije deljiva sa 100
#godina nije prestupna

if int(podaci[2])%400==0:
    print("Godina je prestupna")
elif int(podaci[2])%4==0 and int(podaci[2])%100!=0:
    print("Godina je prestupna")
else:
    print("Godina nije prestupna.")


















    


