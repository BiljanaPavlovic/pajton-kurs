x=4

while x<=99:
    if(x%4==0):
        print("Broj je deljiv sa 4:",x)
    elif(x%3==0):
        print("Broj je deljiv sa 3:",x)
    elif(x%5==0):
        x+=1
        print("Broj je deljiv sa 5:",x)
    else:
        print("Broj ne ispunjava uslove.")
    x+=1
