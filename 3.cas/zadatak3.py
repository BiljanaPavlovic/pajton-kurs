broj=int(input("Unesite broj:"))

if broj%2==0:
    if broj>10:
        print('Broj koji ste uneli je paran i veci od 10')
    else:
        print('Broj koji ste uneli je paran i manji od 10.')

else:
    if broj>5 and broj<30:
        print('Broj je neparan, a u opsegu je.')
    else:
        print("Neparan je i nije u opsegu")
