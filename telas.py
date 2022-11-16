from tkinter import *
from funcoes import *
from tkinter.ttk import Combobox
from tkinter.ttk import Entry

fk_endereco_codigo = 0

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

def f_tela_cliente_dinheiro():
    root = Toplevel()
    root.geometry('300x500')
    root.title('Cliente')

    #label
    label_cliente = Label(root,text = "CLIENTE")
    label_codigo = Label(root,text = "CÓDIGO:")
    label_nome = Label(root,text = "NOME:")
    label_telefone = Label(root, text ="TELEFONE:")
    label_fp = Label(root,text="FORMA\nDE PAGAMENTO", background= 'black', foreground= 'white')
    label_pc = Label(root,text = "PAGAMENTO NO\nCARTÃO")
    label_dinheiro = Label(root,text = "DINHEIRO")
    label_pix = Label(root,text = "PIX")

    #textos
    codigo = StringVar()
    texto_codigo = Entry(root, textvariable = codigo, width=20)
    nome = StringVar()
    texto_nome = Entry(root, textvariable = nome, width=20)
    telefone = StringVar()
    texto_telefone = Entry(root, textvariable = telefone, width=20)

    #checkbutton
    checkPC = Checkbutton(root,text = "SIM", onvalue = 1, offvalue = 0)
    checkDINHEIRO = Checkbutton(root,text = "SIM",onvalue = 1, offvalue = 0)
    checkPIX = Checkbutton(root,text = "SIM",onvalue = 1, offvalue = 0)

    #botões
    addAE = Button(root,text ="Adicionar endereço")
    addTP = Button(root,text = "Voltar a tela pessoa")

    #posicionamento label
    label_cliente.place(relx = 0.5, rely = 0.05, anchor='center')
    label_codigo.place(relx = 0.1, rely = 0.1, anchor = 'w')
    label_nome.place(relx = 0.1, rely = 0.2, anchor = 'w')
    label_telefone.place(relx = 0.05, rely = 0.3, anchor = 'w')
    label_fp.place(relx = 0.01, rely = 0.4, anchor = 'w')
    label_pc.place(relx = 0.1, rely =0.5, anchor = 'w')
    label_dinheiro.place(relx = 0.15, rely =0.6, anchor = 'w')
    label_pix.place(relx = 0.2, rely = 0.7, anchor = 'w')

    #posicionamento textos
    texto_codigo.place(relx = 0.3, rely = 0.1 , anchor = 'w')
    texto_nome.place(relx = 0.3 , rely = 0.2 , anchor = 'w')
    texto_telefone.place(relx = 0.3, rely = 0.3 , anchor = 'w')

    #posicionamento checkbutton
    checkPC.place(relx = 0.5,rely = 0.5,anchor = 'w')
    checkDINHEIRO.place(relx = 0.5,rely = 0.6,anchor = 'w')
    checkPIX.place(relx = 0.5,rely = 0.7,anchor = 'w')

    #posicionamento botões
    addAE.place(relx= 0.5,rely= 0.8,anchor='center')
    addTP.place(relx= 0.5,rely= 0.9,anchor='center')


    root.mainloop()


def f_tela_compra(username):
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
    comboBoxProduto['values'] = ('teste1', 'teste2', 'teste3')
    comboBoxProduto.place(relx=0.3, rely=0.25, anchor="w")

    label_nome = Label(root, text="Quantidade")
    label_nome.place(relx=0.06, rely=0.35, anchor="w")

    qtd = StringVar()
    texto_qtd = Entry(root, textvariable= qtd, width=30)
    texto_qtd.place(relx=0.3, rely=0.35, anchor="w")

    #label_nome = Label(root, text="Entregador")
    #label_nome.place(relx=0.5, rely=0.45, anchor="center")

    #entregador = StringVar()
    #comboBoxEntregador = Combobox(root, textvariable= entregador, height=0.5, width=24)
    #comboBoxEntregador['values'] = ('teste1', 'teste2', 'teste3')
    #comboBoxEntregador.place(relx=0.5, rely=0.50, anchor="center")

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


