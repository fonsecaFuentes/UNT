from tkinter import Tk
import app_views
import app_models


if __name__ == '__main__':
    master = Tk()
    app_model = app_models.DataManagement()
    app_views = app_views.MyApp(master, app_model)
    master.mainloop()
