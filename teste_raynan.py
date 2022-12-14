from tkinter import *
from teste_funcao_raynan import *
from tkinter.ttk import Combobox
from tkinter.ttk import Entry

fk_endereco_codigo = 0

def f_tela_senha():
    root = Tk()
    root.geometry('300x500')
    root.title("Esqueci minha senha")

    label_menu_cliente = Label(root,text="Trocar senha")
    label_menu_cliente.place(relx= 0.5,rely= 0.1,anchor="center")

    label_informarDados = Label(root,text="Informe seus dados")
    label_informarDados.place(relx= 0.5,rely= 0.2,anchor="center")

    label_cpf = Label(root,text="CPF:")
    label_cpf.place(relx= 0.1,rely= 0.3,anchor="w")

    label_username = Label(root,text="Username:")
    label_username.place(relx= 0.1,rely= 0.4,anchor="w")

    label_senha = Label(root,text="Nova senha:")
    label_senha.place(relx= 0.1,rely= 0.5,anchor="w")

    user = StringVar()
    texto_username = Entry(root,textvariable=user)
    texto_username.place(relx= 0.4,rely= 0.4,anchor="w")

    cpf = StringVar()
    texto_cpf = Entry(root,textvariable=cpf)
    texto_cpf.place(relx= 0.4,rely= 0.3,anchor="w")

    nSenha = StringVar()
    texto_senha = Entry(root,textvariable=nSenha)
    texto_senha.place(relx= 0.4,rely= 0.5,anchor="w")

    atualizar = Button(root, text="Redefinir", background="#808080", foreground="black", command= lambda: [f_redefinir_senha(user.get(), cpf.get(), nSenha.get()), root.destroy(), main()])
    atualizar.place(relx=0.5, rely=0.8, anchor="center")

    sair = Button(root, text="Sair", background="#808080", foreground="black", command= lambda: [root.destroy(), main()])
    sair.place(relx=0.5, rely=0.9, anchor="center")

    root.mainloop()

def f_tela_entrega(username):
    root = Toplevel()
    root.geometry('300x500')
    root.title('Entrega')

    #label
    label_entrega = Label(root, text="ENTREGA",background='black',foreground='white')
    label_compra = Label(root, text="Compra:")
     
    label_nome = Label(root, text="Nome:")
    label_telefone = Label(root, text="Telefone:")
    label_cep = Label(root, text="CEP:")
    label_logradouro = Label(root, text="Logradouro:")
    label_numero = Label(root, text="Numero:")
    label_complemento = Label(root, text="Complemento:")
    label_bairro = Label(root, text="Bairro:")
    label_cidade = Label(root, text="Cidade:")
    label_tp_logradouro = Label(root, text="Tp. Logradouro:")

    label_nm = Label(root, text="")
    label_tel = Label(root, text="")
    label_cp = Label(root, text="")
    label_log = Label(root, text="")
    label_num = Label(root, text="")
    label_comp = Label(root, text="")
    label_bai = Label(root, text="")
    label_cid = Label(root, text="")
    label_tp = Label(root, text="")


    #combobox

    compra = StringVar()
    ComboBoxCompra = Combobox(root,textvariable = compra, width= 20, state= 'readonly')
    compraCombo = f_entregar_compra()
    compraCombo = f_retornaLista(compraCombo)
    compraCombo.insert(0, '')
    ComboBoxCompra['values'] = compraCombo
    ComboBoxCompra.bind("<<ComboboxSelected>>", lambda event, parametro = ComboBoxCompra: f_info_compras(compra, label_nm, label_tel, label_cp, label_log, label_num, label_comp, label_bai, label_cid, label_tp))
    #bot??o
    addRE = Button(root,text="Realizar Entrega", command= lambda: [f_atualizar_entregador(username, compra.get()), root.destroy()])
    addM = Button(root,text="Voltar ao menu",command=root.destroy)

    #posicionamento label

    label_entrega.place(relx= 0.5,rely= 0.1,anchor='center')
    label_compra.place(relx= 0.1,rely= 0.2,anchor='center')
    
    #posicionamento combobox
    ComboBoxCompra.place(relx= 0.5,rely= 0.2,anchor='center')

    #posicionamento bot??o
    addRE.place(relx=0.5,rely=0.8,anchor='center')
    addM.place(relx=0.5,rely=0.9,anchor='center')

    label_nome.place(relx= 0.2,rely= 0.3,anchor='center')
    label_telefone.place(relx= 0.2,rely= 0.35,anchor='center')
    label_cep.place(relx= 0.2,rely= 0.4,anchor='center')
    label_logradouro.place(relx= 0.2,rely= 0.45,anchor='center')
    label_numero.place(relx= 0.2,rely= 0.5,anchor='center')
    label_complemento.place(relx= 0.2,rely= 0.55,anchor='center')
    label_bairro.place(relx= 0.2,rely= 0.6,anchor='center')
    label_cidade.place(relx= 0.2,rely= 0.65,anchor='center')
    label_tp_logradouro.place(relx= 0.2,rely= 0.7,anchor='center')

    label_nm.place(relx= 0.5,rely= 0.3,anchor='center')
    label_tel.place(relx= 0.5,rely= 0.35,anchor='center')
    label_cp.place(relx= 0.5,rely= 0.4,anchor='center')
    label_log.place(relx= 0.5,rely= 0.45,anchor='center')
    label_num.place(relx= 0.5,rely= 0.5,anchor='center')
    label_comp.place(relx= 0.5,rely= 0.55,anchor='center')
    label_bai.place(relx= 0.5,rely= 0.6,anchor='center')
    label_cid.place(relx= 0.5,rely= 0.65,anchor='center')
    label_tp.place(relx= 0.5,rely= 0.7,anchor='center')
    
    root.mainloop()


