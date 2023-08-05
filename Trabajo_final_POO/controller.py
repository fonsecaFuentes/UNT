from tkinter import Tk
from app_views import MyApp
from app_models import CreatingDatabaseTables


class Controller:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.db.create_table()
        self.view = MyApp(self.root)


if __name__ == '__main__':
    data_base = CreatingDatabaseTables()

    master = Tk()
    app_views = Controller(master, data_base)
    master.mainloop()
