from model_orm import Users
from message_handling import MenssageHandler
from validation import FieldValidation
from error_handling import ErrorHandling


class DataUsers():
    def __init__(self):
        self.messages = MenssageHandler()
        self.validation = FieldValidation()
        self.user = None
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update_user(self.user)

    def register_user(self, name_entry, forms):
        message = self.messages
        fiels_validation = self.validation.validate_fields

        name = name_entry.get()

        if fiels_validation(name, name, name, name):
            try:
                users = Users()
                users.name = name
                users.save()
                self.actualizar_tree(forms)

                info = "Usuario registrado."
                message.message_info(info)

                return True

            except Exception as e:
                error_handler = ErrorHandling()
                error_handler.handle_exception(e)
        else:
            warning = "Completa el campo Usuario"
            message.message_warning(warning)

    def get_users(self):
        user = Users.select()

        return user

    def actualizar_tree(self, forms):
        records = forms.get_children()
        for element in records:
            forms.delete(element)
        result = self.get_users()
        for row in result:
            forms.insert(
                "", "end",
                text=row.id,
                values=(row.name)
            )

    def tree_selected(self, forms, var_name):
        value = forms.selection()
        if value:
            for element in value:
                item = forms.item(element)
                value = item["values"]
                print(item["values"])
                self.user = value[0]
                self.notify_observers()
        print(self.user)
