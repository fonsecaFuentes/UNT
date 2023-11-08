class Subject:

    observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, message, title, gender, developer, price):
        for observer in self.observers:
            observer.update(message, title, gender, developer, price)


class Observer:
    def update(self):
        raise NotImplementedError("Delegación de actualización")


class Observing(Observer):
    def __init__(self, obj):
        self.observing_a = obj
        self.observing_a.add_observer(self)

    def update(self, message, title, gender, developer, price):
        format_message = (
            f"{message}\nTítulo: {title}\n"
            f"Género: {gender}\nDesarrollador: {developer}\nPrecio: {price}"
        )
        print("-"*25)
        print("Actualización dentro de Observing")
        print("-"*25)
        print(format_message)
        print("-"*25)