def f_tela_compra(username):
    dicProdutos = {}
    root = Toplevel()
    root.geometry('300x500')
    root.title('Compra')

    label_compra = Label(root, text="Compra")
    label_compra.place(relx=0.5, rely=0.085, anchor="center")

    label_nome = Label(root, text="Cliente")
    label_nome.place(relx=0.1, rely=0.15, anchor="w")


    texto_cliente = Entry(root, width=24)
    texto_cliente.insert(0, username)
    texto_cliente.config(state='readonly')
    texto_cliente.place(relx=0.3, rely=0.15, anchor="w")

    label_nome = Label(root, text="Produto")
    label_nome.place(relx=0.1, rely=0.25, anchor="w")

    produto = StringVar()
    comboBoxProduto = Combobox(root, textvariable= produto, width=24, state='readonly')
    produtoCombo = f_retornaInfo(['nome'], 'PRODUTO')
    produtoCombo = f_retornaLista(produtoCombo)
    produtoCombo.insert(0, '')
    comboBoxProduto['values'] = produtoCombo
    comboBoxProduto.place(relx=0.3, rely=0.25, anchor="w")

    label_tpPagamento = Label(root, text="Tp.\nPagamento")
    label_tpPagamento.place(relx=0.08, rely=0.30, anchor="w")

    tpPagamento = StringVar()
    comboBoxtpPagamento = Combobox(root, textvariable= tpPagamento, width=24, state='readonly')
    tpPagamentoCombo = f_retornaInfo(['tipo_pagamento'], 'TIPO_PAGAMENTO')
    tpPagamentoCombo = f_retornaLista(tpPagamentoCombo)
    tpPagamentoCombo.insert(0, '')
    comboBoxtpPagamento['values'] = tpPagamentoCombo
    comboBoxtpPagamento.place(relx=0.3, rely=0.30, anchor="w")

    label_carrinho = Label(root, text="Carrinho")
    label_carrinho.place(relx=0.5, rely=0.35, anchor="center")

    listBoxCarrinho = Listbox(root, height=5, width=45)
    listBoxCarrinho.place(relx=0.5, rely=0.45, anchor="center")

    label_nome = Label(root, text="SubTotal")
    label_nome.place(relx=0.5, rely=0.6, anchor="center")

    subTotal = IntVar()
    texto_subTotal = Entry(root, textvariable= subTotal, width=30)
    texto_subTotal.place(relx=0.5, rely=0.65, anchor="center")

    btnAddCarrinho = Button(root, text="Adicionar ao\nCarrinho", command= lambda: f_adiciona_produto(dicProdutos, subTotal.get(), texto_subTotal, listBoxCarrinho, produtoCombo, pos_produto= f_codigo(produto, produtoCombo)))
    btnAddCarrinho.place(relx=0.5, rely=0.75, anchor="center")

    btnDelCarrinho = Button(root, text="Retirar", command= lambda: f_retirar_produto(listBoxCarrinho, dicProdutos, texto_subTotal, subTotal.get()))
    btnDelCarrinho.place(relx=0.8, rely=0.6, anchor="center")

    btnAddCompra = Button(root, text="Finalizar Compra", command= lambda: [f_cadastar_compra(username, subTotal.get(), dicProdutos, tpPagamentoCombo = f_codigo(tpPagamento, tpPagamentoCombo)),root.destroy()])
    btnAddCompra.place(relx=0.5, rely=0.85, anchor="center")

    btnMenu = Button(root, text="Voltar ao Menu", command=lambda: root.destroy())
    btnMenu.place(relx=0.5, rely=0.95, anchor="center")

    root.mainloop()


