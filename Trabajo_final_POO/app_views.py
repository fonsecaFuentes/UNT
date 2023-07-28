from tkinter import ttk
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import StringVar
import app_models


class MyApp():
    def __init__(self, master, app_model):
        self.master = master
        self.app_model = app_model
        self.vista_app()

    def vista_app(self):

        data_management = app_models.DataManagement()
        interface_management = app_models.InterfaceManagement()

        self.master.title("Lista de Juegos")

        # variables
        var_titulo = StringVar()
        var_estilo = StringVar()
        var_desarrollador = StringVar()
        var_search = StringVar()
        var_precio = StringVar()

        # TREEVIEW
        forms = ttk.Treeview(self.master)
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
        forms.bind(
            "<<TreeviewSelect>>",
            lambda event: interface_management.tree_selected(
                forms, var_titulo, var_estilo, var_desarrollador, var_precio
            )
        )

        # labels
        final_work = Label(
            self.master,
            text="TRABAJO FINAL",
            bg="DarkOrchid3",
            fg="thistle1",
            height=1,
            width=40
        )
        final_work.grid(
            row=0,
            rowspan=2,
            column=0,
            columnspan=8,
            sticky="w" + "e",
            pady=8,
            padx=8
        )

        layout = Label(
            self.master, text="",
            bg="DarkOrchid3",
            fg="thistle1",
            height=1,
            width=40
        )
        layout.grid(
            row=8,
            rowspan=2,
            column=0,
            columnspan=8,
            sticky="w" + "e",
            pady=8,
            padx=8
        )

        buscar = Label(self.master, text="BUSCAR")
        buscar.grid(row=2, column=0, sticky="w", pady=1, padx=8)

        titulo = Label(self.master, text="Titulo")
        titulo.grid(row=12, column=0, sticky="w", padx=8)

        estilo = Label(self.master, text="Estilo")
        estilo.grid(row=14, column=0, sticky="w", padx=8)

        desarrollador = Label(self.master, text="Desarrollador")
        desarrollador.grid(row=12, column=6, sticky="e", padx=8)

        precio = Label(self.master, text="Precio")
        precio.grid(row=14, column=6, sticky="e", padx=8)

        # imputs

        # imput de busqueda
        entry_search = Entry(self.master, textvariable=var_search)
        entry_search.grid(row=3, column=0, sticky="nsew", pady=8, padx=8)

        # imputs agregar y modificar
        entry_add_titulo = Entry(self.master, textvariable=var_titulo)
        entry_add_titulo.grid(
            row=13, column=0, columnspan=3, sticky="nsew", pady=8, padx=8
        )

        entry_add_estilo = Entry(self.master, textvariable=var_estilo)
        entry_add_estilo.grid(
            row=15, column=0, columnspan=3, sticky="nsew", pady=8, padx=8
        )

        entry_add_desarrollador = Entry(
            self.master, textvariable=var_desarrollador, width=36
        )
        entry_add_desarrollador.grid(
            row=13, column=4, columnspan=3, sticky="nsew", pady=8, padx=8
        )

        entry_add_precio = Entry(self.master, textvariable=var_precio)
        entry_add_precio.grid(
            row=15, column=4, columnspan=3, sticky="nsew", pady=8, padx=8
        )

        # botones

        # boton de busqueda
        boton_search = Button(
            self.master, text="Buscar",
            command=lambda: data_management.search_item(
                var_search.get(), forms
            )
        )
        boton_search.grid(row=3, column=6, sticky="nsew", pady=8, padx=8)

        # botones agregar, modificar, borrar y limpiar
        boton_add = Button(
            self.master,
            text="AGREGAR",
            command=lambda: data_management.alta_item(
                var_titulo,
                var_estilo,
                var_desarrollador,
                var_precio,
                forms
                ),
        )
        boton_add.grid(row=16, column=0, sticky="nsew", pady=8, padx=8)

        boton_clean = Button(
            self.master,
            text="LIMPIAR",
            command=lambda: interface_management.clean_fields(
                var_titulo,
                var_estilo,
                var_desarrollador,
                var_precio,
                var_search,
                forms
            ),
        )
        boton_clean.grid(row=16, column=6, sticky="nsew", pady=8, padx=8)

        boton_modify = Button(
            self.master,
            text=" MODIFICAR ",
            command=lambda: data_management.modify_item(
                var_titulo,
                var_estilo,
                var_desarrollador,
                var_precio,
                forms))
        boton_modify.grid(row=6, column=6, sticky="nsew", pady=8, padx=8)

        boton_del = Button(
            self.master, text=" BORRAR ",
            command=lambda: data_management.del_item(forms)
        )
        boton_del.grid(row=4, column=6, sticky="nsew", pady=8, padx=8)

        boton_colors = Button(
            self.master, text="Change Colors",
            command=lambda: interface_management.change_colors(element_list)
            )
        boton_colors.grid(row=2, column=6, sticky="nsew", pady=8, padx=8)

        # lista de elementos de la interfaz
        element_list = [self.master, buscar, titulo, estilo, desarrollador,
                        precio, entry_search, entry_add_titulo,
                        entry_add_estilo, entry_add_desarrollador,
                        entry_add_precio, boton_search, boton_add, boton_clean,
                        boton_modify, boton_del, boton_colors]

        data_management.connect(forms)
