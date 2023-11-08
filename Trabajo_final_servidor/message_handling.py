from tkinter import messagebox


# Manejo de mensajes
class MenssageHandler():

    # Mensajes de información
    def message_info(self, info):
        messagebox.showinfo("✓", info)

    # Mensajes de advertencia
    def message_warning(self, warning):
        messagebox.showwarning("Aviso", warning)

    # Mensajes de confirmación
    def message_confirm(self, confirm):
        confirm = messagebox.askyesno("Confirmación", confirm)
        return confirm

    # Mensajes de error
    def message_error(self, error):
        messagebox.showerror("Error", error)