def f_endereco(nome,cpf,tel,username,senha, tpPessoa,edit,fk_endereco_codigo):
    root = Toplevel()
    root.geometry('300x500')
    root.title('ENDERE??O')

    if(username.get() == '' or len(username.get()) > 25):
        root.destroy()
        messagebox.showinfo('USERNAME', 'O username ultrapassa 25 caracteres ou se encontra vazio!!')
    elif(nome.get() == '' or len(nome.get()) > 250):
        root.destroy()
        messagebox.showinfo('NOME', 'O nome ultrapassa 250 caracteres ou se encontra vazio!!')
    elif(tel.get() == '' or len(tel.get()) > 20):
        root.destroy()
        messagebox.showinfo('TELEFONE', 'O telefone ultrapassa 20 caracteres ou se encontra vazio!!')
    elif(cpf.get() == '' or len(cpf.get()) > 14):
        root.destroy()
        messagebox.showinfo('CPF', 'O nome ultrapassa 14 caracteres ou se encontra vazio!!')
    elif(senha.get() == '' or len(senha.get()) > 25):
        root.destroy()
        messagebox.showinfo('SENHA', 'O nome ultrapassa 25 caracteres ou se encontra vazio!!')
    else:
        info = list()
        #label
        label_endereco = Label(root, text= "ENDERE??O",background='orange')
        label_nm = Label(root, text = "NOME DO CLIENTE:",background='black', foreground='white')
        label_tl = Label(root, text = "TIPO\nLOGRADOURO:",background='black', foreground='white')
        label_logradouro = Label(root, text = "LOGADOURO:",background='black', foreground='white')
        label_numero = Label(root, text = "N??MERO:",background='black', foreground='white')
        label_cep = Label(root, text = "CEP:",background='black', foreground='white')
        label_bairro = Label(root, text = "BAIRRO:",background='black', foreground='white')
        label_cidade = Label(root, text = "CIDADE:",background='black', foreground='white')
        label_complemento = Label(root,text= "COMPLEMENTO:",background='black', foreground='white')

        #texto 
        nm = StringVar()
        texto_nm = Entry(root,textvariable = nm, width=20)

        logradouro = StringVar()
        texto_logradouro = Entry(root, textvariable = logradouro, width=20)

        numero = StringVar()
        texto_numero = Entry(root, textvariable = numero, width=20)

        cep = StringVar()
        texto_cep = Entry(root, textvariable = cep, width=20)

        complemento = StringVar()
        texto_complemento = Entry(root, textvariable=complemento,width=20)

        #combobox
        boxtl = StringVar()
        comboBoxTl = Combobox(root,textvariable = boxtl, width= 20)
        tpLg = f_retornaInfo(['descricao'], 'TIPO_LOGRADOURO')
        tpLg = f_retornaLista(tpLg)
        tpLg.insert(0, '')
        comboBoxTl['values'] = tpLg

        boxcidade = StringVar()
        comboBoxCidade = Combobox(root,textvariable = boxcidade, width= 20)
        cidade = f_retornaInfo(['descricao'], 'CIDADE')
        cidade = f_retornaLista(cidade)
        cidade.insert(0, '')
        comboBoxCidade['values'] = cidade

        boxbairro = StringVar()
        comboBoxBairro = Combobox(root,textvariable = boxbairro, width= 20)
        bairro = f_retornaInfo(['descricao'], 'BAIRRO')
        bairro = f_retornaLista(bairro)
        bairro.insert(0, '')
        comboBoxBairro['values'] = bairro

        #bot??o
        if(edit == 0 or edit == 2):
            addE = Button(root, text ="Cadastrar pessoa",command = lambda: f_cadastrar_pessoas(nome.get(),cpf.get(),tel.get(),username.get(),senha.get(), logradouro.get(), numero.get(), cep.get(), complemento.get(), boxtl.get(), boxcidade.get(), boxbairro.get(), tpPessoa, teste = (f_codigo(boxtl, tpLg), f_codigo(boxcidade, cidade), f_codigo(boxbairro, bairro))))
            btnVoltar = Button(root, text="Voltar para\ntela pessoa", command= root.destroy)
        else:
            #addE = Button(root, text ="Atualizar Cadastro",command = lambda: f_atualizar_pessoas(nome.get(),cpf.get(),tel.get(),username.get(),senha.get(), logradouro.get(), numero.get(), cep.get(), complemento.get(), boxtl.get(), boxcidade.get(), boxbairro.get(), tpPessoa, teste = (f_codigo(boxtl, tpLg), f_codigo(boxcidade, cidade), f_codigo(boxbairro, bairro))))
            btnVoltar = Button(root, text="Voltar ao Menu", command= root.destroy)
        
        #if(edit == 1 or edit == 2):
            #info = f_editar_endereco(fk_endereco_codigo)
            #if(len(info) != 0):
                #texto_cep.insert(0,info[0][0])
                #texto_logradouro.insert(0,info[0][1])
                #texto_numero.insert(0,info[0][2])
                #comboBoxBairro.current(info[0][3])
                #comboBoxCidade.current(info[0][4])
                #comboBoxTl.current(info[0][5])
                #texto_complemento.insert(0,info[0][6])

        #posicionamento label
        label_endereco.place(relx = 0.5,rely = 0.030,anchor = 'center')
        label_nm.place(relx= 0.05,rely= 0.10,anchor='w')
        label_tl.place(relx= 0.13,rely= 0.2,anchor= 'w')
        label_logradouro.place(relx= 0.15,rely= 0.3,anchor= 'w')
        label_numero.place(relx=0.23,rely= 0.4,anchor='w')
        label_cep.place(relx = 0.32, rely= 0.5,anchor ='w')
        label_bairro.place(relx = 0.25, rely= 0.6, anchor='w')
        label_cidade.place(relx= 0.25 ,rely= 0.7,anchor= 'w')
        label_complemento.place(relx=0.1,rely=0.8,anchor='w')

        #posicionamento texto
        texto_nm.place(relx= 0.5,rely= 0.10,anchor = 'w')
        texto_logradouro.place(relx= 0.5,rely= 0.3,anchor ='w')
        texto_numero.place(relx= 0.5,rely= 0.4,anchor ='w')
        texto_cep.place(relx= 0.5,rely= 0.5,anchor ='w')
        texto_complemento.place(relx= 0.5,rely= 0.8,anchor='w')

        #posicionamento bot??o

        addE.place(relx= 0.3, rely= 0.9, anchor='center')
        btnVoltar.place(relx= 0.7, rely= 0.9, anchor='center')

        #posicionameto

        comboBoxTl.place(relx=0.5 ,rely=0.2 ,anchor= 'w')
        comboBoxCidade.place(relx= 0.5,rely=0.7 ,anchor= 'w')
        comboBoxBairro.place(relx= 0.5,rely=0.6 ,anchor= 'w')

        root.mainloop()

