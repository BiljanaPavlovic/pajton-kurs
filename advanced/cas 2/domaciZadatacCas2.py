##definisanje klase

class Knjige:

    def __init__(self, naziv, autor, isbn):
        self.naziv = naziv
        self.autor = autor
        self.isbn = isbn

    def prikaz_naziva(self):
        print(f'Naziv knjige je: {self.naziv}')

#dodavanje objekata u klasu

knjiga1 = Knjige('Osnove programiranja u Pajtonu', 'Milos Kovacevic', '978-86-7466-709-5')
knjiga2 = Knjige('Osnovi telekomunikacije','Ilija Stojanovic', '86-7621-090-x')

########################################
#pozivanje metode

knjiga1.prikaz_naziva()
knjiga2.prikaz_naziva()


