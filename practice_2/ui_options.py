from practice_2 import database as db
from bs4 import BeautifulSoup
import tkinter as tk


def almacenar_productos():
    conn = db.create_database()
    cursor = conn.cursor()

    datablock = db.get_soup().find_all('div', class_='js-product-grid-grid')
    for data in datablock:
        marca = data.find('h4', class_="product-item__brand").text.strip()
        print(marca)
        nombre = data.find('img', class_='lazy')['alt']
        print(nombre)
        link = data.find('a', class_='js-article-link')['href']
        print('https://www.ulabox.com' + link)
        try:
            precio_normal = data.find('del', class_='product-item__price--old').text
        except:
            precio_normal = data.find('strong', class_='product-item__price').text
        print(precio_normal)
        try:
            precio_oferta = data.find('strong', class_='product-grid-footer__price--new').text
        except:
            precio_oferta = '-'
        print(precio_oferta)
        precio_kilo = data.find('small', class_='product-item__ppu nano').text.split('|')[1].strip()
        print(precio_kilo)
        print()

        cursor.execute('INSERT INTO productos VALUES(?,?,?,?,?,?)',(marca, nombre, link, precio_normal, precio_oferta, precio_kilo))
