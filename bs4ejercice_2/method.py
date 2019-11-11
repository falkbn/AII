from bs4ejercice_2 import database as db
from tkinter import messagebox
from datetime import datetime


def datos_cargar():
    None


def datos_mostrar():
    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute('SELECT titulo, autor, fecha FROM noticias')
    noticias = cursor.fetchall()
    return [x[1] + ': ' + x[0] + ' || ' + x[2] for x in noticias]


def get_autores():
    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute('SELECT autor FROM noticias')
    autores = cursor.fetchall()
    autores = sorted((set(autores)))
    return [x[0] for x in autores]


def get_noticia_autor(autor):
    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute('SELECT titulo, autor, fecha FROM noticias WHERE noticias.autor = ?', (autor,))
    noticias = cursor.fetchall()
    return [x[1] + ': ' + x[0] + ' ' + x[2] for x in noticias]


def get_fechas():
    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute('SELECT fecha FROM noticias')
    autores = cursor.fetchall()
    return [x for x in autores]


def get_noticia_fecha(fecha):
    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute('SELECT titulo, autor, fecha FROM noticias WHERE noticias.fecha LIKE ?', ('%' + fecha + '%',))
    noticias = cursor.fetchall()
    return [x[1] + ': ' + x[0] + ' ' + x[2] for x in noticias]
