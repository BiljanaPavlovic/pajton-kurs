from tkinter import *

def akcija(event):
    #print(event.char)
    tekst["text"] = event.char

root = Tk()
root.bind("<Key>",akcija)

tekst = Label(root,text = "")
tekst.pack()


root.mainloop()