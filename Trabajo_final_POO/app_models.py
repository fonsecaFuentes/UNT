import sqlite3
import re
from tkinter import messagebox


class CreatingDatabaseTables():
    def __init__(self):
        self.connection = None
        self.cursor = None

    def create_db(self):
        self.connection = sqlite3.connect("GameDataBase.db")
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.create_db()
        sql = "CREATE TABLE IF NOT EXISTS data_game (id INTEGER PRIMARY KEY,\
            titulo VARCHAR(255), estilo VARCHAR(255), desarrollador\
            VARCHAR(255), precio INTEGER (5))"
        self.cursor.execute(sql)
        self.connection.commit()


class FieldValidation():
    def validate_fields(self, titulo, estilo, desarrollador, precio):
        nulo = r"^(?!\s*$).+"

        if (
            re.match(nulo, titulo)
            and re.match(nulo, estilo)
            and re.match(nulo, desarrollador)
            and re.match(nulo, precio)
        ):
            return True
        else:
            return False

    def validate_price(self, precio):
        numero = r"^\d+(\.\d{1,2})?$"
        if re.match(numero, precio):
            return True
        else:
            return False


class DataManagement():

    def alta_item(self, titulo, estilo, desarrollador, precio, forms):
        #
        creating_db = CreatingDatabaseTables()
        fiels_validation = FieldValidation()
        #
        titulo = titulo.get()
        estilo = estilo.get()
        desarrollador = desarrollador.get()
        precio = precio.get()
        if fiels_validation.validate_fields(
            titulo, estilo, desarrollador, precio
        ):
            if fiels_validation.validate_price(precio):
                data = (titulo, estilo, desarrollador, float(precio))

                creating_db.create_db()
                sql = "INSERT INTO data_game (titulo, estilo, desarrollador,\
                    precio) VALUES (?, ?, ?, ?)"
                creating_db.cursor.execute(sql, data)
                creating_db.connection.commit()
                self.actualizar_tree(forms)
                messagebox.showinfo("Aviso", "Juego agregado exitosamente.")
            else:
                messagebox.showwarning(
                    "Validación", "El valor en el imputs 'precio' no es válido"
                )
        else:
            messagebox.showwarning("Validación", "Tienes campos sin completar")

    def del_item(self, forms):
        #
        creating_db = CreatingDatabaseTables()
        #
        valor = forms.selection()
        if valor:
            confirmar = messagebox.askyesno(
                "Confirmación",
                "¿Estás seguro de que deseas borrar los datos seleccionados?",
            )
            if confirmar:
                for element in valor:
                    item = forms.item(element)
                    mi_id = item["text"]
                    creating_db.create_db()
                    data = (mi_id,)
                    sql = "DELETE FROM data_game WHERE id = ?"
                    creating_db.cursor.execute(sql, data)
                    creating_db.connection.commit()
                    forms.delete(element)
            messagebox.showinfo("Aviso", "datos borrados exitosamente.")

    def modify_item(self, titulo, estilo, desarrollador, precio, forms):
        #
        creating_db = CreatingDatabaseTables()
        fiels_validation = FieldValidation()
        #
        titulo = titulo.get()
        estilo = estilo.get()
        desarrollador = desarrollador.get()
        precio = precio.get()
        valor = forms.selection()
        if valor:
            item = forms.item(valor)
            mi_id = item['text']
            if fiels_validation.validate_fields(
                titulo, estilo, desarrollador, precio
            ):
                if fiels_validation.validate_price(precio):
                    data = (
                        titulo, estilo, desarrollador, float(precio), mi_id
                    )
                    creating_db.create_db()
                    slq = "UPDATE data_game SET titulo=?, estilo=?,\
                            desarrollador=?, precio=? WHERE id=?"
                    creating_db.cursor.execute(slq, data)
                    creating_db.connection.commit()
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
        creating_db = CreatingDatabaseTables()
        creating_db.create_db()
        sql = "SELECT *  FROM data_game ORDER BY id ASC"
        data = creating_db.cursor.execute(sql)

        return data.fetchall()

    def actualizar_tree(self, mitreview):
        records = mitreview.get_children()
        for element in records:
            mitreview.delete(element)
        result = self.get_item()
        for fila in result:
            mitreview.insert(
                "", "end",
                text=fila[0],
                values=(fila[1], fila[2], fila[3], fila[4])
            )

    def search_item(self, var_search, mitreview):
        #
        creating_db = CreatingDatabaseTables()
        #
        creating_db.create_db()
        sql = "SELECT titulo, estilo, desarrollador, precio FROM data_game\
             WHERE titulo LIKE ? OR estilo LIKE ? OR desarrollador LIKE ?"
        data = creating_db.cursor.execute(
            sql, (var_search, var_search, var_search)
        )
        result = data.fetchall()
        records = mitreview.get_children()
        for element in records:
            mitreview.delete(element)
        for fila in result:
            mitreview.insert(
                "", "end", values=(fila[0], fila[1], fila[2], fila[3])
            )

    def connect(self, forms):
        #
        creating_db = CreatingDatabaseTables()
        #
        creating_db.create_db()
        self.actualizar_tree(forms)


class InterfaceManagement():
    def __init__(self):
        self.light = False

    def clean_fields(
        self, var_titulo, var_estilo, var_desarrollador,
        var_precio, var_search, forms
    ):
        #
        data_management = DataManagement()
        #
        var_titulo.set("")
        var_estilo.set("")
        var_desarrollador.set("")
        var_precio.set("")
        var_search.set("")
        data_management.actualizar_tree(forms)

    def tree_selected(
        self, forms, var_titulo, var_estilo, var_desarrollador, var_precio
    ):
        valor = forms.selection()
        if valor:
            for element in valor:
                item = forms.item(element)
                valor = item["values"]

                var_titulo.set(valor[0])
                var_estilo.set(valor[1])
                var_desarrollador.set(valor[2])
                var_precio.set(valor[3])

    def change_colors(self, elements_list):

        if self.light:
            bg_color = "#E0E0E0"
            fg_color = "#000000"
            highlight_color = "#FFFFFF"
            self.light = False
        else:
            bg_color = "#1E1E1E"
            fg_color = "#FFFFFF"
            highlight_color = "#606060"
            self.light = True

        elements_list[0].configure(background=bg_color)
        elements_list[1].configure(background=bg_color, foreground=fg_color)
        elements_list[2].configure(background=bg_color, foreground=fg_color)
        elements_list[3].configure(background=bg_color, foreground=fg_color)
        elements_list[4].configure(background=bg_color, foreground=fg_color)
        elements_list[5].configure(background=bg_color, foreground=fg_color)
        elements_list[6].configure(
            background=highlight_color, foreground=fg_color
        )
        elements_list[7].configure(
            background=highlight_color, foreground=fg_color
        )
        elements_list[8].configure(
            background=highlight_color, foreground=fg_color
        )
        elements_list[9].configure(
            background=highlight_color, foreground=fg_color
        )
        elements_list[10].configure(
            background=highlight_color, foreground=fg_color
        )
        elements_list[11].configure(
            background=highlight_color, foreground=fg_color
        )
        elements_list[12].configure(
            background=highlight_color, foreground=fg_color
        )
        elements_list[13].configure(
            background=highlight_color, foreground=fg_color
        )
        elements_list[14].configure(
            background=highlight_color, foreground=fg_color
        )
        elements_list[15].configure(
            background=highlight_color, foreground=fg_color
        )
        elements_list[16].configure(
            background=highlight_color, foreground=fg_color
        )