def f_tela_pessoa(tpPessoa,edit,username):
    global fk_endereco_codigo
    root = Tk()

    root.geometry('300x500')
    root.title('Pessoa')
    #bot??es
    if(edit == 0):
        addM = Button(root, text='Voltar ao menu',command =lambda:[root.destroy(), main()])
    else:
        addM = Button(root, text='Voltar ao menu',command =lambda:root.destroy())
    addE = Button(root,text='Adicionar endere??o', command=lambda: f_endereco(nome,cpf,tel,user,senha, tpPessoa,edit,fk_endereco_codigo))
    #label
    label_pessoa = Label(root,text ="PESSOA")
    label_username = Label(root,text="USERNAME:")
    label_senha = Label(root,text="SENHA:")
    label_nome = Label(root,text="NOME:")
    label_tel = Label(root,text="TELEFONE:")
    label_cpf = Label(root,text="CPF:")

    #textos
    nome = StringVar()
    texto_nome = Entry(root, textvariable = nome, width=20)
    tel = StringVar()
    texto_tel = Entry(root, textvariable = tel, width=20)
    cpf = StringVar()
    texto_cpf = Entry(root, textvariable = cpf, width=20)
    user = StringVar()
    texto_username = Entry(root,textvariable=user, width=20)
    senha = StringVar()
    texto_senha = Entry(root,textvariable=senha, width=20)
    """"
    if(edit == 1 or edit == 2):
       info = f_editar_pessoa(username)
       if(len(info) != 0):
        texto_nome.insert(0,info[0][0])
        texto_tel.insert(0,info[0][1])
        texto_cpf.insert(0,info[0][2])
        texto_username.insert(0,info[0][3])
        texto_senha.insert(0,info[0][4])
        fk_endereco_codigo = info[0][5]"""
        

    #posicionamento textos
    texto_nome.place(relx = 0.4, rely = 0.2, anchor = 'w')
    texto_tel.place(relx = 0.4, rely = 0.3, anchor = 'w')
    texto_cpf.place(relx = 0.4, rely =0.4, anchor = 'w')
    texto_username.place(relx= 0.4, rely= 0.5, anchor = 'w')
    texto_senha.place(relx= 0.4,rely= 0.6,anchor='w')

    #posicionamento Label
    label_pessoa.place(relx = 0.5, rely = 0.1, anchor = 'n')
    label_nome.place(relx = 0.2, rely = 0.2, anchor = 'w')
    label_tel.place(relx = 0.14, rely = 0.3, anchor = 'w')
    label_cpf.place(relx = 0.25, rely = 0.4, anchor = 'w')
    label_username.place(relx=0.12,rely= 0.5,anchor='w')
    label_senha.place(relx=0.21,rely= 0.6,anchor='w')

    #posicionamento bot??es
    addE.place(relx = 0.5, rely = 0.83, anchor = 'center')
    addM.place(relx = 0.5, rely = 0.93, anchor = 'center')
    

    root.mainloop()

