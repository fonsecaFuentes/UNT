import sqlite3
import re
import os
from tkinter import messagebox


class CreatingDatabaseTables():
    def __init__(self):
        self.directory_path = os.path.dirname(__file__)
        self.new_db_path = os.path.join(
            self.directory_path, "database", "GameDataBase.db"
        )
        self.file_db = self.new_db_path
        database_dir = os.path.dirname(self.file_db)
        if not os.path.exists(database_dir):
            os.makedirs(database_dir)
        self.connect = self.connection()

    def connection(self):
        connect = sqlite3.connect(self.file_db)
        return connect

    def create_table(self):
        connect = self.connect
        cursor = connect.cursor()
        sql = "CREATE TABLE IF NOT EXISTS data_game (id INTEGER PRIMARY KEY,\
            titulo VARCHAR(255), estilo VARCHAR(255), desarrollador\
            VARCHAR(255), precio INTEGER (5))"
        cursor.execute(sql)
        connect.commit()


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
    def __init__(self):
        self.connect_db = CreatingDatabaseTables()
        self.validation = FieldValidation()

    def alta_item(self, titulo, estilo, desarrollador, precio, forms):
        connect = self.connect_db.connection()
        fiels_validation = self.validation.validate_fields
        validation_price = self.validation.validate_price

        titulo = titulo.get()
        estilo = estilo.get()
        desarrollador = desarrollador.get()
        precio = precio.get()
        if fiels_validation(
            titulo, estilo, desarrollador, precio
        ):
            if validation_price(precio):
                data = (titulo, estilo, desarrollador, float(precio))

                cursor = connect.cursor()
                sql = "INSERT INTO data_game (titulo, estilo, desarrollador,\
                    precio) VALUES (?, ?, ?, ?)"
                cursor.execute(sql, data)
                connect.commit()
                self.actualizar_tree(forms)
                messagebox.showinfo("Aviso", "Juego agregado exitosamente.")
            else:
                messagebox.showwarning(
                    "Validación", "El valor en el imputs 'precio' no es válido"
                )
        else:
            messagebox.showwarning("Validación", "Tienes campos sin completar")

    def del_item(self, forms):
        connect = self.connect_db.connection()

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
                    cursor = connect.cursor()
                    data = (mi_id,)
                    sql = "DELETE FROM data_game WHERE id = ?"
                    cursor.execute(sql, data)
                    connect.commit()
                    forms.delete(element)
            messagebox.showinfo("Aviso", "datos borrados exitosamente.")

    def modify_item(self, titulo, estilo, desarrollador, precio, forms):
        connect = self.connect_db.connection()
        fiels_validation = self.validation.validate_fields
        validation_price = self.validation.validate_price

        titulo = titulo.get()
        estilo = estilo.get()
        desarrollador = desarrollador.get()
        precio = precio.get()
        valor = forms.selection()
        if valor:
            item = forms.item(valor)
            mi_id = item['text']
            if fiels_validation(
                titulo, estilo, desarrollador, precio
            ):
                if validation_price(precio):
                    data = (
                        titulo, estilo, desarrollador, float(precio), mi_id
                    )
                    cursor = connect.cursor()
                    slq = "UPDATE data_game SET titulo=?, estilo=?,\
                            desarrollador=?, precio=? WHERE id=?"
                    cursor.execute(slq, data)
                    connect.commit()
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
        connect = self.connect_db.connection()
        cursor = connect.cursor()
        sql = "SELECT *  FROM data_game ORDER BY id ASC"
        data = cursor.execute(sql)

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
        connect = self.connect_db.connection()

        cursor = connect.cursor()
        sql = "SELECT titulo, estilo, desarrollador, precio FROM data_game\
             WHERE titulo LIKE ? OR estilo LIKE ? OR desarrollador LIKE ?"
        data = cursor.execute(
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


class InterfaceManagement():
    def __init__(self):
        self.light = False

    def clean_fields(
        self, var_titulo, var_estilo, var_desarrollador,
        var_precio, var_search, forms
    ):

        data_management = DataManagement()

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
