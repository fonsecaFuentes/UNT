import os
from tkinter import messagebox
from peewee import SqliteDatabase
from peewee import Model
from peewee import CharField
from peewee import IntegerField
from peewee import FloatField
from validation import FieldValidation
from error_handling import ErrorHandling


class DataBaseManager:
    def __init__(self):
        self.directory_path = os.path.dirname(__file__)
        self.db_path = os.path.join(
            self.directory_path, "database", "GameDataBase.db"
        )
        self.database_dir = os.path.dirname(self.db_path)

        if not os.path.exists(self.database_dir):
            os.makedirs(self.database_dir)

        try:
            self.db = SqliteDatabase(self.db_path)
        except Exception as e:
            error_handler = ErrorHandling()
            error_handler.handle_exception(e)

    def connect(self):
        self.db.connect()

    def create_table(self, tables):
        self.db.create_tables(tables)


class Games(Model):
    id = IntegerField(primary_key=True)
    title = CharField()
    gender = CharField()
    developer = CharField()
    price = FloatField()

    class Meta:
        database = DataBaseManager().db


class DataManagement():
    def __init__(self):
        self.validation = FieldValidation()

    def alta_item(
        self, title_entry, gender_entry,
        developer_entry, price_entry, forms
    ):
        fiels_validation = self.validation.validate_fields
        validation_price = self.validation.validate_price

        title = title_entry.get()
        gender = gender_entry.get()
        developer = developer_entry.get()
        price = price_entry.get()

        # Validar campos
        if fiels_validation(
            title,
            gender,
            developer,
            price,
        ):
            # Validar precio
            if validation_price(price):
                # Guardar datos
                try:
                    game = Games()
                    game.title = title
                    game.gender = gender
                    game.developer = developer
                    game.price = float(price)
                    game.save()
                    self.actualizar_tree(forms)
                    messagebox.showinfo(
                        "Aviso", "Juego agregado exitosamente."
                    )
                except Exception as e:
                    error_handler = ErrorHandling()
                    error_handler.handle_exception(e)
                except FileNotFoundError:
                    ErrorHandling.handle_file_not_found()
                except ValueError:
                    ErrorHandling.handle_value_error()
            else:
                messagebox.showwarning(
                    "Validación", "El valor en el imputs 'precio' no es válido"
                )
        else:
            messagebox.showwarning("Validación", "Tienes campos sin completar")

    def del_item(self, forms):
        value = list(forms.selection())

        if value:
            confirmar = messagebox.askyesno(
                "Confirmación",
                "¿Estás seguro de que deseas borrar los datos seleccionados?",
            )
            if confirmar:
                try:
                    for element in value:
                        item = forms.item(element)
                        delete = Games.get(Games.id == item["text"])
                        delete.delete_instance()

                except Exception as e:
                    error_handler = ErrorHandling()
                    error_handler.handle_exception(e)
                except FileNotFoundError:
                    ErrorHandling.handle_file_not_found()
                except ValueError:
                    ErrorHandling.handle_value_error()

            self.actualizar_tree(forms)
            messagebox.showinfo("Aviso", "datos borrados exitosamente.")

    def modify_item(
        self, title_entry, gender_entry,
        developer_entry, price_entry, forms
    ):
        fiels_validation = self.validation.validate_fields
        validation_price = self.validation.validate_price

        title = title_entry.get()
        gender = gender_entry.get()
        developer = developer_entry.get()
        price = price_entry.get()

        value = forms.selection()
        if value:
            item = forms.item(value)
            if fiels_validation(
                title,
                gender,
                developer,
                price,
            ):
                if validation_price(price):
                    # Modificar tabla Games
                    try:
                        modify_game = Games.update(
                            title=title,
                            gender=gender,
                            developer=developer,
                            price=float(price)
                        ).where(Games.id == item["text"])
                        modify_game.execute()

                    except Exception as e:
                        error_handler = ErrorHandling()
                        error_handler.handle_exception(e)
                    except FileNotFoundError:
                        ErrorHandling.handle_file_not_found()
                    except ValueError:
                        ErrorHandling.handle_value_error()

                    self.actualizar_tree(forms)
                    messagebox.showinfo(
                        "Aviso", "Juego modificado exitosamente."
                    )
                else:
                    messagebox.showwarning(
                        "Validación",
                        "El valor en el input 'precio' no es válido"
                    )
            else:
                messagebox.showwarning(
                    "Validación", "Tienes campos sin completar"
                )

    def get_item(self):
        items = Games.select()

        return items

    def actualizar_tree(self, mitreview):
        records = mitreview.get_children()
        for element in records:
            mitreview.delete(element)
        result = self.get_item()
        for row in result:
            mitreview.insert(
                "", "end",
                text=row.id,
                values=(
                    row.title, row.gender, row.developer, row.price
                )
            )

    def search_item(self, var_search, mitreview):
        filter_item = (
            (Games.title ** var_search) |
            (Games.gender ** var_search) |
            (Games.developer ** var_search) |
            (Games.price ** var_search)
        )
        register = Games.select(
            Games.title,
            Games.gender,
            Games.developer,
            Games.price
            ).where(filter_item)

        records = mitreview.get_children()

        for element in records:
            mitreview.delete(element)

        for row in register:
            mitreview.insert(
                "", "end", values=(
                    row.title, row.gender, row.developer, row.price
                )
            )


class InterfaceManagement():
    def __init__(self):
        self.light = False

    def clean_fields(
        self, var_title, var_gender,
        var_developer, var_price, var_search, forms
    ):

        data_management = DataManagement()

        var_title.set("")
        var_gender.set("")
        var_developer.set("")
        var_price.set("")
        var_search.set("")
        data_management.actualizar_tree(forms)

    def tree_selected(
        self, forms, var_title, var_gender,
        var_developer, var_price
    ):
        value = forms.selection()
        if value:
            for element in value:
                item = forms.item(element)
                value = item["values"]

                var_title.set(value[0])
                var_gender.set(value[1])
                var_developer.set(value[2])
                var_price.set(value[3])
