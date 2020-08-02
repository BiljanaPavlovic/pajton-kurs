class Pas: 

    def __init__(self,x, y, z):
        self.rasa = x
        self.ime = y
        self.starost = z

    def lajanje(self):
        print('Av, av!')

###############################

pas1 = Pas('srpski gonic', 'Meda', 1)

print(pas1.ime)

pas2 = Pas('pulin','Maza',9)

print(pas2.rasa)

print(type(pas2))

pas2.lajanje()