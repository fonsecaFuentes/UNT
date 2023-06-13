from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import re


ligh = True


def create_db():
    conection = sqlite3.connect("database.db")
    return conection


def create_table():
    conection = create_db()
    cursor = conection.cursor()
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table'\
         AND name='data_game'"
    )
    table_ok = cursor.fetchone()

    if not table_ok:
        slq = "CREATE TABLE data_game (id INTEGER PRIMARY KEY,\
            titulo VARCHAR(255), estilo VARCHAR(255), desarrollador\
            VARCHAR(255), precio INTEGER (5))"
        cursor.execute(slq)
        conection.commit()


def alta(forms):
    alta = {
        "titulo": entry_add_titulo.get(),
        "estilo": entry_add_estilo.get(),
        "desarrollador": entry_add_desarrollador.get(),
        "precio": entry_add_precio.get(),
    }

    patron = r"^\d+(\.\d{1,2})?$"

    if re.match(patron, alta["precio"]):
        conection = create_db()
        cursor = conection.cursor()
        slq = "INSERT INTO data_game (titulo, estilo, desarrollador, precio)\
            VALUES (?, ?, ?, ?)"
        cursor.execute(slq, tuple(alta.values()))
        conection.commit()
        actualizar_tree(forms)
    else:
        messagebox.showwarning(
            "Validación", "El valor en el imputs 'precio' no es válido"
        )


def tree_selected(event):
    valor = forms.selection()
    if valor:
        item = forms.item(valor)
        valores = item["values"]

        entry_add_titulo.delete(0, "end")
        entry_add_titulo.insert(0, valores[0])
        entry_add_estilo.delete(0, "end")
        entry_add_estilo.insert(0, valores[1])
        entry_add_desarrollador.delete(0, "end")
        entry_add_desarrollador.insert(0, valores[2])
        entry_add_precio.delete(0, "end")
        entry_add_precio.insert(0, valores[3])


def modificar_item(forms):
    valor = forms.selection()
    item = forms.item(valor)
    mi_id = item["text"]

    alta = {
        "titulo": entry_add_titulo.get(),
        "estilo": entry_add_estilo.get(),
        "desarrollador": entry_add_desarrollador.get(),
        "precio": entry_add_precio.get(),
    }
    patron = r"^\d+(\.\d{1,2})?$"

    if re.match(patron, alta["precio"]):
        print("Cadena válida")
        conection = create_db()
        cursor = conection.cursor()
        slq = "UPDATE data_game SET titulo=?, estilo=?, desarrollador=?,\
            precio=? WHERE id=?"
        cursor.execute(
            slq,
            (
                alta["titulo"],
                alta["estilo"],
                alta["desarrollador"],
                alta["precio"],
                mi_id,
            ),
        )
        conection.commit()
        actualizar_tree(forms)
    else:
        print("Cadena no válida")
        messagebox.showwarning(
            "Validación", "El valor en el imputs 'precio' no es válido"
        )


def borrar_item(forms):
    valor = forms.selection()
    item = forms.item(valor)
    mi_id = item["text"]

    conection = create_db()
    cursor = conection.cursor()
    data = (mi_id,)
    sql = "DELETE FROM data_game WHERE id = ?"
    cursor.execute(sql, data)
    conection.commit()
    forms.delete(valor)


def actualizar_tree(mitreview):
    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)

    conection = create_db()
    cursor = conection.cursor()
    sql = "SELECT *  FROM data_game ORDER BY id ASC"
    data = cursor.execute(sql)

    result = data.fetchall()
    for fila in result:
        mitreview.insert(
            "", "end", text=fila[0], values=(fila[1], fila[2], fila[3], fila[4])
        )


def search(mitreview):
    imput_search = entry_search.get()
    conection = create_db()
    cursor = conection.cursor()
    sql = "SELECT titulo, estilo, desarrollador, precio FROM data_game WHERE\
    titulo=? OR estilo=? OR desarrollador=?"
    data = cursor.execute(sql, (imput_search, imput_search, imput_search))

    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)

    result = data.fetchall()
    for fila in result:
        mitreview.insert("", "end", values=(fila[0], fila[1], fila[2], fila[3]))


def clean_fields(forms):
    entry_add_titulo.delete(0, "end")
    entry_add_estilo.delete(0, "end")
    entry_add_desarrollador.delete(0, "end")
    entry_add_precio.delete(0, "end")
    entry_search.delete(0, "end")
    actualizar_tree(forms)


def connect(forms):
    create_db()
    create_table()
    actualizar_tree(forms)


