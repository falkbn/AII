from whoosh1 import method as m
import tkinter as tk


def inicia():
    root = tk.Tk()
    menubar = tk.Menu(root)
    data_menu = tk.Menu(menubar, tearoff=0)
    data_menu.add_command(label="Cargar", command=m.almacenar_noticias)
    data_menu.add_separator()
    data_menu.add_command(label="Salir", command=root.quit)
    menubar.add_cascade(label="Datos", menu=data_menu)

    search_menu = tk.Menu(menubar, tearoff=0)
    search_menu.add_command(label="Titulo y Descripcion", command=None)
    search_menu.add_command(label="Fecha", command=None)
    search_menu.add_command(label="Descripcion", command=None)
    menubar.add_cascade(label="Buscar", menu=search_menu)

    root.config(menu=menubar)
    root.mainloop()
