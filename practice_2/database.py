import sqlite3
import requests
from bs4 import BeautifulSoup

database = 'database.db'


def get_soup():
    source = requests.get('https://www.ulabox.com/campaign/productos-sin-gluten#gref').text
    soup = BeautifulSoup(source, 'lxml')
    return soup


def create_database():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS productos')
    cursor.execute('''CREATE TABLE productos(
                    marca TEXT,
                    nombre TEXT,
                    link TEXT,
                    precio_normal TEXT,
                    precio_oferta TEXT,
                    precio_kilo TEXT)''')
    conn.commit()
    return conn


def connect():
    conn = sqlite3.connect(database)
    return conn


def desconnect(conn):
    conn.close()
