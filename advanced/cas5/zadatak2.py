
print("Otvaranje datoteke...")
datoteka = open(".\\test.txt","w", encoding="utf-8")

print("Upisivanje podataka u datoteku")
datoteka.write("Biljana Pavlovic\nPajton - napredni nivo")

print("Zatvaranje datoteke")
datoteka.close()

print("Otvaranje datoteke za citanje")
fajl = open("test.txt","r",encoding="utf-8")

print("prikaz teksta...")
#print(fajl.readlines())

for i in fajl.readlines():
    print(i.rstrip("\n"))

fajl.close()