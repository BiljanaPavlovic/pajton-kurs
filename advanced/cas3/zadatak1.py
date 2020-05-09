from math import sqrt
##############################


class Tacka:
    def __init__(self, ime, x, y):
        self.ime = ime
        self.x = x
        self.y = y


    def info(self):
        print(f'Naziv {self.ime}\n  ({self.x}, {self.y}) ')


def tacke():
    global tacka_a, tacka_b
    koordinate_a = []
    koordinate_b = []

    
    koordinate_a.append(int(input('Unesite koordinatu x za prvu tacku:')))
    koordinate_a.append(int(input('Unesite koordinatu y za prvu tacku:')))
    
    koordinate_b.append(int(input('Unesite koordinatu x za prvu tacku:')))
    koordinate_b.append(int(input('Unesite koordinatu y za prvu tacku:')))

    tacka_a = Tacka('A', koordinate_a[0], koordinate_a[1])
    tacka_b = Tacka('B', koordinate_b[0], koordinate_b[1])


def rastojanje():
    rastojanje = sqrt((tacka_a.x-tacka_b.x)**2 + (tacka_a.y-tacka_b.y)**2)
    print(f'Rastojanje izmedju tacaka {tacka_a.ime} i {tacka_b.ime} je: {rastojanje}.')


###############################################


tacke()
rastojanje()
