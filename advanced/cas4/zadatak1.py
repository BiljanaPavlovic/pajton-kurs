import os, shutil

print(os.getcwd())

os.chdir('C:\\Users\\zver\\Desktop')

print(os.getcwd())

if os.path.exists('Vezbanje333') == False:
    os.makedirs('Vezbanje333')
else:
    print('Direktorijum vec postoji!')


lokacija_fajla = 'C:\\Users\\zver\\Desktop\\pajton kurs\\advanced\\cas3\\zadatak2.py'
nova_lokacija = '.\\Vezbanje333\\zadatak2.py'

shutil.copy(lokacija_fajla, nova_lokacija)

print(os.path.basename(nova_lokacija))
print(f'Velicina fajla je {os.path.getsize(nova_lokacija)} B')