def f_tela_editar(username):
    root = Toplevel()
    root.geometry('300x500')
    root.title('Editar')

    #label
    label_editar = Label(root, text="EDITAR",background='black',foreground='white')
    label_cliente = Label(root, text="CLIENTE:")
    label_produto = Label(root, text="PRODUTO:")
    label_entregador = Label(root,text="ENTREGADOR:")

    #checkbutton

    checkC = Checkbutton(root, text="SIM",onvalue=1,offvalue=0)
    checkP = Checkbutton(root, text="SIM",onvalue=1,offvalue=0)
    checkE = Checkbutton(root, text="SIM",onvalue=1,offvalue=0)

    #combobox

    cpe = StringVar()
    ComboBoxCPE = Combobox(root,textvariable = cpe, width= 20)

    #botão
    addEI = Button(root,text="Editar informações")
    addM = Button(root,text="Voltar ao menu",command=root.destroy)

    #posicionamento label

    label_editar.place(relx= 0.5,rely= 0.1,anchor='center')
    label_cliente.place(relx= 0.35,rely= 0.2,anchor='center')
    label_produto.place(relx= 0.33,rely= 0.3,anchor='center')
    label_entregador.place(relx= 0.3,rely= 0.4,anchor='center')

    #posicionamento checkbutton

    checkC.place(relx=0.6,rely=0.2,anchor='center')
    checkP.place(relx=0.6,rely=0.3,anchor='center')
    checkE.place(relx=0.6,rely=0.4,anchor='center')

    #posicionamento combobox
    ComboBoxCPE.place(relx= 0.5,rely= 0.5,anchor='center')

    #posicionamento botão
    addEI.place(relx=0.5,rely=0.7,anchor='center')
    addM.place(relx=0.5,rely=0.8,anchor='center')

    root.mainloop()

def f_endereco(nome,cpf,tel,username,senha, tpPessoa,edit,fk_endereco_codigo):
    root = Toplevel()
    root.geometry('300x500')
    root.title('ENDEREÇO')

    #label
    label_endereco = Label(root, text= "ENDEREÇO",background='orange')
    label_nm = Label(root, text = "NOME DO CLIENTE:",background='black', foreground='white')
    label_tl = Label(root, text = "TIPO\nLOGRADOURO:",background='black', foreground='white')
    label_logradouro = Label(root, text = "LOGADOURO:",background='black', foreground='white')
    label_numero = Label(root, text = "NÚMERO:",background='black', foreground='white')
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

    #botão
    addE = Button(root, text ="Cadastrar pessoa",command = lambda: f_cadastrar_pessoas(nome.get(),cpf.get(),tel.get(),username.get(),senha.get(), logradouro.get(), numero.get(), cep.get(), complemento.get(), boxtl.get(), boxcidade.get(), boxbairro.get(), tpPessoa, teste = (f_codigo(boxtl.get(), tpLg), f_codigo(boxcidade.get(), cidade), f_codigo(boxbairro.get(), bairro))))
    btnVoltar = Button(root, text="Voltar para\ntela pessoa", command= root.destroy)

    if(edit == 1):
        info = f_editar_endereco(fk_endereco_codigo)
        texto_cep.insert(0,info[0][0])
        texto_logradouro.insert(0,info[0][1])
        texto_numero.insert(0,info[0][2])
        texto_complemento.insert(0,info[0][6])

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

    #posicionamento botão

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
    #botões
    if(edit == 0):
        addM = Button(root, text='Voltar ao menu',command =lambda:[root.destroy(), main()])
    else:
        addM = Button(root, text='Voltar ao menu',command =lambda:root.destroy())
    addE = Button(root,text='Adicionar endereço', command=lambda: f_endereco(nome,cpf,tel,user,senha, tpPessoa,edit,fk_endereco_codigo))
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
    if(edit == 1):
       info = f_editar_pessoa(username)
       texto_nome.insert(0,info[0][0])
       texto_tel.insert(0,info[0][1])
       texto_cpf.insert(0,info[0][2])
       texto_username.insert(0,info[0][3])
       texto_senha.insert(0,info[0][4])
       fk_endereco_codigo = info[0][5]
    

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

    #posicionamento botões
    addE.place(relx = 0.5, rely = 0.83, anchor = 'center')
    addM.place(relx = 0.5, rely = 0.93, anchor = 'center')
    

    root.mainloop()


