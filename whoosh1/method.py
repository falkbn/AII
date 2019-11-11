from whoosh1 import database as db
from tkinter import messagebox


def almacenar_noticias():
    try:
        conn = db.create_database()
        cursor = conn.cursor()

        for datablock in db.get_soup(3):
            datablock = datablock.find_all('div', class_='news-card')
            for data in datablock:
                categoria = data.find('div', class_="meta-category").text.split('-')[1].strip()
                print(categoria)
                titulo = data.find('a', class_='meta-title-link').text
                print(titulo)
                enlace = data.find('a', class_='meta-title-link')['href']
                print(enlace)
                try:
                    descripcion = data.find('div', class_='meta-body').text
                except:
                    descripcion = None
                print(descripcion)
                fecha = data.find('div', class_='meta-date').text
                print(fecha)
                print()

                cursor.execute('INSERT INTO noticias VALUES(?,?,?,?,?)',
                               (categoria, titulo, enlace, descripcion, fecha))
                conn.commit()

        noticias = str(cursor.execute('SELECT COUNT(*) FROM noticias').fetchone()[0])
        var = 'Base de datos creada correctamente con ' + noticias + ' entradas'
        db.disconnect(conn)

    except ValueError as e:
        var = 'Error al crear la base de datos'
        print(e)

    messagebox.showinfo('Base de datos', var)


almacenar_noticias()
