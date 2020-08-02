import os, shutil, zipfile

#1. pravljenje direktorijuma
if os.path.exists('zipovanje') == False:
    os.makedirs('zipovanje')
else:
    print('Direktorijum vec postoji!')

#2. kopiranje datoteka

lokacija_datoteka = 'C:\\Users\\zver\\Desktop\\pajton kurs\\advanced\\cas 2'

print(os.listdir(lokacija_datoteka))

fajlovi = os.listdir(lokacija_datoteka)

for i in fajlovi:
    stara_lokacija = lokacija_datoteka + "\\" + i
    nova_lokacija = ".\\zipovanje\\" + i
    shutil.copy(stara_lokacija, nova_lokacija )

novi_fajlovi = os.listdir(".\\zipovanje")
print(novi_fajlovi)

brojac = 1
for j in novi_fajlovi:
    ekstenzija = j.split(".")
    print(ekstenzija)
    os.rename(".\\zipovanje\\"+j, ".\\zipovanje\\"+ str(brojac)+"."+ekstenzija[1])
    brojac+=1

#os.rename('.\\zipovanje\\', ".\\zipovanje2\\")

### Zipovanje

fajl = zipfile.ZipFile(".\\zipovanje.zip", 'w')
novi_fajlovi = os.listdir(".\\zipovanje")

for k in novi_fajlovi:
    fajl.write(".\\zipovanje" + k, compress_type=zipfile.ZIP_DEFLATED)

fajl.close()