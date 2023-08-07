from tkinter import ttk
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import StringVar
from app_models import DataManagement
from app_models import InterfaceManagement


class MyButton():
    def __init__(
        self, parent,
        text, command,
        row, column,
        sticky, pady,
        padx
    ):
        self.button = Button(parent, text=text, command=command)
        self.button.grid(
            row=row,
            column=column,
            sticky=sticky,
            padx=padx,
            pady=pady
        )

    def configure(self, **kwargs):
        self.button.configure(**kwargs)


class MyEntry():
    def __init__(
        self, parent,
        textvariable,
        row, column,
        columnspan,
        sticky, pady,
        padx
    ):
        self.entry = Entry(parent, textvariable=textvariable)
        self.entry.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            sticky=sticky,
            padx=padx,
            pady=pady
        )

    def configure(self, **kwargs):
        self.entry.configure(**kwargs)


class MyLabel():
    def __init__(
        self, parent,
        text,
        row, column,
        sticky, pady,
        padx
    ):
        self.label = Label(parent, text=text)
        self.label.grid(
            row=row,
            column=column,
            sticky=sticky,
            padx=padx,
            pady=pady
        )

    def configure(self, **kwargs):
        self.label.configure(**kwargs)


class MyLayout(MyLabel):
    def __init__(
        self, text,
        bg, fg,
        width,
        row,
        rowspan,
        column,
        columnspan,
        sticky,
        pady,
        padx
    ):
        self.layout = Label(
            text=text, bg=bg, fg=fg, width=width
        )
        self.layout.grid(
            row=row,
            column=column,
            rowspan=rowspan,
            columnspan=columnspan,
            sticky=sticky,
            pady=pady,
            padx=padx
        )


class MyApp():
    def __init__(self, master):
        self.master = master
        self.data_management = DataManagement()
        self.interface_management = InterfaceManagement()
        self.light = False

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
        self.final_work = MyLayout(
            text="TRABAJO FINAL",
            bg="DarkOrchid3",
            fg="thistle1",
            width=40,
            row=0,
            rowspan=2,
            column=0,
            columnspan=8,
            sticky="w" + "e",
            pady=8,
            padx=8
        )

        self.layout = MyLayout(
            text="",
            bg="DarkOrchid3",
            fg="thistle1",
            width=40,
            row=8,
            rowspan=2,
            column=0,
            columnspan=8,
            sticky="w" + "e",
            pady=8,
            padx=8
        )

        self.buscar = MyLabel(
            self.master,
            text="BUSCAR",
            row=2, column=0, sticky="w", pady=1, padx=8
        )

        self.titulo = MyLabel(
            self.master,
            text="Título",
            row=12, column=0, sticky="w", pady=8, padx=8
        )

        self.estilo = MyLabel(
            self.master,
            text="Estilo",
            row=14, column=0, sticky="w", pady=8, padx=8
        )

        self.desarrollador = MyLabel(
            self.master,
            text="Desarrollador",
            row=12, column=6, sticky="e", pady=0, padx=8
        )

        self.precio = MyLabel(
            self.master,
            text="Precio",
            row=14, column=6, sticky="e", pady=0, padx=8
        )

        # imputs

        # imput de busqueda
        self.entry_search = MyEntry(
            self.master,
            textvariable=self.var_search,
            row=3, column=0, columnspan=None, sticky="nsew", pady=8, padx=8
        )

        # imputs agregar y modificar
        self.entry_add_titulo = MyEntry(
            self.master,
            textvariable=self.var_titulo,
            row=13, column=0, columnspan=2, sticky="nsew", pady=8, padx=8
        )

        self.entry_add_estilo = MyEntry(
            self.master,
            textvariable=self.var_estilo,
            row=15, column=0, columnspan=2, sticky="nsew", pady=8, padx=8
        )

        self.entry_add_desarrollador = MyEntry(
            self.master,
            textvariable=self.var_desarrollador,
            row=13, column=3, columnspan=4, sticky="nsew", pady=8, padx=8
        )

        self.entry_add_precio = MyEntry(
            self.master,
            textvariable=self.var_precio,
            row=15, column=3, columnspan=4, sticky="nsew", pady=8, padx=8
        )

        # botones

        # boton de busqueda
        self.boton_search = MyButton(
            self.master,
            text="Buscar",
            command=lambda: self.data_management.search_item(
                self.var_search.get(), self.forms
            ),
            row=3, column=6, sticky="nsew", pady=8, padx=8
        )

        # botones agregar, modificar, borrar y limpiar campos

        # boton agregar
        self.boton_add = MyButton(
            self.master,
            text="AGREGAR",
            command=lambda: self.data_management.alta_item(
                self.var_titulo,
                self.var_estilo,
                self.var_desarrollador,
                self.var_precio,
                self.forms
            ),
            row=16, column=0, sticky="nsew", pady=8, padx=8
        )

        # boton limpiar campos
        self.boton_clean = MyButton(
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
            row=16, column=6, sticky="nsew", pady=8, padx=8
        )

        # boton modificar
        self.boton_modify = MyButton(
            self.master,
            text=" MODIFICAR ",
            command=lambda: self.data_management.modify_item(
                self.var_titulo,
                self.var_estilo,
                self.var_desarrollador,
                self.var_precio,
                self.forms
            ),
            row=6, column=6, sticky="nsew", pady=8, padx=8
        )

        # boton borrar
        self.boton_del = MyButton(
            self.master,
            text=" BORRAR ",
            command=lambda: self.data_management.del_item(self.forms),
            row=4, column=6, sticky="nsew", pady=8, padx=8
        )

        # boton cambiar los colores
        self.boton_colors = MyButton(
            self.master,
            text="Change Colors",
            command=lambda: self.change_colors(),
            row=2, column=6, sticky="nsew", pady=8, padx=8
        )

        self.data_management.actualizar_tree(self.forms)

    def change_colors(self):
        if self.light:
            self.bg_color = "#E0E0E0"
            self.fg_color = "#000000"
            self.highlight_color = "#FFFFFF"
            self.light = False
        else:
            self.bg_color = "#1E1E1E"
            self.fg_color = "#FFFFFF"
            self.highlight_color = "#606060"
            self.light = True

        self.configure_colors(
            self.bg_color, self.fg_color, self.highlight_color
        )

    def configure_colors(self, bg_color, fg_color, highlight_color):
        list_buttons = [
            self.boton_colors, self.boton_search, self.boton_add,
            self.boton_clean, self.boton_modify, self.boton_del
        ]
        list_labels = [
            self.titulo, self.estilo, self.desarrollador, self.precio,
            self.buscar
        ]

        list_entries = [
            self.entry_search, self.entry_add_titulo, self.entry_add_estilo,
            self.entry_add_desarrollador, self.entry_add_precio
        ]

        for button in list_buttons:
            button.configure(background=highlight_color, foreground=fg_color)

        for label in list_labels:
            label.configure(background=bg_color, foreground=fg_color)

        for entry in list_entries:
            entry.configure(background=highlight_color, foreground=fg_color)
        self.master.configure(background=bg_color)
