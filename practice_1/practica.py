# Author: Antonio

import tkinter as tk


class Practica1:
    def inicia(self):
        self.root = tk.Tk()
        menubar = tk.Menu(self.root)
        data_menu = tk.Menu(menubar, tearoff=0)
        data_menu.add_command(label="Cargar", command=self.cargar)
        data_menu.add_command(label="Mostrar", command=self.mostrar)
        data_menu.add_command(label="Salir", command=self.salir)
        menubar.add_cascade(label="Datos", menu=data_menu)

        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Tema", command=self.tema)
        edit_menu.add_command(label="Fecha", command=self.fecha)
        menubar.add_cascade(label="Buscar", menu=edit_menu)

        stats_menu = tk.Menu(menubar, tearoff=0)
        stats_menu.add_command(label="Temas más populares", command=self.temas_populares)
        stats_menu.add_command(label="Temas más activos", command=self.temas_activos)
        menubar.add_cascade(label="Estadísticas", menu=stats_menu)

        self.root.config(menu=menubar)
        self.root.mainloop()

    def cargar(self):
        print("Cargando")

    def mostrar(self):
        print("Mostrando")

    def salir(self):
        print("Saliendo")

    def tema(self):
        print("Tema")

    def fecha(self):
        print("Fecha")

    def buscar(self):
        print("Buscando")

    def temas_populares(self):
        print("Temas populares")

    def temas_activos(self):
        print("Temas activos")
