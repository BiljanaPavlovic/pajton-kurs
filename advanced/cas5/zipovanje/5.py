class Osoba:

    def __init__(self, pol, ime, visina, tezina):
        self.pol = pol
        self.ime = ime
        self.visina = visina
        self.tezina = tezina

    def info(self):
        print(f'Ime: {self.ime}\n pol: {self.pol}\n visina: {self.visina} \n tezina: {self.tezina}')

    def predstavi(self):
        print(f'Ja sam {self.ime}.')
######################################

osoba1 = Osoba('z', 'Biljana', '1.68', '75')

osoba2 = Osoba('m','Marko',1.82,85)
osoba1.info()
osoba2.info()
osoba1.predstavi()
osoba2.predstavi()

