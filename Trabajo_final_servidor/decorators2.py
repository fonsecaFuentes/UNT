from error_handling import ErrorHandling
import os
import datetime


class Decorators:
    def __init__(self):
        self.error_handler = ErrorHandling()

    # Rutas para el archivo de registro de decoradores
    directory_path = os.path.dirname(__file__)
    txt_path = os.path.join(
        directory_path, "decorator_txt", "log.txt"
    )
    file_dir = os.path.dirname(txt_path)

    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    # Registrar el decorador
    def register_decorator(self, message):
        with open(self.txt_path, "a") as log:
            timestamp = datetime.datetime.now().strftime("%d - %m - %Y  %H:%M")
            log.write(f"Se ha dado un error: {message} ({timestamp})\n")