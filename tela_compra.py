from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Entry

def f_tela_compra():
    root = Toplevel()
    root.geometry('300x500')
    root.title('Compra')

    label_compra = Label(root, text="Compra")
    label_compra.place(relx=0.5, rely=0.085, anchor="center")

    label_nome = Label(root, text="Cliente")
    label_nome.place(relx=0.1, rely=0.15, anchor="w")

    cliente = StringVar()
    comboBoxCliente = Combobox(root, textvariable= cliente, height=0.5, width=24)
    comboBoxCliente['values'] = ('teste1', 'teste2', 'teste3')
    comboBoxCliente.place(relx=0.3, rely=0.15, anchor="w")

    label_nome = Label(root, text="Produto")
    label_nome.place(relx=0.1, rely=0.25, anchor="w")

    produto = StringVar()
    comboBoxProduto = Combobox(root, textvariable= produto, height=0.5, width=24)
    comboBoxProduto['values'] = ('teste1', 'teste2', 'teste3')
    comboBoxProduto.place(relx=0.3, rely=0.25, anchor="w")

    label_nome = Label(root, text="Quantidade")
    label_nome.place(relx=0.06, rely=0.35, anchor="w")

    qtd = StringVar()
    texto_qtd = Entry(root, textvariable= qtd, width=30)
    texto_qtd.place(relx=0.3, rely=0.35, anchor="w")

    label_nome = Label(root, text="Entregador")
    label_nome.place(relx=0.5, rely=0.45, anchor="center")

    entregador = StringVar()
    comboBoxEntregador = Combobox(root, textvariable= entregador, height=0.5, width=24)
    comboBoxEntregador['values'] = ('teste1', 'teste2', 'teste3')
    comboBoxEntregador.place(relx=0.5, rely=0.50, anchor="center")

    label_nome = Label(root, text="SubTotal")
    label_nome.place(relx=0.5, rely=0.6, anchor="center")

    subTotal = StringVar()
    texto_subTotal = Entry(root, textvariable= subTotal, width=30)
    texto_subTotal.place(relx=0.5, rely=0.65, anchor="center")

    btnAddCarrinho = Button(root, text="Adicionar ao\nCarrinho")
    btnAddCarrinho.place(relx=0.5, rely=0.75, anchor="center")

    btnAddCompra = Button(root, text="Finalizar Compra")
    btnAddCompra.place(relx=0.5, rely=0.85, anchor="center")

    btnMenu = Button(root, text="Voltar ao Menu", command= root.destroy)
    btnMenu.place(relx=0.5, rely=0.95, anchor="center")

    root.mainloop()