
zaposleni=[]
prezime_ime=[]
datumi=[]
broj_zaposlenih=int(input('Koliko vasa firma ima zaposlenih?'))
sum=0


for i in range(0,broj_zaposlenih):
    x=[]
    ime=input('Upisite ime zaposlenog:')
    prezime=input('Upisite prezime zaposlenog:')
    #inicijali
    inicijali=ime[0]+'.'+prezime[0]+'.'
    jmbg=input('Upisite jmbg zaposlenog:')
    if len(jmbg)!=13:
        print("Pogresan jmbg broj.")
        input("upisite ispravan broj:")
    else:
        #datum
        datum=int(jmbg[0:7])

        #pol
        if int(jmbg[9:12])<499 and int(jmbg[9:12])>0:
            pol='muski'
        elif int(jmbg[9:12])>500 and int(jmbg[9:12])<999:
            pol='zenski'
        else:
            print("Pogresan jmbg")
    planta=int(input('Upisite platu zaposlenog:'))
    
    x.append(ime)
    x.append(prezime)
    x.append(jmbg)
    x.append(planta)
    x.append(inicijali)
    x.append(datum)
    x.append(pol)
    zaposleni.append(x)
    sum=sum+planta
    prezime_ime.insert(0,prezime)
    prezime_ime.insert(1,ime)
        
    print("Prezime i ime",zaposleni[i][1],zaposleni[i][0])
    print("JMBG zaposlenih je:",zaposleni[i][2])
    print('Inicijali zaposlenih su:',zaposleni[i][4])
    print('Datum rodjenja:',zaposleni[i][5])
    print("Pol:",zaposleni[i][6])
        



print(zaposleni)



prosecna_plata=sum/broj_zaposlenih
print("Prosecna plata u Vasem preduzecu je:",prosecna_plata)



print()