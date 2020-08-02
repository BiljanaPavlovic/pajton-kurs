from random import randint

class Igrac:

    poeni = 0

    def __init__(self, ime):
        self.ime = ime

    def dodaj_poen(self):
        self.poeni+=1

    def prikaz_poena(self):
        print(f'{self.ime} trenutno ima {self.poeni}')

#########################################

igrac = Igrac(input('Unesite ime korisnika:'))



#############################################
while True:

    broj = randint(1,20)

    for i in range(5, 0, -1):
        pogodak = int(input('Unesite broj:'))

        if pogodak == broj:
            print('Bravo! Pogodili ste broj.!')
            igrac.dodaj_poen()
            break
        if pogodak < broj:
            print('Broj koji ste uneli je manji od zamisljenog.')
           
        if pogodak > broj:
            print('Broj koji ste uneli je veci od zamisljenog.')


        print(f'Ostalo vam je jos {i-1} pokusaja.')

    print(f'Racunar je zamislio broj {broj}.')
    igrac.prikaz_poena()

    pitanje = input('Da li zelite ponovo da igrate D/N:')
    while pitanje.lower() not in ['d', 'n']:
        pitanje = input('Uneli ste pogresno slovo, pokusajte ponovo:')

    if pitanje == 'n':
        break
 

print()