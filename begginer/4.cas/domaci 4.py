indeks=input("Unesite broj indeksa:").upper()
#godina upisa
godina_upisa="20"+indeks[2:4]
print("Fakultet ste upisali",godina_upisa,"godine")
#modul
if indeks[0:2]=="PS":
    print("Modul postanski saobracaj i mreze.")
elif indeks[0:2]=="LO":
    print("Modul logistika.")
elif indeks[0:2]=="VZ":
    print("Modul vazdusni saobracaj i transport.")
elif indeks[0:2]=="VD":
    print("Modul vodeni saobracaj i transport.") 
elif indeks[0:2]=="DT":
    print("Modul drumski i gradski transport.")  
elif indeks[0:2]=="DS":
    print("Modul drumski i gradski saobracaj.")  
elif indeks[0:2]=="ZE":
    print("Modul zeleznicki saobracaj i transport.")   
else:
    print("Modul nije validan.")
#akreditacija
if int(godina_upisa)>2006 and int(godina_upisa)<2009:
    print("Akreditacija 06.")
elif int(godina_upisa)>2009 and int(godina_upisa)<2014:
    print("Akreditacija 09")
elif int(godina_upisa)>2014 and int(godina_upisa)<2020:
    print("Akreditacija 14.")
elif int(godina_upisa)>2020:
    print("Akreditacija 20.")
else:
    print("Broj indeksa nije validan.")


#PS130211
#VD150245
