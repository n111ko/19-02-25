from tkinter import *
from _19_02_25 import *
global värv


def värvi_valik():
    värv = "white"
    if tekst.get() != "":
        tekst.configure(bg = "yellow")
        värv = tekst.get()

    else:
        tekst.configure(bg = "red")
    return värv

def figuur():
    global värv
    valik = var.get()
    värv = värvi_valik()
    if valik == 1:
        Vihmavari(värv)
    elif valik == 2:
        Vaal(värv)
    else:
        Prillid(värv)
        print("Joonistan hiljem")

aken = Tk()
aken.geometry("800x400")
aken.title("Graafikud")
pealkiri = Label(aken, text = "Erinevad pildid Matplotlib abil", font = "Calibri 24", fg = "green", bg = "yellow", pady = 20, width = 200)

var = IntVar()
r1 = Radiobutton(aken, text = "Vihmavari", font = "Calibri 18", variable = var, value = 1, command = figuur)
r2 = Radiobutton(aken, text = "Vaal", font = "Calibri 18", variable = var, value = 2, command = figuur)
r3 = Radiobutton(aken, text = "Prillid", font = "Calibri 18", variable = var, value = 3, command = figuur)

tekst = Entry(aken, font = "Calibri 24", fg = "green", bg = "yellow", width = 100)

nupp = Button(aken, text = "Värvi valik", font = "Calibri 24", command = värvi_valik)

pealkiri.pack() # place(x = ..., y = ...), grid(column = ..., row = ...)
tekst.pack()
nupp.pack
r1.pack()
r2.pack()
r3.pack()
aken.mainloop()