from whoosh1 import database as db
from tkinter import messagebox
from whoosh1 import wh
from datetime import datetime


def almacenar_noticias():
    try:
        conn = db.create_database()
        cursor = conn.cursor()

        for page, datablock in enumerate(db.get_soup(3), start=1):
            datablock = datablock.find_all('div', class_='news-card')
            for notice, data in enumerate(datablock, start=1):
                file = open('Docs/p-' + str(page) + '-n' + str(notice) + '.txt', 'w')
                categoria = data.find('div', class_="meta-category").text.split('-')[1].strip()
                file.write(categoria + '\n')
                titulo = data.find('a', class_='meta-title-link').text
                file.write(titulo + '\n')
                enlace = data.find('a', class_='meta-title-link')['href']
                file.write(enlace + '\n')
                try:
                    descripcion = data.find('div', class_='meta-body').text
                except:
                    descripcion = "N/A"
                file.write(descripcion + '\n')
                fecha = data.find('div', class_='meta-date').text
                datecode = enlace.split('-')[1].split('/')[0]
                datecode = str(datetime.fromtimestamp(int(datecode)))
                file.write(datecode + '\n' + '\n')
                file.close()

                cursor.execute('INSERT INTO noticias VALUES(?,?,?,?,?)',
                               (categoria, titulo, enlace, descripcion, fecha))
                conn.commit()

        noticias = str(cursor.execute('SELECT COUNT(*) FROM noticias').fetchone()[0])
        var = 'Base de datos creada correctamente con ' + noticias + ' entradas'
        db.disconnect(conn)

        wh.crea_index('Docs', 'Index')

    except ValueError as e:
        var = 'Error al crear la base de datos'
        print(e)

    messagebox.showinfo('Base de datos', var)
