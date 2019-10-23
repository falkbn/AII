from bs4ejercice_2 import method as m
import tkinter as tk


def inicia():
    root = tk.Tk()
    menubar = tk.Menu(root)
    data_menu = tk.Menu(menubar, tearoff=0)
    data_menu.add_command(label="Cargar", command=m.datos_cargar)
    data_menu.add_command(label="Mostrar", command=datos_mostrar)
    data_menu.add_separator()
    data_menu.add_command(label="Salir", command=root.quit)
    menubar.add_cascade(label="Datos", menu=data_menu)

    search_menu = tk.Menu(menubar, tearoff=0)
    search_menu.add_command(label="Autor", command=None)
    search_menu.add_command(label="Fecha", command=None)
    menubar.add_cascade(label="Buscar", menu=search_menu)

    root.config(menu=menubar)
    root.mainloop()


def datos_mostrar():
    window1 = tk.Tk()
    scroll = tk.Scrollbar(window1)
    scroll.pack(side='right', fill='y')
    lb = tk.Listbox(window1, yscrollcommand=scroll.set)

    for id, i in enumerate(m.datos_mostrar()):
        lb.insert(id, i)
        lb.pack(fill='both', expand=True)

    window1.mainloop()
