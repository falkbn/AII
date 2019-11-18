from whoosh1 import method as m
import tkinter as tk
from whoosh.index import open_dir
from whoosh.qparser import MultifieldParser


def inicia():
    root = tk.Tk()
    menubar = tk.Menu(root)
    data_menu = tk.Menu(menubar, tearoff=0)
    data_menu.add_command(label="Cargar", command=m.almacenar_noticias)
    data_menu.add_separator()
    data_menu.add_command(label="Salir", command=root.quit)
    menubar.add_cascade(label="Datos", menu=data_menu)

    search_menu = tk.Menu(menubar, tearoff=0)
    search_menu.add_command(label="Titulo y Descripcion", command=entry_b_1)
    search_menu.add_command(label="Fecha", command=None)
    search_menu.add_command(label="Descripcion", command=None)
    menubar.add_cascade(label="Buscar", menu=search_menu)

    root.config(menu=menubar)
    root.mainloop()


def entry_b_1():
    window1 = tk.Tk()
    label = tk.Label(window1, text='Termino de busqueda: ')
    label.grid(row=0, column=0)
    entry1 = tk.Entry(window1, bd=5)
    entry1.grid(row=0, column=1)
    button1 = tk.Button(window1, text='Buscar', command=lambda: listbox_b_1(entry1.get()))
    button1.grid(row=0, column=2)
    window1.mainloop()


def listbox_b_1(entry):
    window1 = tk.Tk()
    scroll = tk.Scrollbar(window1)
    scroll.pack(side='right', fill='y')
    lb = tk.Listbox(window1, yscrollcommand=scroll.set)
    ix = open_dir('Index')
    with ix.searcher() as searcher:
        query = MultifieldParser(["titulo", "descripcion"], ix.schema).parse(entry)
        restrict_query = query.
        results = searcher.search(query, limit=None, mask=restrict_query)
        for r in results:
            lb.insert(tk.END, r['categoria'])
            lb.insert(tk.END, r['titulo'])
            lb.insert(tk.END, r['fecha'])
            lb.insert(tk.END, '')
    lb.pack(side=tk.BOTTOM, fill=tk.BOTH)
    scroll.config(command=lb.yview)

    window1.mainloop()
