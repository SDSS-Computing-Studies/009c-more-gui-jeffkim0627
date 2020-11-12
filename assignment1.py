import tkinter as tk 
from tkinter import *

win = tk.Tk()
win.title("triangle")
win.geometry("600x400")

a = 0
b = 0
c = 0
h = 0

def formula():
    a = int(Entrya.get())
    b = int(Entryb.get())
    c = int(Entryc.get())
    h = int(Entryh.get())

    if b > 0 and h > 0:
        A = b*h/2
        print(A)
    elif a > 0 and b > 0 and c > 0:
        s = int((a+b+c)/2)
        A = (s*(s-a)*(s-b)*(s-c))**(1/2)
        print(A)
    else :
        print("Area cannot be calculated with the information given")


trianglephoto = PhotoImage(file="triangle.png")
label1 = tk.Label(win, image=trianglephoto)
label2 = tk.Label(win, text="Enter in as much information about the \n trangle shown and I wil calculate the area")
Entrya = Entry(win, text="a", width=4)
Entryb = Entry(win, text="b", width=4)
Entryc = Entry(win, text="c", width=4)
Entryh = Entry(win, text="h", width=4)
Button1 = Button(win, text="Calculate", command=formula)



label1.grid(row=1, column=1)
label2.place(x=0, y=300)
Entrya.place(x=160 ,y=100)
Entryb.place(x=260 ,y=230)
Entryc.place(x=400 ,y=100)
Entryh.place(x=300 ,y=120)
Button1.place(x=300 ,y=300)



win.mainloop()