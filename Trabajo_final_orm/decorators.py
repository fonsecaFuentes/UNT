# Importamos la clase ErrorHandling desde el módulo error_handling
from error_handling import ErrorHandling


# Decorador para registrar la entrada de nuevos registros
def registry_decorator(function):
    def inner(self, *args):
        # Llamamos a la función original
        function(self, *args)
        print("Ingreso de nuevo registro")
        print("-"*25)
        print("Elementos guardados:")
        # Imprimimos los valores de los elementos
        print("Título:", args[0].get())
        print("Género:", args[1].get())
        print("Desarrollador:", args[2].get())
        print("Precio:", args[3].get())
        print("-"*25)
    return inner


# Decorador para registrar la eliminación de elementos
def del_decorator(function):
    def inner(self, *args):
        """Importamos la clase Games desde el módulo model_orm
            localmente para evitar un problema de importación circular"""
        from model_orm import Games
        value = list(args[0].selection())
        print(value)
        print("Se ha eliminado un elemento")
        print("-"*25)
        print("Elementos eliminados:")
        for element in value:
            item = args[0].item(element)
            game = Games.get(Games.id == item["text"])
            if game:
                # Imprimimos los detalles del juego eliminado
                print("Título:", game.title)
                print("Género:", game.gender)
                print("Desarrollador:", game.developer)
                print("Precio:", game.price)
        print("-"*25)
        # Llamamos a la función original
        function(self, *args)
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
            print("Modificación de un elemento")
            print("-"*25)
            print("Elementos modificados:")
            # Comprobar si los campos han cambiado y mostrar los cambios
            if args[0].get() != original_title:
                print("Título:", args[0].get())
            if args[1].get() != original_gender:
                print("Género:", args[1].get())
            if args[2].get() != original_developer:
                print("Desarrollador:", args[2].get())
            if float(args[3].get()) != original_price:
                print("Precio:", args[3].get())
            print("-"*25)
        # Manejo de errores en caso de que ocurra una excepción
        # UnboundLocalError
        except UnboundLocalError:
            error_handler = ErrorHandling()
            error_handler.unbound_local_error()
    return inner
