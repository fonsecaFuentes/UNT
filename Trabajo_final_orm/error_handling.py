import os
import datetime
from tkinter import messagebox


class ErrorHandling(Exception):

    directory_path = os.path.dirname(__file__)
    txt_path = os.path.join(
        directory_path, "error_txt", "log.txt"
    )
    file_dir = os.path.dirname(txt_path)

    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    def show_error(self, message):
        messagebox.showerror("Error", message)

    def register_error(self, message):
        with open(self.txt_path, "a") as log:
            timestamp = datetime.datetime.now().strftime("%d - %m - %Y  %H:%M")
            log.write(f"Se ha dado un error: {message} ({timestamp})\n")

    def handle_file_not_found(self):
        message = "Archivo de base de datos no encontrado."
        self.show_error(message)
        self.register_error("FileNotFoundError: " + message)

    def handle_value_error(self):
        message = "Error al convertir el precio a número."
        self.show_error(message)
        self.register_error("ValueError: " + message)

    def handle_exception(self, e):
        message = "Error desconocido:\n" + str(e)
        self.show_error(message)
        self.register_error("Exception: " + message)
