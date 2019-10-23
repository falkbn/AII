from bs4ejercice_2 import database as db
from tkinter import messagebox
from datetime import datetime


def datos_cargar():
    conn = db.create_database()
    cursor = conn.cursor()

    try:
        datablock = db.get_soup().find_all('div', class_='news-body')
        for data in datablock:
            titulo = data.find('div', class_='center-content').h2.text.strip()
            print(titulo)
            enlace = data.find('div', class_='center-content').a['href']
            print(enlace)
            autor = data.find('div', class_='news-submitted').find_all('a')[1].text
            print(autor)
            fecha = data.find_all('span', class_='ts visible')[1]['data-ts']
            fecha = str(datetime.fromtimestamp(int(fecha)))
            print(fecha)
            contenido = data.find('div', class_='news-content').text
            print(contenido)
            print()

            cursor.execute('INSERT INTO noticias VALUES(?,?,?,?,?)',
                           (titulo, enlace, autor, fecha, contenido))
            conn.commit()
            cursor.execute('SELECT COUNT(*) FROM noticias')
            c = cursor.fetchone()

        db.disconnect(conn)
        var = 'Base de datos creada correctamente con ' + str(c[0]) + ' entradas'

    except ValueError as e:
        var = 'Error al crear la base de datos'
        print(e)

    messagebox.showinfo('Base de datos', var)


def datos_mostrar():
    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute('SELECT titulo, autor, fecha FROM noticias')
    noticias = cursor.fetchall()
    return [x[1] + ': ' + x[0] + ' || ' + x[2] for x in noticias]


def busq_autor():
    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute('SELECT autor FROM noticias')
    autores = cursor.fetchall()
    return [x[0] for x in autores]


def busq_fecha():
    None