def f_editar_produto(username):
    root = Toplevel()
    root.geometry('300x500')
    root.title('Editar Produto')

    cbProduto = StringVar()
    comboBoxProduto = Combobox(root, textvariable = cbProduto)
    Produto = f_retornaInfo(['nome'], 'PRODUTO')
    Produto = f_retornaLista(Produto)
    Produto.insert(0, '')
    comboBoxProduto['values'] = Produto
    comboBoxProduto.place(relx=0.3, rely=0.15, anchor="w")
    #comboBoxProduto.bind("<<ComboboxSelected>>", lambda event, parametro = comboBoxProduto: f_info_produtos(cbProduto.get()))

    label_codigo = Label(root, text="Produto")
    label_codigo.place(relx=0.5, rely=0.06, anchor="center")

    label_nome = Label(root, text="Nome")
    label_nome.place(relx=0.1, rely=0.2, anchor="w")

    nome = StringVar()
    texto_nome = Entry(root,textvariable = nome, )
    texto_nome.place(relx=0.3, rely=0.2, anchor="w")

    label_nome = Label(root, text="Tipo de\nProduto")
    label_nome.place(relx=0.1, rely=0.3, anchor="w")

    cbTpProduto = StringVar()
    comboBoxTpProduto = Combobox(root, textvariable = cbTpProduto)
    tpProduto = f_retornaInfo(['descricao'], 'TIPO_PRODUTO')
    tpProduto = f_retornaLista(tpProduto)
    tpProduto.insert(0, '')
    comboBoxTpProduto['values'] = tpProduto
    comboBoxTpProduto.place(relx=0.3, rely=0.3, anchor="w")

    label_valor = Label(root, text="Pre??o")
    label_valor.place(relx=0.1, rely=0.4, anchor="w")

    valor = StringVar()
    texto_valor = Entry(root, textvariable=valor)
    texto_valor.place(relx=0.3, rely=0.4, anchor="w")

    label_valor = Label(root, text="Descri????o")
    label_valor.place(relx=0.1, rely=0.6, anchor="w")

    texto_descricao = Text(root, height= 5, width=23)
    texto_descricao.place(relx=0.3, rely=0.6, anchor="w")

    btnAddProduto = Button(root, text="Alterar", command=lambda:[f_cadastrar_produto(nome.get(), cbTpProduto.get(), valor.get(), texto_descricao.get("1.0", END), new=f_codigo(cbTpProduto, tpProduto), cod_func= f_funcRes(username)), root.destroy()]) #command=part(f_cadastrar, root)
    btnAddProduto.place(relx=0.5, rely=0.8, anchor="center")


    btnVoltarMenu = Button(root, text="Voltar ao Menu", command= root.destroy)
    btnVoltarMenu.place(relx=0.5, rely=0.9, anchor="center")

    root.mainloop()

