import os, shutil

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
    shutil.copy(lokacija_datoteka+'\\'+i, '.\\zipovanje\\'+i )