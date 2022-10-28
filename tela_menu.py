from tkinter import *
from tela_pessoa import f_tela_pessoa
from tela_produto import f_tela_produto
from tela_compra import f_tela_compra

def main():
    root = Tk()
    root.geometry('300x500')
    root.title("Menu")

    label_menu = Label(root, text="MENU")
    label_menu.place(relx=0.5, rely=0.1, anchor="center")

    addPessoa = Button(root, text="Adicionar Pessoa", command=f_tela_pessoa, background="#808080", foreground="black")
    addPessoa.place(relx=0.5, rely=0.3, anchor="center")

    addProduto = Button(root, text="Adicionar Produto", command=f_tela_produto, background="#808080", foreground="black")
    addProduto.place(relx=0.5, rely=0.4, anchor="center")

    addCompra = Button(root, text="Fazer Compra", command= f_tela_compra,  background="#808080", foreground="black")
    addCompra.place(relx=0.5, rely=0.5, anchor="center")

    edit = Button(root, text="Editar", background="#808080", foreground="black")
    edit.place(relx=0.5, rely=0.6, anchor="center")
  
    root.mainloop()


    return 0
if __name__=="__main__":
    main()
