# Author: Antonio

from practice_1 import database
from bs4 import BeautifulSoup
import urllib.request
import tkinter as tk

url = "https://foros.derecho.com/foro/20-Derecho-Civil-General/page"


def cargar():
    # Refresh db data
    con = database.create_database()
    cursor = con.cursor()
    pages = 3
    publications = []
    for i in range(pages):
        # Request html
        request = urllib.request.urlopen(url + str(i + 1))
        html = request.read()
        request.close()

        # Filter data
        soup = BeautifulSoup(html, "html.parser")
        datablock = soup.findAll("li", {"class": "threadbit"})

        for d in datablock:
            title = d.find("a", {"class": "title"})["title"]
            link = d.find("a", {"class": "title"})["href"]
            author = d.find("a", {"class": "username"}).text
            date = d.find("a", {"class": "username"})["title"][-16:]
            responses = d.findAll("li")[0].text
            visits = d.findAll("li")[1].text
            publications.append((title, link, author, date, responses[12:], visits[9:]))

    sql = "insert into publication(title, link, author, date, responses, visits) values (?, ?, ?, ?, ?, ?)"
    con.executemany(sql, publications)
    sql = "select count(*) from publication"
    cursor.execute(sql)
    pub_number = cursor.fetchone()

    # Informamos de las publicaciones añadidas
    win = tk.Toplevel()
    win.title("Información")
    l = tk.Label(win, text="Se han almacenado " + str(pub_number[0]) + " comunicaciones.")
    l.grid(row=0, column=0)
    con.commit()
    con.close()


def mostrar():
    # Informamos de las publicaciones añadidas
    win = tk.Toplevel()
    win.title("Mostrando publicaciones")

    scrollbar = tk.Scrollbar(win)
    scrollbar.pack(side="right", fill="y")

    l = tk.Listbox(win, yscrollcommand=scrollbar.set)
    l.pack(fill="both", expand=True)

    con = database.get_db_connection()
    cursor = con.cursor()
    sql = "select title, author, date from publication"
    cursor.execute(sql)
    for item in cursor.fetchall():
        l.insert(tk.END, item)

        scrollbar.config(command=l.yview)
    con.close()


def buscar_tema():
    win = tk.Toplevel()
    win.title("Buscar tema")
    entry = tk.Entry(win)
    entry.pack()
    button = tk.Button(win, text="Buscar", command=lambda: get_title(entry.get()))
    button.pack()


def buscar_fecha():
    win = tk.Toplevel()
    win.title("Buscar tema")
    entry = tk.Entry(win)
    entry.pack()
    button = tk.Button(win, text="Buscar", command=lambda: get_date(entry.get()))
    button.pack()


def temas_populares():
    con = database.get_db_connection()
    cursor = con.cursor()
    sql = "select title, author, date, visits from publication order by visits desc limit 5"
    cursor.execute(sql)

    win = tk.Toplevel()
    win.title("Temas populares")

    scrollbar = tk.Scrollbar(win)
    scrollbar.pack(side="right", fill="y")

    l = tk.Listbox(win, yscrollcommand=scrollbar.set)
    l.pack(fill="both", expand=True)
    for item in cursor.fetchall():
        l.insert(tk.END, item)

    scrollbar.config(command=l.yview)

    con.close()


def temas_activos():
    con = database.get_db_connection()
    cursor = con.cursor()
    sql = "select title, author, date, responses from publication order by responses desc limit 5"
    cursor.execute(sql)

    win = tk.Toplevel()
    win.title("Temas activos")

    scrollbar = tk.Scrollbar(win)
    scrollbar.pack(side="right", fill="y")

    l = tk.Listbox(win, yscrollcommand=scrollbar.set)
    l.pack(fill="both", expand=True)
    for item in cursor.fetchall():
        l.insert(tk.END, item)

    scrollbar.config(command=l.yview)

    con.close()


def get_title(title):
    con = database.get_db_connection()
    cursor = con.cursor()
    sql = "select title, author, date from publication where title like ?"
    cursor.execute(sql, ("%" + title + "%",))

    win = tk.Toplevel()
    win.title("Mostrando publicaciones")

    scrollbar = tk.Scrollbar(win)
    scrollbar.pack(side="right", fill="y")

    l = tk.Listbox(win, yscrollcommand=scrollbar.set)
    l.pack(fill="both", expand=True)
    for item in cursor.fetchall():
        l.insert(tk.END, item)

    scrollbar.config(command=l.yview)

    con.close()


def get_date(title):
    con = database.get_db_connection()
    cursor = con.cursor()
    sql = "select title, author, date from publication where date like ?"
    cursor.execute(sql, ("%" + title + "%",))

    win = tk.Toplevel()
    win.title("Mostrando publicaciones")

    scrollbar = tk.Scrollbar(win)
    scrollbar.pack(side="right", fill="y")

    l = tk.Listbox(win, yscrollcommand=scrollbar.set)
    l.pack(fill="both", expand=True)
    for item in cursor.fetchall():
        l.insert(tk.END, item)

    scrollbar.config(command=l.yview)

    con.close()
