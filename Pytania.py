import tkinter
import sqlite3

import sqlite3

conn = sqlite3.connect('baza.db')

c = conn.cursor()


def stworz_tabele(nazwa):
    c.execute("""CREATE TABLE """ + nazwa + """ (
            nr integer,
            pytanie text,
            odp1 text,
            odp2 text,
            odp3 text,
            odp4 text,
            correct integer
            )""")


def insert_question(nazwa, nr, pytanie, odp1, odp2, odp3, odp4, correct):
    with conn:
        c.execute("INSERT INTO " + nazwa + " VALUES (:nr, :pytanie, :odp1, :odp2, :odp3, :odp4, :correct)", {'nr': nr,
                                                                                                             'pytanie': pytanie,
                                                                                                             'odp1': odp1,
                                                                                                             'odp2': odp2,
                                                                                                             'odp3': odp3,
                                                                                                             'odp4': odp4,
                                                                                                             'correct': correct})


def gettables():
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    temp = c.fetchall()
    tab = []
    for i in temp:
        slowo = ''.join(i)
        tab.append(slowo)
    return tab


def get_pytanie(nazwa):
    c.execute("SELECT pytanie FROM " + nazwa + ";")
    temp = c.fetchall()
    tab = []
    for i in temp:
        slowo = ''.join(i)
        tab.append(slowo)
    return tab

def get_calosc(nazwa,nr):
    c.execute("SELECT pytanie, odp1, odp2, odp3, odp4, correct FROM " + nazwa + " WHERE nr=:nr",{'nr':nr})
    temp = c.fetchall()
    return temp

def get_odp1(nazwa):
    c.execute("SELECT odp1 FROM " + nazwa + ";")
    temp = c.fetchall()
    tab = []
    for i in temp:
        slowo = ''.join(i)
        tab.append(slowo)
    return tab


def get_odp2(nazwa):
    c.execute("SELECT odp2 FROM " + nazwa + ";")
    temp = c.fetchall()
    tab = []
    for i in temp:
        slowo = ''.join(i)
        tab.append(slowo)
    return tab

def get_odp3(nazwa):
    c.execute("SELECT odp3 FROM " + nazwa + ";")
    temp = c.fetchall()
    tab = []
    for i in temp:
        slowo = ''.join(i)
        tab.append(slowo)
    return tab

def get_odp4(nazwa):
    c.execute("SELECT odp4 FROM " + nazwa + ";")
    temp = c.fetchall()
    tab = []
    for i in temp:
        slowo = ''.join(i)
        tab.append(slowo)
    return tab

def get_ilosc(nazwa):
    c.execute("SELECT odp4 FROM " + nazwa + ";")
    temp = c.fetchall()
    return int(len(temp))

def get_correct(nazwa):
    c.execute("SELECT correct FROM " + nazwa + ";")
    temp = c.fetchall()
    tab = []
    for i in temp:
        slowo = ''.join(i)
        tab.append(slowo)
    return tab





#
#pytanie1 = ["Co to PyCharm?", "Najnowsza gra", "Książka autorstwa mr. Charm", "Środowisko do programowania"
#        , "Sam juz nie wiem", 3]
#pytanie2 = ["Co daje funkcja print ?", "Pozwala wyświetlic dany ciag znakow", "Dzięki niej możesz dostać + 20 exp"
#        , "Taka funkcja nie istnieje", "Sluzy do nauki gry na gitarze", 1]
#pytanie3 = ["""Poprzez wyrazenie "def" definiuje sie: """, "Mechanizmy", "Slowniki", "Listy", "Procedury", 4]
#pytanie4 = ["""Wyrazeniem "import" można: """, "Odwolywac sie do innych programow", "Importowac biblioteki"
#        , "Zawiesic komputer", "Importowac inne programy", 2]
#pytanie5 = ["""Wyrazenie "s.count(x)": """, "Zlicza wystepowanie wyrazen x w liscie s", "Zlicza bledy w liscie s"
#        , "Sumuje wyniki o indeksie x w procedurze s", "Zlicza wyrazenia s w liscie x", 1]
#pytanie6 = ["""Funkcja "len()": """, "Tworzy liste len", "Pozwala na budowanie szeregow funkcyjnych"
#        , "Zwraca ilosc elementow listy", "Podaje wspolczynnik zmiennosci", 3]
#pytanie7 = ["""Funkcja "s.remove(x)" jest pozyteczna przy: """, "Wyszukiwaniu okreslonego elementu z listy"
#        , "Usuwaniu okreslonego elementu z listy", "Przesunieciu elementu z listy o wektor x"
#        , "Dodawaniu okreslonegoelemtu z listy", 2]
#pytanie8 = ["""Funkcja "range(n,x)": """, "Dzieli liczbe n przez x"
#        , "Tworzy dwa argumenty procedury n i x", "Zwraca reszte z dzielenia n i x", "Tworzy liste znakow od n do x", 4]
#

