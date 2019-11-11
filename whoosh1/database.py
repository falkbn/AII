import sqlite3
import requests
from bs4 import BeautifulSoup

database = 'database.db'


def get_soup(page_index):
    i = 1
    soup = []
    while i <= page_index:
        source = requests.get('http://www.sensacine.com/noticias/?page=' + str(i)).text
        soup.append(BeautifulSoup(source, 'lxml'))
        i += 1
    return soup


def create_database():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS noticias')
    cursor.execute('''CREATE TABLE noticias(
                    categoria TEXT,
                    titulo TEXT,
                    enlace TEXT,
                    descripcion TEXT,
                    fecha TEXT)''')
    conn.commit()
    return conn


def connect():
    conn = sqlite3.connect(database)
    return conn


def disconnect(conn):
    conn.close()
