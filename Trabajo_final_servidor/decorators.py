import os
import datetime
# Importamos la clase ErrorHandling desde el módulo error_handling
from error_handling import ErrorHandling


def register_decorator(message):
    # Rutas para el archivo de registro de decoradores
    directory_path = os.path.dirname(__file__)
    txt_path = os.path.join(
        directory_path, "decorator_txt", "log.txt"
    )
    file_dir = os.path.dirname(txt_path)

    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    with open(txt_path, "a") as log:
        timestamp = datetime.datetime.now().strftime("%d - %m - %Y  %H:%M")
        log.write(f"{message}\nAccion realizada: ({timestamp})\n")


# Decorador para registrar la entrada de nuevos registros
def registry_decorator(function):
    def inner(self, *args):
        # Llamamos a la función original
        function(self, *args)
        format_message = (
            "-"*25,
            "Elementos guardados:\n" +
            "Titulo:" + " " + args[0].get() + "\n" +
            "Genero:" + " " + args[1].get() + "\n" +
            "Desarrollador:" + " " + args[2].get() + "\n" +
            "Precio:" + args[3].get() + "\n" +
            "-"*25
        )
        message = "\n".join(format_message)
        register_decorator(message)
    return inner


# Decorador para registrar la eliminación de elementos
def del_decorator(function):
    def inner(self, *args):
        """Importamos la clase Games desde el módulo model_orm
            localmente para evitar un problema de importación circular"""
        from model_orm import Games
        value = list(args[0].selection())
        deleted_data = []
        for element in value:
            item = args[0].item(element)
            game = Games.get(Games.id == item["text"])
            if game:
                data = (
                    "Titulo:" + " " + str(game.title),
                    "Genero:" + " " + str(game.gender),
                    "Desarrollador:" + " " + str(game.developer),
                    "Precio:" + " " + str(game.price)
                )
                deleted_data.append("\n".join(data))
        format_message = (
            "-" * 25,
            "Elementos eliminados:\n" + "\n".join(deleted_data),
            "-" * 25
        )
        message = "\n".join(format_message)
        # Llamamos a la función original
        function(self, *args)
        register_decorator(message)
    return inner


# Decorador para registrar la modificación de elementos
def update_decrorator(function):
    def inner(self, *args):
        """Importamos la clase Games desde el módulo model_orm
            localmente para evitar un problema de importación circular"""
        from model_orm import Games
        value = list(args[4].selection())
        for element in value:
            item = args[4].item(element)
            game_id = item["text"]
            game = Games.get(Games.id == game_id)
            # Verificar si el juego existe y almacenar sus valores originales
            if game:
                original_title = game.title
                original_gender = game.gender
                original_developer = game.developer
                original_price = game.price

        # Llamamos a la función original
        function(self, *args)

        try:
            # Comprobar si los campos han cambiado y mostrar los cambios
            if args[0].get() != original_title:
                format_message = (
                    "-"*25,
                    "Elementos modificados:\n" +
                    "Titulo:" + " " + args[0].get() + "\n" +
                    "-"*25
                )
                message = "\n".join(format_message)
                register_decorator(message)

            if args[1].get() != original_gender:
                format_message = (
                    "-"*25,
                    "Elementos modificados:\n" +
                    "Genero:" + " " + args[1].get() + "\n" +
                    "-"*25
                )
                message = "\n".join(format_message)
                register_decorator(message)

            if args[2].get() != original_developer:
                format_message = (
                    "-"*25,
                    "Elementos modificados:\n" +
                    "Desarrollador:" + " " + args[2].get() + "\n" +
                    "-"*25
                )
                message = "\n".join(format_message)
                register_decorator(message)

            if float(args[3].get()) != original_price:
                format_message = (
                    "-"*25,
                    "Elementos modificados:\n" +
                    "Precio:" + " " + args[3].get() + "\n" +
                    "-"*25
                )
                message = "\n".join(format_message)
                register_decorator(message)

        # Manejo de errores en caso de que ocurra una excepción
        # UnboundLocalError
        except UnboundLocalError:
            error_handler = ErrorHandling()
            error_handler.unbound_local_error()
    return inner
