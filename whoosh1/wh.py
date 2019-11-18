import os
from datetime import datetime
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT, DATETIME, ID
from whoosh.qparser import QueryParser, MultifieldParser
from whoosh import qparser


# Crea un indice desde los documentos contenidos en dirdocs
# El indice lo crea en un directorio (dirindex)
def crea_index(dirdocs, dirindex):
    if not os.path.exists(dirdocs):
        print("Error: no existe el directorio de documentos " + dirdocs)
    else:
        if not os.path.exists(dirindex):
            os.mkdir(dirindex)

    ix = create_in(dirindex, schema=get_schema())
    writer = ix.writer()
    for docname in os.listdir(dirdocs):
        if not os.path.isdir(dirdocs + docname):
            add_doc(writer, dirdocs, docname)
    writer.commit()


def get_schema():
    return Schema(categoria=TEXT(stored=True), titulo=TEXT(stored=True), enlace=TEXT(stored=True),
                  descripcion=TEXT(stored=True), fecha=TEXT(stored=True), nombrefichero=ID(stored=True))


def add_doc(writer, path, docname):
    try:
        fileobj = open(path + '\\' + docname, "r")
        cat = fileobj.readline().strip()
        tit = fileobj.readline().strip()
        enl = fileobj.readline().strip()
        des = fileobj.readline().strip()
        # f = fileobj.readline().strip()
        # fec = datetime.strptime(f, '%d%m%Y')
        fec = fileobj.readline().strip()
        fileobj.close()

        writer.add_document(categoria=cat, titulo=tit, enlace=enl, descripcion=des,
                            fecha=fec, nombrefichero=docname)

        print("Creado indice para fichero " + docname)
    except:
        print("Error: No se ha podido añadir el documento " + path + '\\' + docname)
