opstina=input("Upisite naziv opstine na kojoj zivite:")

duzina=len(opstina)

if duzina%4==0:
    print("Broj karaktera je deljiv sa 4")

elif opstina[0].isupper():
    print("Broj karaktera nije deljiv sa 4, a pocetno slovo je veliko")
else:
    print("Broj karaktera nije deljiv sa 4, a pocetno slovo je malo")
