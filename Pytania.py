import tkinter
import sqlite3

import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()

def stworz_tabele(nazwa):
    c.execute("""CREATE TABLE """+nazwa+""" (
            pytanie text,
            odp1 text,
            odp2 text,
            odp3 text,
            odp4 text,
            correct integer
            )""")


def insert_question(nazwa,pytanie,odp1,odp2,odp3,odp4,correct):
    with conn:
        c.execute("INSERT INTO "+nazwa+" VALUES (:pytanie, :odp1, :odp2, :odp3, :odp4, :correct)", {'pytanie': pytanie,'odp1':odp1,'odp2':odp2,'odp3':odp3,'odp4':odp4,'correct':correct})

def gettables():
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    temp = c.fetchall()
    tab = []
    for i in temp:
        slowo = ''.join(i)
        tab.append(slowo)
    return tab


def get_pytanie(nazwa):
    c.execute("SELECT pytanie FROM "+nazwa+";")
    return c.fetchall()

def get_odp1(nazwa):
    c.execute("SELECT odp1 FROM "+nazwa+";")
    return c.fetchall()

def get_odp2(nazwa):
    c.execute("SELECT odp2 FROM "+nazwa+";")
    return c.fetchall()

def get_odp3(nazwa):
    c.execute("SELECT odp3 FROM "+nazwa+";")
    return c.fetchall()

def get_odp4(nazwa):
    c.execute("SELECT odp4 FROM "+nazwa+";")
    return c.fetchall()

def get_correct(nazwa):
    c.execute("SELECT correct FROM "+nazwa+";")
    return c.fetchall()

conn.close()

def baza():
    lista = [["Rodzaje marketingu","cyfrowy,szeptany,internetowy,ambient marketing","biologiczny, historyczny","sam juz nie wiem","agresywny,pasywny",1],["Podaj jakosc","1","2","3","4",2]]
    return lista
