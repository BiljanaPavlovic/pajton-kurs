prvo_ime=input("Unesite prvo ime:")
drugo_ime=input("Unesite drugo ime:")

prvo_duzina=len(prvo_ime.lower())
drugo_duzina=len(drugo_ime.lower())


if prvo_duzina<drugo_duzina:
    print("Ime",drugo_ime,"ima vise karaktera od",prvo_ime)
    
elif prvo_duzina>drugo_duzina:
    print("Ime",prvo_ime,"ima vise karaktera od",drugo_ime)
else:
    print("Oba imena su jednaka")
