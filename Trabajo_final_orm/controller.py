import views
from tkinter import Tk
from model_orm import DataBaseManager
from model_orm import Games


class Controller:
    def __init__(self, root):
        self.root = root
        self.view = views.MyApp(self.root)


if __name__ == '__main__':
    master = Tk()

    db = DataBaseManager()
    db.connect()
    db.create_table([Games])

    app = Controller(master)
    master.mainloop()