def f_produto(username):
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

    cbTpProduto = StringVar()
    comboBoxTpProduto = Combobox(root, textvariable = cbTpProduto)
    tpProduto = f_retornaInfo(['descricao'], 'TIPO_PRODUTO')
    tpProduto = f_retornaLista(tpProduto)
    tpProduto.insert(0, '')
    comboBoxTpProduto['values'] = tpProduto
    comboBoxTpProduto.place(relx=0.3, rely=0.3, anchor="w")

    label_valor = Label(root, text="Preço")
    label_valor.place(relx=0.1, rely=0.4, anchor="w")

    valor = StringVar()
    texto_valor = Entry(root, textvariable=valor)
    texto_valor.place(relx=0.3, rely=0.4, anchor="w")

    label_valor = Label(root, text="Descrição")
    label_valor.place(relx=0.1, rely=0.6, anchor="w")

    texto_descricao = Text(root, height= 5, width=23)
    texto_descricao.place(relx=0.3, rely=0.6, anchor="w")

    btnAddProduto = Button(root, text="Cadastrar", command=lambda:[f_cadastrar_produto(nome.get(), cbTpProduto.get(), valor.get(), texto_descricao.get("1.0", END), new=f_codigo(cbTpProduto, tpProduto), cod_func= f_funcRes(username))]) #command=part(f_cadastrar, root)
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

    edit = Button(root, text="Editar Informação", background="#808080", foreground="black",command= lambda: f_tela_pessoa(2,1,username))
    edit.place(relx=0.5, rely=0.5, anchor="center")

    sair = Button(root, text="Sair", background="#808080", foreground="black", command= lambda: [root.destroy(), main()])
    sair.place(relx=0.5, rely=0.6, anchor="center")

    root.mainloop()

def f_menu_entregador(username):
    root = Tk()
    root.geometry('300x500')
    root.title("Menu Entregador")

    label_menu_entregador = Label(root, text="MENU ENTREGADOR")
    label_menu_entregador.place(relx=0.5, rely=0.1, anchor="center")

    addEntrega = Button(root, text="Entrega", background="#808080", foreground="black")
    addEntrega.place(relx=0.5, rely=0.4, anchor="center")

    edit = Button(root, text="Editar Informações", background="#808080", foreground="black",command= lambda: f_tela_pessoa(1,1,username))
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

    addCE = Button(root, text="Cadastrar Entregador", background="#808080", foreground="black", command=lambda: f_tela_pessoa(1, 0, username = None))
    addCE.place(relx=0.5, rely=0.5, anchor="center")

    addCF = Button(root, text="Cadastrar Funcionário", background="#808080", foreground="black", command=lambda: f_tela_pessoa(0, 0, username = None))
    addCF.place(relx=0.5, rely=0.6, anchor="center")

    edit = Button(root, text="Editar Informação", background="#808080", foreground="black",command= lambda: f_tela_pessoa(0,1,username))
    edit.place(relx=0.5, rely=0.7, anchor="center")

    sair = Button(root, text="Sair", background="#808080", foreground="black", command= lambda: [root.destroy(), main()])
    sair.place(relx=0.5, rely=0.8, anchor="center")

    root.mainloop()

def f_validaUserT(username, senha, label_confirmarcao, root):
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

def main():
    root = Tk()
    root.geometry('300x500')
    root.title("Login")

    label_menu = Label(root, text="LOGIN")
    label_menu.place(relx=0.5, rely=0.1, anchor="center")

    label_nc = Label(root,text="Ainda não é cadastrado!")
    label_nc.place(relx = 0.5, rely = 0.75, anchor="center")

    label_username = Label(root, text="Username")
    label_username.place(relx= 0.16,rely=0.3,anchor="center")

    label_senha = Label(root,text="Senha")
    label_senha.place(relx=0.2,rely=0.4,anchor="center")

    username = StringVar()
    texto_username = Entry(root,textvariable = username,width = 20)
    texto_username.place(relx= 0.5, rely= 0.3, anchor="center")

    senha = StringVar()
    texto_senha = Entry(root,textvariable = senha,show="*",width=20)
    texto_senha.place(relx= 0.5, rely= 0.4, anchor ="center")

    label_confirmarcao = Label(root)
    label_confirmarcao.place(relx=0.5, rely=0.55, anchor="center")

    Entrar = Button(root, text="Entrar",background="#808080", foreground="black", command=lambda: [f_validaUserT(username.get(), senha.get(), label_confirmarcao, root)])
    Entrar.place(relx=0.5, rely=0.485, anchor="center")

    Cadastro = Button(root, text="Cadastrar-se",background="#808080", foreground="black", command= lambda:[root.destroy(), f_tela_pessoa(2, 0, username = None)])
    Cadastro.place(relx=0.5,rely=0.8,anchor="center")

    root.mainloop()

    return 0
if __name__ == "__main__": main()