import os
import datetime
from message_handling import MenssageHandler


# Manejo de errores
class ErrorHandling(Exception):
    def __init__(self):
        self.messages = MenssageHandler.message_error

    # Rutas para el archivo de registro de errores
    directory_path = os.path.dirname(__file__)
    txt_path = os.path.join(
        directory_path, "error_txt", "log.txt"
    )
    file_dir = os.path.dirname(txt_path)

    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    # Registrar el error
    def register_error(self, message):
        with open(self.txt_path, "a") as log:
            timestamp = datetime.datetime.now().strftime("%d - %m - %Y  %H:%M")
            log.write(f"Se ha dado un error: {message} ({timestamp})\n")

    # Maneja la excepción de "FileNotFoundError".
    def handle_file_not_found(self):
        message = "Archivo de base de datos no encontrado."
        self.messages(self, message)
        self.register_error("FileNotFoundError: " + message)

    # Maneja la excepción de "ValueError".
    def handle_value_error(self):
        message = "Error al convertir el precio a número."
        self.messages(self, message)
        self.register_error("ValueError: " + message)

    # Maneja la excepción desconocida
    def handle_exception(self, e):
        message = "Error desconocido:\n" + str(e)
        self.messages(self, message)
        self.register_error("Exception: " + message)
