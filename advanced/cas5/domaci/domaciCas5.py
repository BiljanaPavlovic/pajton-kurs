import os, shutil, zipfile

if os.path.exists('materijal') == False:
    os.makedirs('materijal')
else:
    print('Direktorijum vec postoji!')


lokacija_datoteka = 'C:\\Users\\zver\\Desktop\\pajton kurs\\advanced\\cas5\\domaci'

print(os.listdir(lokacija_datoteka))

fajlovi = os.listdir(lokacija_datoteka)

for i in fajlovi:
    stara_lokacija = lokacija_datoteka + "\\" + i
    nova_lokacija = "materijal\\" + i
    shutil.copy(stara_lokacija, nova_lokacija )

novi_fajlovi = os.listdir("materijal")
print(novi_fajlovi)

brojac = 1
for j in novi_fajlovi:
    ekstenzija = j.split(".")
    print(ekstenzija)
    os.rename("materijal\\"+j, "materijal\\"+ str(brojac)+"."+ekstenzija[1])
    brojac+=1



fajl = zipfile.ZipFile("materijal.zip", 'w')
novi_fajlovi = os.listdir("materijal")

for k in novi_fajlovi:
    fajl.write("materijal" + k, compress_type=zipfile.ZIP_DEFLATED)

fajl.close()