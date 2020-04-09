pitanje=input("Unesite sta zelite da izracunate:\n'\ta-celzijusi u farenhajte\n\te-farenhajte u celzijuse:").lower()

if pitanje=="a":
    ulaz=float(input("Unesite temperaturu u celzijusima"))
    izlaz=1.8*ulaz+32
    print("Ulazna temperatura je:",ulaz,"C")
    print("Izlazna temperatura je:",izlaz,"F")
    
elif pitanje=="e":
    ulaz=float(input("Unesite temperaturu u farenhajtima:"))
    izlaz=(ulaz-32)/1.8
    print("Ulazna temperatura je:",ulaz,"F")
    print("Izlazna temperatura je:", izlaz,"C")

else:
    print("Uneli ste pogresno slovo.")
    
