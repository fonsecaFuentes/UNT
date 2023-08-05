from tkinter import ttk
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import StringVar
from app_models import DataManagement
from app_models import InterfaceManagement


class MyApp():
    def __init__(self, master):
        self.master = master
        self.data_management = DataManagement()
        self.interface_management = InterfaceManagement()

        self.master.title("Lista de Juegos")

        # variables
        self.var_titulo = StringVar()
        self.var_estilo = StringVar()
        self.var_desarrollador = StringVar()
        self.var_search = StringVar()
        self.var_precio = StringVar()

        # TREEVIEW
        self.forms = ttk.Treeview(self.master)
        self.forms["columns"] = ("titulo", "estilo", "desarrollador", "precio")
        self.forms.column("#0", width=0, minwidth=0)
        self.forms.column("titulo", width=100, minwidth=100)
        self.forms.column("estilo", width=100, minwidth=100)
        self.forms.column("desarrollador", width=100, minwidth=100)
        self.forms.column("precio", width=100, minwidth=100)

        self.forms.heading("#0", text="")
        self.forms.heading("titulo", text="Título")
        self.forms.heading("estilo", text="Estilo")
        self.forms.heading("desarrollador", text="Desarrollador")
        self.forms.heading("precio", text="Precio")

        self.forms.grid(
            row=4, rowspan=3, column=0, columnspan=5, pady=8, padx=8
        )
        self.forms.bind(
            "<<TreeviewSelect>>",
            lambda event: self.interface_management.tree_selected(
                self.forms,
                self.var_titulo,
                self.var_estilo,
                self.var_desarrollador,
                self.var_precio
            )
        )

        # labels
        self.final_work = Label(
            self.master,
            text="TRABAJO FINAL",
            bg="DarkOrchid3",
            fg="thistle1",
            height=1,
            width=40
        )
        self.final_work.grid(
            row=0,
            rowspan=2,
            column=0,
            columnspan=8,
            sticky="w" + "e",
            pady=8,
            padx=8
        )

        self.layout = Label(
            self.master, text="",
            bg="DarkOrchid3",
            fg="thistle1",
            height=1,
            width=40
        )
        self.layout.grid(
            row=8,
            rowspan=2,
            column=0,
            columnspan=8,
            sticky="w" + "e",
            pady=8,
            padx=8
        )

        self.buscar = Label(self.master, text="BUSCAR")
        self.buscar.grid(row=2, column=0, sticky="w", pady=1, padx=8)

        self.titulo = Label(self.master, text="Titulo")
        self.titulo.grid(row=12, column=0, sticky="w", padx=8)

        self.estilo = Label(self.master, text="Estilo")
        self.estilo.grid(row=14, column=0, sticky="w", padx=8)

        self.desarrollador = Label(self.master, text="Desarrollador")
        self.desarrollador.grid(row=12, column=6, sticky="e", padx=8)

        self.precio = Label(self.master, text="Precio")
        self.precio.grid(row=14, column=6, sticky="e", padx=8)

        # imputs

        # imput de busqueda
        self.entry_search = Entry(self.master, textvariable=self.var_search)
        self.entry_search.grid(row=3, column=0, sticky="nsew", pady=8, padx=8)

        # imputs agregar y modificar
        self.entry_add_titulo = Entry(
            self.master, textvariable=self.var_titulo
        )
        self.entry_add_titulo.grid(
            row=13, column=0, columnspan=3, sticky="nsew", pady=8, padx=8
        )

        self.entry_add_estilo = Entry(
            self.master, textvariable=self.var_estilo
        )
        self.entry_add_estilo.grid(
            row=15, column=0, columnspan=3, sticky="nsew", pady=8, padx=8
        )

        self.entry_add_desarrollador = Entry(
            self.master, textvariable=self.var_desarrollador, width=36
        )
        self.entry_add_desarrollador.grid(
            row=13, column=4, columnspan=3, sticky="nsew", pady=8, padx=8
        )

        self.entry_add_precio = Entry(
            self.master, textvariable=self.var_precio
        )
        self.entry_add_precio.grid(
            row=15, column=4, columnspan=3, sticky="nsew", pady=8, padx=8
        )

        # botones

        # boton de busqueda
        self.boton_search = Button(
            self.master, text="Buscar",
            command=lambda: self.data_management.search_item(
                self.var_search.get(), self.forms
            )
        )
        self.boton_search.grid(row=3, column=6, sticky="nsew", pady=8, padx=8)

        # botones agregar, modificar, borrar y limpiar
        self.boton_add = Button(
            self.master,
            text="AGREGAR",
            command=lambda: self.data_management.alta_item(
                self.var_titulo,
                self.var_estilo,
                self.var_desarrollador,
                self.var_precio,
                self.forms
                ),
        )
        self.boton_add.grid(row=16, column=0, sticky="nsew", pady=8, padx=8)

        self.boton_clean = Button(
            self.master,
            text="LIMPIAR",
            command=lambda: self.interface_management.clean_fields(
                self.var_titulo,
                self.var_estilo,
                self.var_desarrollador,
                self.var_precio,
                self.var_search,
                self.forms
            ),
        )
        self.boton_clean.grid(row=16, column=6, sticky="nsew", pady=8, padx=8)

        self.boton_modify = Button(
            self.master,
            text=" MODIFICAR ",
            command=lambda: self.data_management.modify_item(
                self.var_titulo,
                self.var_estilo,
                self.var_desarrollador,
                self.var_precio,
                self.forms))
        self.boton_modify.grid(row=6, column=6, sticky="nsew", pady=8, padx=8)

        self.boton_del = Button(
            self.master, text=" BORRAR ",
            command=lambda: self.data_management.del_item(self.forms)
        )
        self.boton_del.grid(row=4, column=6, sticky="nsew", pady=8, padx=8)

        self.boton_colors = Button(
            self.master, text="Change Colors",
            command=lambda: self.interface_management.change_colors(
                element_list
            )
            )
        self.boton_colors.grid(row=2, column=6, sticky="nsew", pady=8, padx=8)

        # lista de elementos de la interfaz
        element_list = [self.master, self.buscar, self.titulo, self.estilo,
                        self.desarrollador, self.precio, self.entry_search,
                        self.entry_add_titulo, self.entry_add_estilo,
                        self.entry_add_desarrollador, self.entry_add_precio,
                        self.boton_search, self.boton_add, self.boton_clean,
                        self.boton_modify, self.boton_del, self.boton_colors]

        self.data_management.actualizar_tree(self.forms)
