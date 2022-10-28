
from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Entry

def f_tela_produto():
    root = Toplevel()
    root.geometry('300x500')
    root.title('Produto')

    label_codigo = Label(root, text="Produto")
    label_codigo.place(relx=0.5, rely=0.06, anchor="center")

    label_codigo = Label(root, text="Código")
    label_codigo.place(relx=0.1, rely=0.1, anchor="w")

    codigo = StringVar()
    texto_codigo = Entry(root, textvariable= codigo, width=30)
    texto_codigo.place(relx=0.3, rely=0.1, anchor="w")

    label_nome = Label(root, text="Nome")
    label_nome.place(relx=0.1, rely=0.2, anchor="w")

    nome = StringVar()
    texto_nome = Entry(root,textvariable = nome, )
    texto_nome.place(relx=0.3, rely=0.2, anchor="w")

    label_nome = Label(root, text="Tipo de\nProduto")
    label_nome.place(relx=0.1, rely=0.3, anchor="w")

    escolha = StringVar()
    comboBoxTpProduto = Combobox(root, textvariable= escolha, height=0.5, width=24)
    comboBoxTpProduto['values'] = ('teste1', 'teste2', 'teste3')
    comboBoxTpProduto.place(relx=0.3, rely=0.3, anchor="w")

    label_telefone = Label(root, text="Preço")
    label_telefone.place(relx=0.1, rely=0.4, anchor="w")

    telefone = StringVar()
    texto_telefone = Entry(root, textvariable=telefone)
    texto_telefone.place(relx=0.3, rely=0.4, anchor="w")

    btnAddProduto = Button(root, text="Cadastrar")
    btnAddProduto.place(relx=0.5, rely=0.8, anchor="center")

    btnVoltarMenu = Button(root, text="Voltar ao Menu", command= root.destroy)
    btnVoltarMenu.place(relx=0.5, rely=0.9, anchor="center")

    root.mainloop()