from practice_2 import database as db
from tkinter import messagebox


def almacenar_productos():
    try:
        var = 'Base de datos creada correctamente'
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

            cursor.execute('INSERT INTO productos VALUES(?,?,?,?,?,?)',
                           (marca, nombre, link, precio_normal, precio_oferta, precio_kilo))
            conn.commit()

        db.desconnect(conn)

    except ValueError as e:
        var = 'Error al crear la base de datos'
        print(e)

    messagebox.showinfo('Base de datos', var)


def todas_las_marcas():
    conn = db.connect()
    cursor = conn.cursor()

    cursor.execute('''SELECT marca FROM productos''')
    marcas = cursor.fetchall()
    marcas = sorted(set(map(lambda x: x[0], marcas)))
    print(marcas)

    db.desconnect(conn)
    return marcas


def buscar_ofertas():
    conn = db.connect()
    cursor = conn.cursor()

    cursor.execute('SELECT nombre FROM productos WHERE precio_oferta != "-"')
    ofertas = cursor.fetchall()
    ofertas = sorted(set(ofertas))
    print(ofertas)

    db.desconnect(conn)
    return [x[0] for x in ofertas]


def busqueda_marcas(marca):
    conn = db.connect()
    cursor = conn.cursor()

    cursor.execute('SELECT nombre, precio_normal, precio_oferta FROM productos WHERE marca == ?', (marca,))
    nombres = cursor.fetchall()
    nombres = sorted(set(nombres))
    print(nombres[0])

    db.desconnect(conn)
    return [x[0] for x in nombres]

