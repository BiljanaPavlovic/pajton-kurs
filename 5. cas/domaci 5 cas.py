from statistics import mean

studenti=[["Petar", "Petrovic"],["Marko","Markovic"]]

#unosimo ocene

ocena_petar=input("Unesite prosecnu ocenu studenta Petra:")
ocena_marko=input("Unesite prosecnu ocenu studenta Marka:")

#ocene smestamo u liste

studenti[0].append(ocena_petar)
studenti[1].append(ocena_marko)

#status studenta

if float(ocena_petar)>=8.5:
    print("Petar je na budzetu.")
else:
    print("Petar je na samofinansiranju.")


if float(ocena_marko)>=8.5:
    print("Marko je na budzetu.")
else:
    print("Marko je na samofinansiranju.")


#dodajemo podatke o stanovanju

studenti[0].insert(1,"Pancevo")
studenti[1].insert(1,"Zemun")



#prosecna ocena studenata
ocene=[]
ocene.append(float(ocena_petar))
ocene.append(float(ocena_marko))
prosecna_ocena=mean(ocene)

print("Prosecna ocena studenata je:",prosecna_ocena)

#sortiranje liste
studenti[0].sort()
studenti[1].sort()
studenti.sort()

print(studenti)
