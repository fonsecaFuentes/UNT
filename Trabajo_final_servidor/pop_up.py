from tkinter import Toplevel
from tkinter import ttk
from tkinter import StringVar
from views import MyButton
from views import MyEntry
from views import MyLabel
from users import DataUsers


class PopUp():
    def __init__(self, master):
        self.master = master
        self.var_name = StringVar()
        self.register = DataUsers()

        self.user_registration_popup()

    def register_and_close_popup(self, users):
        if self.register.register_user(self.var_name, users):
            self.user_registration_popup.destroy()

    # Crear una ventana emergente para el registro de usuario
    def user_registration_popup(self):
        # self.user_registration_popup = tk.Toplevel(self.master)
        self.user_registration_popup = Toplevel()
        self.user_registration_popup.geometry("270x330")
        self.user_registration_popup.title("Registro de Usuario")

        self.user_registration_popup.lift(self.master)

        # Selección de usuario
        self.forms = ttk.Treeview(self.user_registration_popup)
        self.forms['columns'] = ('name')
        self.forms.column("#0", width=0, minwidth=0)
        self.forms.column("name", width=100, minwidth=100)

        self.forms.heading("#0", text="")
        self.forms.heading("name", text="Usuario")

        self.forms.grid(
            row=4, rowspan=3, column=0, pady=8, padx=8
        )

        # self.forms.bind(
        #     "<<TreeviewSelect>>",
        #     lambda event: self.register.tree_selected(
        #         self.forms,
        #         self.var_name,
        #     )
        # )

        # Botón para selecionar al usuario
        self.button_selected = MyButton(
            self.user_registration_popup,
            text="Selecionar",
            command=lambda: self.register.tree_selected(
                self.forms, self.var_name,
            ),
            row=5,
            column=1,
            sticky="nsew",
            pady=8,
            padx=8
        )

        # Etiqueta en la ventana emergente
        self.label_register = MyLabel(
            self.user_registration_popup,
            text="Nombre de Usuario:",
            row=0,
            column=0,
            sticky="w",
            pady=8,
            padx=8
        )

        # Campo de entrada para el nombre de usuario
        self.username_entry = MyEntry(
            self.user_registration_popup,
            textvariable=self.var_name,
            row=0,
            column=1,
            rowspan=None,
            columnspan=None,
            sticky="w",
            pady=8,
            padx=8
        )

        # Botón para registrar al usuario
        self.button_register = MyButton(
            self.user_registration_popup,
            text="Registrarse",
            command=lambda: self.register_and_close_popup(self.forms),
            row=1,
            column=0,
            sticky="nsew",
            pady=8,
            padx=8
        )

        self.register.actualizar_tree(self.forms)

        # Establece el foco en la ventana emergente
        self.user_registration_popup.grab_set()
        # Espera hasta que la ventana emergente se cierre
        self.user_registration_popup.wait_window()
