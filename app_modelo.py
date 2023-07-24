import sqlite3
import re
from tkinter import messagebox

# variable para la funcion change_colors
light = True


def create_db():
    conection = sqlite3.connect("database.db")
    return conection


def create_table():
    conection = create_db()
    cursor = conection.cursor()
    slq = "CREATE TABLE IF NOT EXISTS data_game (id INTEGER PRIMARY KEY,\
            titulo VARCHAR(255), estilo VARCHAR(255), desarrollador\
            VARCHAR(255), precio INTEGER (5))"
    cursor.execute(slq)
    conection.commit()


def validate_fields(titulo, estilo, desarrollador, precio):
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


def validate_price(precio):
    numero = r"^\d+(\.\d{1,2})?$"
    if re.match(numero, precio):
        return True
    else:
        return False


def alta_item(titulo, estilo, desarrollador, precio, forms):
    if validate_fields(titulo, estilo, desarrollador, precio):
        if validate_price(precio):
            data = (titulo, estilo, desarrollador, float(precio))

            conection = create_db()
            cursor = conection.cursor()
            slq = "INSERT INTO data_game (titulo, estilo, desarrollador,\
                precio) VALUES (?, ?, ?, ?)"
            cursor.execute(slq, data)
            conection.commit()
            actualizar_tree(forms)
            messagebox.showinfo("Aviso", "Juego agregado exitosamente.")
        else:
            messagebox.showwarning(
                "Validación", "El valor en el imputs 'precio' no es válido"
            )
    else:
        messagebox.showwarning("Validación", "Tienes campos sin completar")


def del_item(forms):
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
                conection = create_db()
                cursor = conection.cursor()
                data = (mi_id,)
                sql = "DELETE FROM data_game WHERE id = ?"
                cursor.execute(sql, data)
                conection.commit()
                forms.delete(element)
        messagebox.showinfo("Aviso", "datos borrados exitosamente.")


def modify_item(titulo, estilo, desarrollador, precio, forms):
    valor = forms.selection()
    if valor:
        item = forms.item(valor)
        mi_id = item['text']
        if validate_fields(titulo, estilo, desarrollador, precio):
            if validate_price(precio):
                data = (titulo, estilo, desarrollador, float(precio), mi_id)
                conection = create_db()
                cursor = conection.cursor()
                slq = "UPDATE data_game SET titulo=?, estilo=?,\
                        desarrollador=?, precio=? WHERE id=?"
                cursor.execute(slq, data)
                conection.commit()
                actualizar_tree(forms)
                messagebox.showinfo("Aviso", "Juego modificado exitosamente.")
            else:
                messagebox.showwarning(
                    "Validación", "El valor en el input 'precio' no es válido"
                )
        else:
            messagebox.showwarning("Validación", "Tienes campos sin completar")


def actualizar_tree(mitreview):
    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)
    result = get_item()
    for fila in result:
        mitreview.insert(
            "", "end",
            text=fila[0],
            values=(fila[1], fila[2], fila[3], fila[4])
        )


def get_item():
    conection = create_db()
    cursor = conection.cursor()
    sql = "SELECT *  FROM data_game ORDER BY id ASC"
    data = cursor.execute(sql)

    return data.fetchall()


def search_item(var_search, mitreview):
    conection = create_db()
    cursor = conection.cursor()
    sql = "SELECT titulo, estilo, desarrollador, precio FROM data_game WHERE\
    titulo LIKE ? OR estilo LIKE ? OR desarrollador LIKE ?"
    data = cursor.execute(sql, (var_search, var_search, var_search))
    result = data.fetchall()
    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)
    for fila in result:
        mitreview.insert(
            "", "end", values=(fila[0], fila[1], fila[2], fila[3])
        )


def clean_fields(
    var_titulo, var_estilo, var_desarrollador, var_precio, var_search, forms
):
    var_titulo.set("")
    var_estilo.set("")
    var_desarrollador.set("")
    var_precio.set("")
    var_search.set("")
    actualizar_tree(forms)


def tree_selected(
    forms, var_titulo, var_estilo, var_desarrollador, var_precio
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


def change_colors(master, buscar, titulo, estilo, desarrollador, precio,
                  entry_search, entry_add_titulo, entry_add_estilo,
                  entry_add_desarrollador, entry_add_precio,
                  boton_search, boton_add, boton_clean,
                  boton_modify, boton_del, boton_colors):

    global light

    if light:
        bg_color = "#E0E0E0"
        fg_color = "#000000"
        highlight_color = "#FFFFFF"
        light = False
    else:
        bg_color = "#1E1E1E"
        fg_color = "#FFFFFF"
        highlight_color = "#606060"
        light = True

    master.configure(background=bg_color)
    buscar.configure(background=bg_color, foreground=fg_color)
    titulo.configure(background=bg_color, foreground=fg_color)
    estilo.configure(background=bg_color, foreground=fg_color)
    desarrollador.configure(background=bg_color, foreground=fg_color)
    precio.configure(background=bg_color, foreground=fg_color)
    entry_search.configure(background=highlight_color, foreground=fg_color)
    entry_add_titulo.configure(background=highlight_color, foreground=fg_color)
    entry_add_estilo.configure(background=highlight_color, foreground=fg_color)
    entry_add_desarrollador.configure(
        background=highlight_color, foreground=fg_color
    )
    entry_add_precio.configure(background=highlight_color, foreground=fg_color)
    boton_search.configure(background=highlight_color, foreground=fg_color)
    boton_add.configure(background=highlight_color, foreground=fg_color)
    boton_clean.configure(background=highlight_color, foreground=fg_color)
    boton_modify.configure(background=highlight_color, foreground=fg_color)
    boton_del.configure(background=highlight_color, foreground=fg_color)
    boton_colors.configure(background=highlight_color, foreground=fg_color)
