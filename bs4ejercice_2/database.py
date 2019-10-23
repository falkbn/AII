import requests
import sqlite3
from bs4 import BeautifulSoup

database = 'database.sqlite'


def get_soup():
    source = requests.get('https://www.meneame.net/').text
    soup = BeautifulSoup(source, 'lxml')
    return soup


def create_database():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS noticias')
    cursor.execute('''CREATE TABLE noticias(
                    titulo TEXT,
                    enlace TEXT,
                    autor TEXT,
                    fecha TEXT,
                    contenido TEXT)''')
    conn.commit()
    return conn


def connect():
    conn = sqlite3.connect(database)
    return conn


def disconnect(conn):
    conn.close()
