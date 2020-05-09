#import math
from math import sin, cos, radians, atan, sqrt

def unos_broja():
    unos=input('Unesite koliko mesta zelite da dodate u spisak:')
   
    while unos.isdecimal() ==False or int(unos) <2:
        unos=input('Uneli ste pogresnu vrednost, pokusajte ponovo:')

    unos=int(unos)
    return unos

def unos_podataka(x):
    global podaci
    podaci={}
    for i in range(x):
        mesto=input('Unesite naziv mesta')
        lat=float(input('Unesite geografsku sirinu'))
        lon=float(input('Unesite geografsku duzinu'))
        podaci[mesto] = {'lat': lat, "lon":lon}


def udaljenost():
    mesto_1=input("Izaberite prvo mesto:")
    while mesto_1 not in podaci.keys():
        mesto_1=input('Uneli ste nepostojece mesto, pokusajte ponovo:')

    mesto_2=input("Izaberite drugo mesto:")

    while mesto_2 not in podaci.keys():
        mesto_2=input('Uneli ste nepostojece mesto, pokusajte ponovo:')


    lat1 = radians(podaci[mesto_1]['lat'])
    lon1 = radians(podaci[mesto_1]['lon'])
    lat2 = radians(podaci[mesto_2]['lat'])
    lon2 = radians(podaci[mesto_2]['lon'])

    a = sin((lat2-lat1)/2)**2+cos(lat1)*cos(lat2)*sin((lon2-lon1)/2)**2

    c = 2 * atan(sqrt(a)/sqrt(1-a))
    rastojanje = 6373 * c

    print(f"Rastojanje izmedju dva mesta je {rastojanje} km")
##############################################

unos=unos_broja()
unos_podataka(unos)
udaljenost()