def f_produto(username):
    root = Toplevel()
    root.geometry('300x500')
    root.title('Produto')

    label_codigo = Label(root, text="Produto")
    label_codigo.place(relx=0.5, rely=0.06, anchor="center")

    label_nome = Label(root, text="Nome")
    label_nome.place(relx=0.1, rely=0.2, anchor="w")

    nome = StringVar()
    texto_nome = Entry(root,textvariable = nome)
    texto_nome.place(relx=0.3, rely=0.2, anchor="w")

    label_nome = Label(root, text="Tipo de\nProduto")
    label_nome.place(relx=0.1, rely=0.3, anchor="w")

    cbTpProduto = StringVar()
    comboBoxTpProduto = Combobox(root, textvariable = cbTpProduto)
    tpProduto = f_retornaInfo(['descricao'], 'TIPO_PRODUTO')
    tpProduto = f_retornaLista(tpProduto)
    tpProduto.insert(0, '')
    comboBoxTpProduto['values'] = tpProduto
    comboBoxTpProduto.place(relx=0.3, rely=0.3, anchor="w")

    label_valor = Label(root, text="Pre??o")
    label_valor.place(relx=0.1, rely=0.4, anchor="w")

    valor = StringVar()
    texto_valor = Entry(root, textvariable=valor)
    texto_valor.place(relx=0.3, rely=0.4, anchor="w")

    label_valor = Label(root, text="Descri????o")
    label_valor.place(relx=0.1, rely=0.6, anchor="w")

    texto_descricao = Text(root, height= 5, width=23)
    texto_descricao.place(relx=0.3, rely=0.6, anchor="w")

    btnAddProduto = Button(root, text="Cadastrar", command=lambda:[f_cadastrar_produto(nome.get(), cbTpProduto.get(), valor.get(), texto_descricao.get("1.0", END), new=f_codigo(cbTpProduto, tpProduto), cod_func= f_funcRes(username)), root.destroy()]) #command=part(f_cadastrar, root)
    btnAddProduto.place(relx=0.5, rely=0.8, anchor="center")


    btnVoltarMenu = Button(root, text="Voltar ao Menu", command= root.destroy)
    btnVoltarMenu.place(relx=0.5, rely=0.9, anchor="center")

    root.mainloop()

def f_menu_cliente(username):
    root = Tk()
    root.geometry('300x500')
    root.title("Menu Cliente")

    label_menu_cliente = Label(root,text="MENU CLIENTE")
    label_menu_cliente.place(relx= 0.5,rely= 0.1,anchor="center")

    addCompra = Button(root, text="Fazer Compra", background="#808080", foreground="black", command= lambda: f_tela_compra(username))
    addCompra.place(relx=0.5, rely=0.4, anchor="center")

    edit = Button(root, text="Editar Informa????o", background="#808080", foreground="black",command= lambda: f_tela_pessoa(2,1,username))
    edit.place(relx=0.5, rely=0.5, anchor="center")

    delete = Button(root, text="Excluir Cadastro", background="#808080", foreground="black",command= lambda: [f_excluir_cliente(username), root.destroy(), main()])
    delete.place(relx=0.5, rely=0.6, anchor="center")

    sair = Button(root, text="Sair", background="#808080", foreground="black", command= lambda: [root.destroy(), main()])
    sair.place(relx=0.5, rely=0.7, anchor="center")

    root.mainloop()

