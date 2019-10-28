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
    search_menu.add_command(label="Autor", command=buscar_autor)
    search_menu.add_command(label="Fecha", command=buscar_fecha)
    menubar.add_cascade(label="Buscar", menu=search_menu)

    root.config(menu=menubar)
    root.mainloop()


def buscar_fecha():
    window1 = tk.Tk()
    label_fecha = tk.Label(window1, text='Fecha de búsqueda: ')
    label_fecha.grid(row=0, column=0)
    entry1 = tk.Entry(window1, bd=5)
    entry1.grid(row=0, column=1)
    button1 = tk.Button(window1, text='Buscar', command=lambda: filtrar_fechas(entry1.get()))
    button1.grid(row=0, column=2)
    window1.mainloop()


def filtrar_fechas(fecha):
    window1 = tk.Tk()
    scroll = tk.Scrollbar(window1)
    scroll.pack(side='right', fill='y')
    lb = tk.Listbox(window1, yscrollcommand=scroll.set)

    for id, i in enumerate(m.get_noticia_fecha(fecha)):
        lb.insert(id, i)
        lb.pack(fill='both', expand=True)

    window1.mainloop()


def buscar_autor():
    window1 = tk.Tk()
    spin = tk.Spinbox(window1, values=m.get_autores())
    spin.grid(row=0, column=0)
    aceptar = tk.Button(window1, text='Aceptar', command=lambda: filtrar_autores(spin.get()))
    aceptar.grid(row=1, column=0)
    window1.mainloop()


def filtrar_autores(autor):
    window1 = tk.Tk()
    scroll = tk.Scrollbar(window1)
    scroll.pack(side='right', fill='y')
    lb = tk.Listbox(window1, yscrollcommand=scroll.set)

    for id, i in enumerate(m.get_noticia_autor(autor)):
        lb.insert(id, i)
        lb.pack(fill='both', expand=True)

    window1.mainloop()


def datos_mostrar():
    window1 = tk.Tk()
    scroll = tk.Scrollbar(window1)
    scroll.pack(side='right', fill='y')
    lb = tk.Listbox(window1, yscrollcommand=scroll.set)

    for id, i in enumerate(m.datos_mostrar()):
        lb.insert(id, i)
        lb.pack(fill='both', expand=True)

    window1.mainloop()
