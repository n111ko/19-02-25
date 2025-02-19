from tkinter import *
from _19_02_25 import *

def figuur():
    valik = var.get()
    if valik == 1:
        Vihmavari()
    elif valik == 2:
        Vaal()
    else:
        Prillid()
        print("Joonistan hiljem")

aken = Tk()
aken.geometry("800x400")
aken.title("Graafikud")
pealkiri = Label(aken, text = "Erinevad pildid Matplotlib abil", font = "Calibri 24", fg = "green", bg = "yellow", pady = 20, width = 200)

var = IntVar()
r1 = Radiobutton(aken, text = "Vihmavari", font = "Calibri 18", variable = var, value = 1, command = figuur)
r2 = Radiobutton(aken, text = "Vaal", font = "Calibri 18", variable = var, value = 2, command = figuur)
r3 = Radiobutton(aken, text = "Prillid", font = "Calibri 18", variable = var, value = 3, command = figuur)

pealkiri.pack()
r1.pack()
r2.pack()
r3.pack()
aken.mainloop()