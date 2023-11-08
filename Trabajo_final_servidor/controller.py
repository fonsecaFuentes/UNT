from views import MyApp
from tkinter import Tk
from model_orm import DataBaseManager
from model_orm import DataManagement
from model_orm import Games
from observer import Observing


# Inicializa el controlador principal.
class Controller:
    def __init__(self, root):
        # Asigna la ventana raíz
        self.root = root
        # Crea la vista principal
        self.view = MyApp(self.root)
        self.data_management = DataManagement()
        self.observer = Observing(self.data_management)


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
