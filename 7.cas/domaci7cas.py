
brojBrojeva=input('Koliko brojeva zelite da unesete?')
broj_brojeva=int(brojBrojeva)
brojevi=[]
suma=0

while broj_brojeva>=1:
    uneti_brojevi=int(input("Unesite broj:"))
    suma=suma+uneti_brojevi
    broj_brojeva=broj_brojeva-1
    brojevi.append(uneti_brojevi)

srednja_vrednost=suma/int(brojBrojeva)
print('Uneli ste sledece brojeve:',brojevi)
print('Njihov zbir je:',suma)

print('A srednja vrednost je:',srednja_vrednost)