def f_menu_entregador(username):
    root = Tk()
    root.geometry('300x500')
    root.title("Menu Entregador")

    label_menu_entregador = Label(root, text="MENU ENTREGADOR")
    label_menu_entregador.place(relx=0.5, rely=0.1, anchor="center")

    addEntrega = Button(root, text="Entrega", background="#808080", foreground="black", command= lambda: f_tela_entrega(username))
    addEntrega.place(relx=0.5, rely=0.4, anchor="center")

    edit = Button(root, text="Editar Informa????es", background="#808080", foreground="black",command= lambda: f_tela_pessoa(1,1,username))
    edit.place(relx=0.5, rely=0.5, anchor="center")

    sair = Button(root, text="Sair", background="#808080", foreground="black", command= lambda: [root.destroy(), main()])
    sair.place(relx=0.5, rely=0.6, anchor="center")

    root.mainloop()


def f_menu_funcionario(username):
    root = Tk()
    root.geometry('300x500')
    root.title("Menu Funcionario")

    label_menu_funcionario = Label(root, text="MENU FUNCIONARIO")
    label_menu_funcionario.place(relx=0.5, rely=0.1, anchor="center")

    addCP = Button(root, text="Cadastrar Produtos", background="#808080", foreground="black", command= lambda: f_produto(username))
    addCP.place(relx=0.5, rely=0.4, anchor="center")

    addEP = Button(root, text="Editar Produto", background="#808080", foreground="black", command=lambda: f_editar_produto(username))
    addEP.place(relx=0.5, rely=0.5, anchor="center")

    '''addCF = Button(root, text="Cadastrar Funcion??rio", background="#808080", foreground="black", command=lambda: f_tela_pessoa(0, 2, username = None))
    addCF.place(relx=0.5, rely=0.6, anchor="center")'''

    edit = Button(root, text="Editar Informa????o", background="#808080", foreground="black",command= lambda: f_tela_pessoa(0,1,username))
    edit.place(relx=0.5, rely=0.6, anchor="center")

    sair = Button(root, text="Sair", background="#808080", foreground="black", command= lambda: [root.destroy(), main()])
    sair.place(relx=0.5, rely=0.7, anchor="center")

    root.mainloop()

def f_validaUserT(username, senha, label_confirmarcao, root):
    if(len(username) < 25 and len(senha) < 25):
        res = f_validaUser(username, senha, label_confirmarcao)

        if(res == 0):
            root.destroy()
            f_menu_funcionario(username)
        elif(res == 1):
            root.destroy()
            f_menu_entregador(username)
        elif(res == 2):
            root.destroy()
            f_menu_cliente(username)
    else:
        label_confirmarcao.config(text="O m??ximo de caracteres\n?? 25. :(", foreground = "RED")

def main():
    root = Tk()
    root.geometry('300x500')
    root.title("Login")

    label_menu = Label(root, text="LOGIN")
    label_menu.place(relx=0.5, rely=0.1, anchor="center")

    label_nc = Label(root,text="Ainda n??o ?? cadastrado?")
    label_nc.place(relx = 0.5, rely = 0.65, anchor="center")

    label_es = Label(root,text="Esqueceu sua senha?")
    label_es.place(relx = 0.5, rely = 0.8, anchor="center")

    label_username = Label(root, text="Username")
    label_username.place(relx= 0.16,rely=0.3,anchor="center")

    label_senha = Label(root,text="Senha")
    label_senha.place(relx=0.2,rely=0.4,anchor="center")

    username = StringVar()
    texto_username = Entry(root,textvariable = username, width = 20)
    texto_username.place(relx= 0.5, rely= 0.3, anchor="center")

    senha = StringVar()
    texto_senha = Entry(root,textvariable = senha,show="*",width=20)
    texto_senha.place(relx= 0.5, rely= 0.4, anchor ="center")

    label_confirmarcao = Label(root)
    label_confirmarcao.place(relx=0.5, rely=0.55, anchor="center")

    Entrar = Button(root, text="Entrar",background="#808080", foreground="black", command=lambda: [f_validaUserT(username.get(), senha.get(), label_confirmarcao, root)])
    Entrar.place(relx=0.5, rely=0.485, anchor="center")

    Cadastro = Button(root, text="Cadastrar-se",background="#808080", foreground="black", command= lambda:[root.destroy(), f_tela_pessoa(2, 0, username = None)])
    Cadastro.place(relx=0.5,rely=0.7,anchor="center")

    Esqueceu = Button(root, text="Alterar",background="#808080", foreground="black", command= lambda:[root.destroy(), f_tela_senha()])
    Esqueceu.place(relx=0.5,rely=0.85,anchor="center")

    root.mainloop()

    return 0
if __name__ == "__main__": main()