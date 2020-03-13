import tkinter as tkr
from PIL import Image, ImageTk
import time
import Pytania
import random

root = tkr.Tk()
load = Image.open("Alg.png")
load = load.resize((610, 510), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)
nr1 = 1
nr2 = 1
lista = Pytania.baza()
it = []
it2 = []

def main(nr1,nr2):
    global odp,nrpytania
    odp = 0
    nrpytania = 0
    list = root.place_slaves()
    for l in list:
        l.destroy()
    list = root.pack_slaves()
    for l in list:
        l.destroy()
    print(nr1,nr2)
    HEIGHT = 500
    WIDTH = 600

    canvas = tkr.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    img = tkr.Label(root, image=render)
    img.image = render
    img.place(x=-5, y=-5)

    button1 = tkr.Button(root, text="Start", font=30,command = lambda : start(nr1,nr2))
    button1.place(relx = 0.5,rely = 0.5,relheight=0.1, relwidth=0.3,anchor = 'n')

    button2 = tkr.Button(root, text="Ustawienia", font=30, command = ustawienia)
    button2.place(relx=0.5, rely=0.65, relheight=0.1, relwidth=0.3, anchor='n')

def start(nr1,nr2):
    global it,it2
    it = []
    it2 = []
    for i in lista:
        for j in range(nr1):
            it.append(i)

    random.shuffle(it)
    pytania(it[nrpytania],nr2)

    #for i in lista:
    #    print(i)
    #    if pytania(i) != True:
    #        for j in range(nr2):
    #            it.append(i)
    #           random.shuffle(it
    #    else:
    #        it.remove(i)

def pytania(pytanie,ilosc):
    list = root.place_slaves()
    for l in list:
        l.destroy()
    list = root.pack_slaves()
    for l in list:
        l.destroy()


    var1 = tkr.IntVar()
    var2 = tkr.IntVar()
    var3 = tkr.IntVar()
    var4 = tkr.IntVar()

    label1 = tkr.Label(root, text=pytanie[0], font=30)
    label1.place(relx=0.2, rely=0.1, relheight=0.1, relwidth=0.7, anchor='n')

    label2 = tkr.Label(root, text=pytanie[1], font=20)
    label2.place(relx=0.15, rely=0.3, relheight=0.1, relwidth=0.7, anchor='w')

    label3 = tkr.Label(root, text=pytanie[2], font=20)
    label3.place(relx=0.15, rely=0.4, relheight=0.1, relwidth=0.7, anchor='w')

    label4 = tkr.Label(root, text=pytanie[3], font=20)
    label4.place(relx=0.15, rely=0.5, relheight=0.1, relwidth=0.7, anchor='w')

    label5 = tkr.Label(root, text=pytanie[4], font=20)
    label5.place(relx=0.15, rely=0.6, relheight=0.1, relwidth=0.7, anchor='w')

    check1 = tkr.Checkbutton(root, font=20, variable=var1)
    check1.place(relx=0.05, rely=0.25, relheight=0.1, relwidth=0.1, anchor='n')

    check2 = tkr.Checkbutton(root, font=20, variable=var2)
    check2.place(relx=0.05, rely=0.35, relheight=0.1, relwidth=0.1, anchor='n')

    check3 = tkr.Checkbutton(root, font=20, variable=var3)
    check3.place(relx=0.05, rely=0.45, relheight=0.1, relwidth=0.1, anchor='n')

    check4 = tkr.Checkbutton(root, font=20, variable=var4)
    check4.place(relx=0.05, rely=0.55, relheight=0.1, relwidth=0.1, anchor='n')

    button1 = tkr.Button(root, text="Dalej", font=20,command = lambda : czy_prawidlowe(pytanie[5],var1.get(),var2.get(),var3.get(),var4.get(),ilosc))
    button1.place(relx=0.8, rely=0.85, relheight=0.1, relwidth=0.2, anchor='n')

    button2 = tkr.Button(root, text="Sprawdz", font=20,
                         command=lambda: sprawdz(pytanie[5], label2,label3,label4,label5))
    button2.place(relx=0.6, rely=0.85, relheight=0.1, relwidth=0.2, anchor='n')

def sprawdz(nr,label1,label2,label3,label4):
    if nr == 1:
        label1.config(bg="green")
    elif nr == 2:
        label2.config(bg="green")
    elif nr == 3:
        label3.config(bg="green")
    elif nr == 4:
        label4.config(bg="green")