def change_colors():
    global ligh

    if ligh:
        bg_color = "#E0E0E0"
        fg_color = "#000000"
        highlight_color = "#FFFFFF"
        ligh = False
    else:
        bg_color = "#1E1E1E"
        fg_color = "#FFFFFF"
        highlight_color = "#606060"
        ligh = True

    master.configure(background=bg_color)
    buscar.configure(background=bg_color, foreground=fg_color)
    titulo.configure(background=bg_color, foreground=fg_color)
    estilo.configure(background=bg_color, foreground=fg_color)
    desarrollador.configure(background=bg_color, foreground=fg_color)
    precio.configure(background=bg_color, foreground=fg_color)
    entry_search.configure(background=highlight_color, foreground=fg_color)
    entry_add_titulo.configure(background=highlight_color, foreground=fg_color)
    entry_add_estilo.configure(background=highlight_color, foreground=fg_color)
    entry_add_desarrollador.configure(background=highlight_color, foreground=fg_color)
    entry_add_precio.configure(background=highlight_color, foreground=fg_color)
    boton_search.configure(background=highlight_color, foreground=fg_color)
    boton_add.configure(background=highlight_color, foreground=fg_color)
    boton_clean.configure(background=highlight_color, foreground=fg_color)
    boton_modify.configure(background=highlight_color, foreground=fg_color)
    boton_del.configure(background=highlight_color, foreground=fg_color)
    boton_colors.configure(background=highlight_color, foreground=fg_color)


master = Tk()

# variables
var_titulo = StringVar()
var_estilo = StringVar()
var_desarrollador = StringVar()
entry_search = StringVar()
var_precio = IntVar()

# lista
forms = ttk.Treeview(master)
forms["columns"] = ("titulo", "estilo", "desarrollador", "precio")
forms.column("#0", width=0, minwidth=0)
forms.column("titulo", width=100, minwidth=100)
forms.column("estilo", width=100, minwidth=100)
forms.column("desarrollador", width=100, minwidth=100)
forms.column("precio", width=100, minwidth=100)

forms.heading("#0", text="")
forms.heading("titulo", text="Título")
forms.heading("estilo", text="Estilo")
forms.heading("desarrollador", text="Desarrollador")
forms.heading("precio", text="Precio")

forms.grid(row=4, rowspan=3, column=0, columnspan=5, pady=8, padx=8)
forms.bind("<<TreeviewSelect>>", tree_selected)

# labels
final_work = Label(
    master, text="TRABAJO FINAL", bg="DarkOrchid3", fg="thistle1", height=1, width=40
)
final_work.grid(row=0, rowspan=2, column=0, columnspan=8, sticky=W + E, pady=8, padx=8)

layout = Label(master, text="", bg="DarkOrchid3", fg="thistle1", height=1, width=40)
layout.grid(row=8, rowspan=2, column=0, columnspan=8, sticky=W + E, pady=8, padx=8)

buscar = Label(master, text="BUSCAR")
buscar.grid(row=2, column=0, sticky=W, pady=1, padx=8)

titulo = Label(master, text="Titulo")
titulo.grid(row=12, column=0, sticky=W, padx=8)

estilo = Label(master, text="Estilo")
estilo.grid(row=14, column=0, sticky=W, padx=8)

desarrollador = Label(master, text="Desarrollador")
desarrollador.grid(row=12, column=6, sticky=E, padx=8)

precio = Label(master, text="Precio")
precio.grid(row=14, column=6, sticky=E, padx=8)

# imputs

# imput de busqueda
entry_search = Entry(master)
entry_search.grid(row=3, column=0, sticky="nsew", pady=8, padx=8)

# imputs agregar y modificar
entry_add_titulo = Entry(master)
entry_add_titulo.grid(row=13, column=0, columnspan=3, sticky="nsew", pady=8, padx=8)

entry_add_estilo = Entry(master)
entry_add_estilo.grid(row=15, column=0, columnspan=3, sticky="nsew", pady=8, padx=8)

entry_add_desarrollador = Entry(master, width=36)
entry_add_desarrollador.grid(
    row=13, column=4, columnspan=3, sticky="nsew", pady=8, padx=8
)

entry_add_precio = Entry(master)
entry_add_precio.grid(row=15, column=4, columnspan=3, sticky="nsew", pady=8, padx=8)

# botones

# boton de busqueda
boton_search = Button(master, text="Buscar", command=lambda: search(forms))
boton_search.grid(row=3, column=6, sticky="nsew", pady=8, padx=8)

# botones agregar, modificar, borrar y limpiar
boton_add = Button(master, text="AGREGAR", command=lambda: alta(forms))
boton_add.grid(row=16, column=0, sticky="nsew", pady=8, padx=8)

boton_clean = Button(master, text="LIMPIAR", command=lambda: clean_fields(forms))
boton_clean.grid(row=16, column=6, sticky="nsew", pady=8, padx=8)

boton_modify = Button(master, text=" MODIFICAR ", command=lambda: modificar_item(forms))
boton_modify.grid(row=6, column=6, sticky="nsew", pady=8, padx=8)

boton_del = Button(master, text=" BORRAR ", command=lambda: borrar_item(forms))
boton_del.grid(row=4, column=6, sticky="nsew", pady=8, padx=8)

boton_colors = Button(master, text="Change Colors", command=lambda: change_colors())
boton_colors.grid(row=2, column=6, sticky="nsew", pady=8, padx=8)

connect(forms)
change_colors()

master.mainloop()
