from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
#import math
from math import sqrt
from PIL import ImageTk, Image

#----------------------

def resenja():
    a = float(param_a.get())
    b = float(param_b.get())
    c = float(param_c.get())

    D = b**2-4*a*c

    if D>0:
        x1 = (-b+sqrt(D))/(2*a)
        x2 = (-b-sqrt(D))/(2*a)
        resenja["text"]=f"Решења су реална и различита.\nx1 = {x1}\nx2 = {x2}"
        grafik(a,b,c)
    if D==0:
        x = -b/(2*a)
        resenja["text"]=f"Решења су реална и једнака.\nx1 = {x}\nx2 = {x}"
        grafik(a,b,c)
    if D<0:
        resenja["text"]=f"Решења су конјуговано-комплексна."

def grafik(a,b,c):
    x = np.arange(-20,21)
    y = a*x**2+b*x+c
    plt.clf()
    plt.plot(x,y, label="График функције",zorder=4)
    plt.title("Квадратна једначина")
    plt.grid(zorder=1)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.savefig("grafik.jpg")

    global slika_pozicija

    slika_izvor = Image.open("grafik.jpg")
    slika_izvor = slika_izvor.resize((400,300), Image.ANTIALIAS)

    slika = ImageTk.PhotoImage(slika_izvor)

    slika_pozicija = Label(root,image=slika)
    slika_pozicija.image = slika
    slika_pozicija.grid(row=0, column=2, rowspan=3)

    

    
def obrisi():
    resenja["text"]=""

    param_a.delete(0,END)
    param_a.insert(0,"")

    param_b.delete(0,END)
    param_b.insert(0,"")

    param_c.delete(0,END)
    param_c.insert(0,"")

    slika_pozicija.destroy()

def novi_prozor():
    prozor = Toplevel(root)
    prozor.title("О програму")

    opis_programa = Message(prozor, text="Овај програм рачуна решења квадратне једначине на основу унетих параметара.\n\nАутор: Никола Ђорђевић")
    opis_programa.pack()

def izadji():
    root.destroy()

def saveres():
    datoteka = open("rezultat.txt","w",encoding="utf-8")

    

    datoteka.close()

#----------------------

root = Tk()


root.title("Квадратна једначина")

#Мени
meni = Menu(root)
podmeni = Menu(meni, tearoff=0)
podmeni.add_command(label="Сачувај резултат", command=saveres)
podmeni.add_command(label="Изађи", command=izadji)
meni.add_cascade(label="Датотека", menu=podmeni)
meni.add_command(label="О програму", command=novi_prozor)
root.config(menu=meni)

#Наслов
naslov = Label(root,text="Квадратна једначина")
naslov.grid(row=0, column=0, columnspan=2)

#Опис
opis = Message(root, text="Овај програм рачуна решења квадратна једначине на основу унетих параметара a, b и c.")
opis.grid(row=1, column=0, columnspan=2)

#Параметар а
param_a_tekst = Label(root, text="a   =", bg="red", fg="white", pady=20)
param_a_tekst.grid(row=2, column=0)

param_a = Entry(root, width=10)
param_a.grid(row=2, column=1)

#Параметар b
param_b_tekst = Label(root, text="b   =")
param_b_tekst.grid(row=3, column=0)

param_b = Entry(root, width=10)
param_b.grid(row=3, column=1)

#Параметар c
param_c_tekst = Label(root, text="c   =")
param_c_tekst.grid(row=4, column=0)

param_c = Entry(root, width=10)
param_c.grid(row=4, column=1)

#Дугме
dugme = Button(root, text="Израчунај", command=resenja)
dugme.grid(row=5,column=0)

#Поништи дугме
ponisti = Button(root, text="Поништи", command=obrisi)
ponisti.grid(row=5,column=1)

#Решења
resenja = Label(root, text="")
resenja.grid(row=4, column=2, rowspan=2, columnspan=2)


root.geometry("500x300")
root.mainloop()
