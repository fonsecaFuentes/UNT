from tkinter import ttk
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import StringVar
from model_orm import DataManagement
from model_orm import InterfaceManagement


# Clase MyButton para crear botones personalizados
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


# Clase MyEntry para crear campos de entrada personalizados
class MyEntry():
    def __init__(
        self,
        parent,
        textvariable,
        row,
        rowspan,
        column,
        columnspan,
        sticky,
        pady,
        padx
    ):
        self.entry = Entry(parent, textvariable=textvariable)
        self.entry.grid(
            row=row,
            rowspan=rowspan,
            column=column,
            columnspan=columnspan,
            sticky=sticky,
            padx=padx,
            pady=pady
        )

    def configure(self, **kwargs):
        self.entry.configure(**kwargs)


# Clase MyLabel para crear etiquetas personalizadas
class MyLabel():
    def __init__(
        self, parent,
        text,
        row,
        column,
        sticky,
        pady,
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


# Clase MyLayout para crear diseños personalizados
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


# Clase principal para la aplicación
class MyApp():
    def __init__(self, master):
        # Configuración inicial de la aplicación
        self.master = master
        self.data_management = DataManagement()
        self.interface_management = InterfaceManagement()
        self.light = False

        self.master.title("Lista de Juegos")

        # variables para almacenar datos de entrada
        self.var_title = StringVar()
        self.var_gender = StringVar()
        self.var_developer = StringVar()
        self.var_price = StringVar()
        self.var_search = StringVar()

        # Configuración de TREEVIEW
        self.forms = ttk.Treeview(self.master)
        self.forms["columns"] = ("title", "gender", "developer", "price")
        self.forms.column("#0", width=0, minwidth=0)
        self.forms.column("title", width=100, minwidth=100)
        self.forms.column("gender", width=100, minwidth=100)
        self.forms.column("developer", width=100, minwidth=100)
        self.forms.column("price", width=100, minwidth=100)

        self.forms.heading("#0", text="")
        self.forms.heading("title", text="Título")
        self.forms.heading("gender", text="Género")
        self.forms.heading("developer", text="Desarrollador")
        self.forms.heading("price", text="Precio")

        self.forms.grid(
            row=4, rowspan=3, column=0, columnspan=5, pady=8, padx=8
        )
        self.forms.bind(
            "<<TreeviewSelect>>",
            lambda event: self.interface_management.tree_selected(
                self.forms,
                self.var_title,
                self.var_gender,
                self.var_developer,
                self.var_price
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
            columnspan=9,
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
            columnspan=9,
            sticky="w" + "e",
            pady=8,
            padx=8
        )

        # Label de busqueda
        self.search = MyLabel(
            self.master,
            text="BUSCAR",
            row=2, column=0, sticky="w", pady=1, padx=8
        )

        # Label título
        self.title = MyLabel(
            self.master,
            text="Título",
            row=12, column=0, sticky="w", pady=8, padx=8
        )

        # Label de genero
        self.gender = MyLabel(
            self.master,
            text="Género",
            row=14, column=0, sticky="w", pady=8, padx=8
        )

        # Label de desarrollador
        self.developer = MyLabel(
            self.master,
            text="Desarrollador",
            row=12, column=7, sticky="e", pady=0, padx=8
        )

        # Label de precio
        self.price = MyLabel(
            self.master,
            text="Precio",
            row=14, column=7, sticky="e", pady=0, padx=8
        )

        # Imputs

        # Imput de busqueda
        self.entry_search = MyEntry(
            self.master,
            textvariable=self.var_search,
            row=3,
            rowspan=None,
            column=0,
            columnspan=None,
            sticky="nsew",
            pady=8,
            padx=8
        )

        # Imputs agregar y modificar
        # Imput de titulo
        self.entry_add_title = MyEntry(
            self.master,
            textvariable=self.var_title,
            row=13,
            rowspan=None,
            column=0,
            columnspan=2,
            sticky="nsew",
            pady=8,
            padx=8
        )

        # Imput de genero
        self.entry_add_gender = MyEntry(
            self.master,
            textvariable=self.var_gender,
            row=15,
            rowspan=None,
            column=0,
            columnspan=2,
            sticky="nsew",
            pady=8,
            padx=8
        )

        # Imput de desarrollador
        self.entry_add_developer = MyEntry(
            self.master,
            textvariable=self.var_developer,
            row=13,
            rowspan=None,
            column=4,
            columnspan=4,
            sticky="nsew",
            pady=8,
            padx=8
        )

        # Imput de precio
        self.entry_add_price = MyEntry(
            self.master,
            textvariable=self.var_price,
            row=15,
            rowspan=None,
            column=4,
            columnspan=4,
            sticky="nsew",
            pady=8,
            padx=8
        )

        # Botones

        # Boton de busqueda
        self.boton_search = MyButton(
            self.master,
            text="Buscar",
            command=lambda: self.data_management.search_item(
                self.var_search.get(), self.forms
            ),
            row=3, column=6, sticky="nsew", pady=8, padx=8
        )

        # Boton agregar
        self.boton_add = MyButton(
            self.master,
            text="AGREGAR",
            command=lambda: self.data_management.alta_item(
                self.var_title,
                self.var_gender,
                self.var_developer,
                self.var_price,
                self.forms
            ),
            row=16, column=0, sticky="nsew", pady=8, padx=8
        )

        # Boton limpiar campos
        self.boton_clean = MyButton(
            self.master,
            text="LIMPIAR",
            command=lambda: self.interface_management.clean_fields(
                self.var_title,
                self.var_gender,
                self.var_developer,
                self.var_price,
                self.var_search,
                self.forms
            ),
            row=16, column=7, sticky="nsew", pady=8, padx=8
        )

        # Boton modificar
        self.boton_modify = MyButton(
            self.master,
            text=" MODIFICAR ",
            command=lambda: self.data_management.modify_item(
                self.var_title,
                self.var_gender,
                self.var_developer,
                self.var_price,
                self.forms
            ),
            row=6, column=6, sticky="nsew", pady=8, padx=8
        )

        # Boton borrar
        self.boton_del = MyButton(
            self.master,
            text=" BORRAR ",
            command=lambda: self.data_management.del_item(self.forms),
            row=4, column=6, sticky="nsew", pady=8, padx=8
        )

        # Boton cambiar los colores
        self.boton_colors = MyButton(
            self.master,
            text="Change Colors",
            command=lambda: self.change_colors(),
            row=2, column=6, sticky="nsew", pady=8, padx=8
        )

        # Boton conectar
        self.boton_connect = MyButton(
            self.master,
            text=" CONNECT ",
            command=lambda: self.change_colors(),
            row=3, column=7, sticky="nsew", pady=8, padx=8
        )

        # Boton desconectar
        self.boton_disconnect = MyButton(
            self.master,
            text=" DISCONNECT ",
            command=lambda: self.change_colors(),
            row=4, column=7, sticky="nsew", pady=8, padx=8
        )

        # Boton enviar datos
        self.boton_send_data = MyButton(
            self.master,
            text=" SEND DATA ",
            command=lambda: self.change_colors(),
            row=6, column=7, sticky="nsew", pady=8, padx=8
        )

        self.data_management.actualizar_tree(self.forms)

    # Metodo para cambiar los colores
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

    # Metodo para configurar los colores
    def configure_colors(self, bg_color, fg_color, highlight_color):
        list_buttons = [
            self.boton_colors, self.boton_search, self.boton_add,
            self.boton_clean, self.boton_modify, self.boton_del,
            self.boton_connect, self.boton_disconnect,
            self.boton_send_data
        ]
        list_labels = [
            self.title, self.gender, self.developer, self.price,
            self.search
        ]

        list_entries = [
            self.entry_search, self.entry_add_title, self.entry_add_gender,
            self.entry_add_developer, self.entry_add_price
        ]

        for button in list_buttons:
            button.configure(background=highlight_color, foreground=fg_color)

        for label in list_labels:
            label.configure(background=bg_color, foreground=fg_color)

        for entry in list_entries:
            entry.configure(background=highlight_color, foreground=fg_color)

        self.master.configure(background=bg_color)
