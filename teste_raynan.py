from tkinter import *




    
root = Tk()
root.geometry('300x500')
root.title("Menu Funcionario")

off = PhotoImage(file = r"soso.jpg")

label_menu_funcionario = Label(root, text="MENU FUNCIONARIO")
label_menu_funcionario.place(relx=0.5, rely=0.1, anchor="center")

addCP = Button(root, text="Cadastrar Produtos", background="#808080", foreground="black")
addCP.place(relx=0.5, rely=0.4, anchor="center")

addCE = Button(root, text="Cadastrar Entregador", background="#808080", foreground="black")
addCE.place(relx=0.5, rely=0.5, anchor="center")

edit = Button(root, text="Editar Informação", background="#808080", foreground="black")
edit.place(relx=0.5, rely=0.6, anchor="center")

on_button = Button(root, text="oi", bd = 0)

on_button.place(relx=0.5, rely=0.7, anchor="center")

root.mainloop()
