import views
from tkinter import Tk
from model_orm import DataBaseManager
from model_orm import Games


# Inicializa el controlador principal.
class Controller:
    def __init__(self, root):
        # Asigna la ventana raíz
        self.root = root
        # Crea la vista principal
        self.view = views.MyApp(self.root)


if __name__ == '__main__':
    # Crea la ventana principal
    master = Tk()

    # Administra la base de datos
    db = DataBaseManager()
    # Conecta a la base de datos
    db.connect()
    # Crea la tabla de juegos
    db.create_table([Games])

    # Inicializa la aplicación
    app = Controller(master)
    master.mainloop()
