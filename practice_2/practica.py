import tkinter as tk

from practice_2 import ui_options as ui


def inicia():
    root = tk.Tk()
    almacenar = tk.Button(root, text='Almacenar', command=ui.almacenar_productos)
    almacenar.grid(row=0, column=0)
    mostrar = tk.Button(root, text='Mostrar', command=mostrar_marcas)
    mostrar.grid(row=0, column=1)
    root.mainloop()


def mostrar_marcas():
    window1 = tk.Tk()
    spin = tk.Spinbox(window1, values=ui.todas_las_marcas())
    spin.grid(row=0, column=0)
    aceptar = tk.Button(window1, text='Aceptar', command=lambda: filtrar_marcas(spin.get()))
    aceptar.grid(row=1, column=0)
    window1.mainloop()


def filtrar_marcas(marca):
    window1 = tk.Tk()
    scroll = tk.Scrollbar(window1)
    scroll.pack(side='right', fill='y')
    lb = tk.Listbox(window1, yscrollcommand=scroll.set)

    for id, i in enumerate(ui.busqueda_marcas(marca)):
        lb.insert(id, i)
        lb.pack(fill='both', expand=True)

    window1.mainloop()
