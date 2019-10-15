import ctypes
import practica
import ui_options

if __name__ == "__main__":
    # Para prevenir que se vea borroso (solo windows)
    ctypes.windll.shcore.SetProcessDpiAwareness(
        1)  

    p = practica.Practica1()
    p.cargar = ui_options.cargar
    p.mostrar = ui_options.mostrar
    p.salir = lambda: p.root.destroy()
    p.tema = ui_options.buscar_tema
    p.fecha = ui_options.buscar_fecha
    p.temas_populares = ui_options.temas_populares
    p.temas_activos = ui_options.temas_activos
    p.inicia()
