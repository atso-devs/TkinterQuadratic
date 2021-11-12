import math
import tkinter as tk
from tkinter import *

window = Tk()
window.title("Квадратное уравнение")
window.geometry('500x200')

A = StringVar()
B = StringVar()
C = StringVar()


def clicked():

    a = float(A.get())
    b = float(B.get())
    c = float(C.get())

    D = b ** 2 - 4 * a * c

    if(D > 0):
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        textRes.configure(text="Дискриминант = " + str(D) + "\n" + "X1 = "+str(x1) + "\n" + "X2 = " + str(x2))
    elif(D == 0):
        x = -b / (2 * a)
        textRes.configure(text="Дискриминат = 0 \n X = " + str(x))
    else:
        textRes.configure(text="Дискриминат < 0 \n Корней нет")





text1 = Label(window, text="Введите коэфициенты квадратного уравнения")
text1.grid(column=0, row=0)

textA = Label(window, text="A")
textA.grid(column=0, row=1)
txtInpA = Entry(window, width=15, textvariable=A)
txtInpA.grid(column=0, row=2)

textB = Label(window, text="B")
textB.grid(column=0, row=3)
txtInpB = Entry(window, width=15, textvariable=B)
txtInpB.grid(column=0, row=4)

textC = Label(window, text="C")
textC.grid(column=0, row=5)
txtInpC = Entry(window, width=15, textvariable=C)
txtInpC.grid(column=0, row=6)

btn = Button(window, text="Решить", command=clicked)
btn.grid(column=1, row=3)

textResTitle = Label(window, text="Результат")
textResTitle.grid(column=1, row=4)

textRes = Label(window, text="")
textRes.grid(column=1, row=5)







window.mainloop()