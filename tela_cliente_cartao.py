from tkinter import *

def f_cliente_cartao():

    root = Toplevel()
    root.geometry('300x500')
    root.title('Cliente')

    label_cliente = Label(root, text="Cliente")
    label_cliente.place(relx=0.5, rely=0.085, anchor="center")    

    label_codigo = Label(root, text="Código")
    label_codigo.place(relx=0.1, rely=0.1, anchor="w")

    codigo = StringVar()
    texto_codigo = Entry(root,textvariable = codigo, width = 20)
    texto_codigo.place(relx=0.3, rely=0.1, anchor="w")

    label_nome = Label(root, text="Nome")
    label_nome.place(relx=0.1, rely=0.2, anchor="w")

    nome = StringVar()
    texto_nome = Entry(root,textvariable = nome, width = 20)
    texto_nome.place(relx=0.3, rely=0.2, anchor="w")

    label_telefone = Label(root, text="Telefone")
    label_telefone.place(relx=0.1, rely=0.3, anchor="w")

    telefone = StringVar()
    texto_telefone = Entry(root, textvariable = telefone, width = 20)
    texto_telefone.place(relx=0.3, rely=0.3, anchor="w")

    label_codigo = Label(root, text="Forma\nde Pagamento")
    label_codigo.place(relx=0.1, rely=0.4, anchor="w")

    checkPgCartao = Checkbutton(root, text="Cartão", onvalue= 1, offvalue=0)
    checkPgCartao.place(relx=0.45, rely=0.4, anchor="w")

    label_apelido_cartao = Label(root, text="Apelido\ndo Cartão")
    label_apelido_cartao.place(relx=0.1, rely=0.5, anchor="w")

    apelido = StringVar()
    texto_apelido_cartao = Entry(root, textvariable= apelido, width = 20)
    texto_apelido_cartao.place(relx=0.35, rely=0.5, anchor="w")

    label_num_cartao = Label(root, text="Número\ndo Cartão")
    label_num_cartao.place(relx=0.1, rely=0.6, anchor="w")

    numCartao = StringVar()
    texto_num_cartao = Entry(root, textvariable= numCartao, width = 20)
    texto_num_cartao.place(relx=0.35, rely=0.6, anchor="w")

    label_validade = Label(root, text="Validade\ndo Cartão")
    label_validade.place(relx=0.1, rely=0.7, anchor="w")

    validade = StringVar()
    texto_validade = Entry(root, textvariable= validade, width = 20)
    texto_validade.place(relx=0.35, rely=0.7, anchor="w")

    label_cvv = Label(root, text="CVV\ndo Cartão")
    label_cvv.place(relx=0.1, rely=0.8, anchor="w")

    cvv = StringVar()
    texto_cvv = Entry(root, textvariable=cvv, width = 20)
    texto_cvv.place(relx=0.35, rely=0.8, anchor="w")

    btnAddEdereco = Button(root, text="Adicionar Endereço")
    btnAddEdereco.place(relx=0.5, rely=0.88, anchor="center")

    btnVoltar = Button(root, text="Voltar a tela Pessoa")
    btnVoltar.place(relx=0.5, rely=0.95, anchor="center")

    root.mainloop()