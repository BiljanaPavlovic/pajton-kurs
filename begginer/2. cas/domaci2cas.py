
#unos maticnog broja
maticni_broj=input('Unesite maticni broj:')

#izvlacim datum

dan=maticni_broj[0:2]#.lstrip[0]
mesec=maticni_broj[2:4]#.lstrip[0]
godina=maticni_broj[4:7]

datum=dan.lstrip('0')+'.'+mesec.lstrip('0')+'.'+'1'+godina+'.'

#zbir osme i devete cifre

zbir=int(maticni_broj[7])+int(maticni_broj[8])

#ispisivanje podataka
print('Maticni broj',maticni_broj)
print('Datum rodjenja je:',datum)
print('Zbir osme i devete cifre je',zbir)