def czy_prawidlowe(prawidlowe,nr1,nr2,nr3,nr4,ilosc):
    global odp,nrpytania,it,it2

    if prawidlowe == 1:
        if nr1 == 1 and nr2 == 0 and nr3 == 0 and nr4 == 0:
            odp += 1
            nrpytania += 1
        else:
            odp -= 1
            for i in range(ilosc):
                it2.append(it[nrpytania])
    elif prawidlowe == 2:
        if nr1 == 0 and nr2 == 1 and nr3 == 0 and nr4 == 0:
            odp += 1
            nrpytania += 1
        else:
            odp -= 1
            for i in range(ilosc):
                it2.append(it[nrpytania])
    elif prawidlowe == 3:
        if nr1 == 0 and nr2 == 0 and nr3 == 1 and nr4 == 0:
            odp += 1
            nrpytania += 1
        else:
            odp -= 1
            for i in range(ilosc):
                it2.append(it[nrpytania])
    elif prawidlowe == 4:
        if nr1 == 0 and nr2 == 0 and nr3 == 0 and nr4 == 1:
            odp += 1
            nrpytania += 1
        else:
            odp -= 1
            for i in range(ilosc):
                it2.append(it[nrpytania])

    #print(len(it),nrpytania,odp)
    if nrpytania < len(it):
        pytania(it[nrpytania],ilosc)
        print(it,it2)
    elif nrpytania == len(it) and len(it2) > 0:
        it = it2
        it2 = []
        it = random.shuffle(it)
        nrpytania = 0
        pytania(it[nrpytania], ilosc)
        print("1")
    else:
        wynik(1,1)


def ustawienia():
    list = root.place_slaves()
    for l in list:
        l.destroy()
    list = root.pack_slaves()
    for l in list:
        l.destroy()

    var1 = tkr.IntVar()
    var2 = tkr.IntVar()
    var3 = tkr.IntVar()
    var4 = tkr.IntVar()
    var5 = tkr.IntVar()
    var6 = tkr.IntVar()
    var7 = tkr.IntVar()
    var8 = tkr.IntVar()

    label1 = tkr.Label(root, text = "Wybierz ilosc powtorzeń 1 pytania:", font = 20)
    label1.place(relx = 0.25,rely = 0.1,relheight=0.1, relwidth=0.7,anchor = 'n')

    label3 = tkr.Label(root, text="1             2            3             4", font=20)
    label3.place(relx=0.24, rely=0.3, relheight=0.1, relwidth=0.5, anchor='n')

    check1 = tkr.Checkbutton(root, font=20,variable = var1)
    check1.place(relx=0.1, rely=0.2, relheight=0.1, relwidth=0.2, anchor='n')

    check2 = tkr.Checkbutton(root, font=20,variable = var2)
    check2.place(relx=0.2, rely=0.2, relheight=0.1, relwidth=0.2, anchor='n')

    check3 = tkr.Checkbutton(root, font=20,variable = var3)
    check3.place(relx=0.3, rely=0.2, relheight=0.1, relwidth=0.2, anchor='n')

    check4 = tkr.Checkbutton(root, font=20,variable = var4)
    check4.place(relx=0.4, rely=0.2, relheight=0.1, relwidth=0.2, anchor='n')

    label2 = tkr.Label(root, text="Dodaj pytanie w razie bledu",font = 20)
    label2.place(relx=0.25, rely=0.5, relheight=0.1, relwidth=0.9, anchor='n')

    check5 = tkr.Checkbutton(root, font=20, variable = var5)
    check5.place(relx=0.1, rely=0.6, relheight=0.1, relwidth=0.2, anchor='n')

    check6 = tkr.Checkbutton(root, font=20, variable = var6)
    check6.place(relx=0.2, rely=0.6, relheight=0.1, relwidth=0.2, anchor='n')

    check7 = tkr.Checkbutton(root, font=20, variable = var7)
    check7.place(relx=0.3, rely=0.6, relheight=0.1, relwidth=0.2, anchor='n')

    check8 = tkr.Checkbutton(root, font=20, variable = var8)
    check8.place(relx=0.4, rely=0.6, relheight=0.1, relwidth=0.2, anchor='n')

    label4 = tkr.Label(root, text="1             2             3             4", font=20)
    label4.place(relx=0.24, rely=0.7, relheight=0.1, relwidth=0.5, anchor='n')

    button1 = tkr.Button(root, text="Dalej", font=30, command = lambda : ustawieniahelp(var1.get(),var2.get(),var3.get(),var4.get(),var5.get(),var6.get(),var7.get(),var8.get()))
    button1.place(relx=0.8, rely=0.85, relheight=0.1, relwidth=0.3, anchor='n')

def ustawieniahelp(nr1,nr2,nr3,nr4,nr5,nr6,nr7,nr8):
    lista1 = [nr1,nr2,nr3,nr4]
    lista2 = [nr5,nr6,nr7,nr8]

    if lista1.count(1) != 0:
        pk1 = lista1.index(1) + 1
    else:
        pk1 = 0
    if lista2.count(1) != 0:
        pk2 = lista2.index(1) + 1
    else:
        pk2 = 0

    main(pk1,pk2)

def wynik(pk1,pk2):
    global odp

    list = root.place_slaves()
    for l in list:
        l.destroy()
    list = root.pack_slaves()
    for l in list:
        l.destroy()

    label1 = tkr.Label(root, text="Twoj wynik to:  " + str(odp), font=30)
    label1.place(relx=0.5, rely=0.3, relheight=0.2, relwidth=0.7, anchor='n')

    button1 = tkr.Button(root, text="Dalej", font=30,
                         command=lambda: main(pk1,pk2))
    button1.place(relx=0.8, rely=0.85, relheight=0.1, relwidth=0.3, anchor='n')

main(nr1,nr2)

root.mainloop()