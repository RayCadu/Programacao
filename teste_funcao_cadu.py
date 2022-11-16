from conectSQL import *


def f_cadastrar_pessoas(nome,cpf,tel,username,senha,logradouro,numero,cep,boxtl,boxcidade,boxbairro,complemento, tpPessoa, teste):
    
    dicp = {}
    dicp["username"] = username
    dicp["nome"] = nome
    dicp["telefone"] = tel
    dicp["cpf"] = cpf
    dicp["senha"] = senha
    dicp["fk_endereco_codigo"] = f_cadastrar_endereco(cep,logradouro,numero,boxbairro,boxcidade,boxtl,complemento, teste)
    f_inserirDados("PESSOA",dicp,"username")

    if(tpPessoa == 0):
        dicC = {}
        dicC["fk_pessoa_username"] = username
        f_inserirDados("FUNCIONARIO", dicC, "codigo")

    elif(tpPessoa == 1):
        dicC = {}
        dicC["fk_pessoa_username"] = username
        f_inserirDados("ENTREGADOR", dicC, "codigo")

    elif(tpPessoa == 2):
        dicC = {}
        dicC["fk_pessoa_username"] = username
        f_inserirDados("CLIENTE", dicC, "codigo")
    
    return 0

def f_cadastrar_endereco(cep,logradouro,numero,boxbairro,boxcidade,boxtl,complemento, teste):
    dice = {}
    dice["cep"] = cep
    dice["logradouro"] = logradouro
    dice["numero"] = numero
    if(teste[2] == 0):
        dice["bairro"] = f_cadastrar_bairro(boxbairro)
    else:
        dice["bairro"] = teste[2]

    if(teste[1] == 0):
        dice["cidade"] = f_cadastrar_cidade(boxcidade)
    else:
        dice["cidade"] = teste[1]

    if(teste[0] == 0):
        dice["tipo_logradouro"] = f_cadastrar_tl(boxtl)
    else:
        dice["tipo_logradouro"] = teste[0]
        
    dice["complemento"] = complemento


    return f_inserirDados("endereco",dice,"codigo")

def f_cadastrar_bairro(boxbairro):
    dicb = {}
    dicb["descricao"] = boxbairro
  
    return str(f_inserirDados("BAIRRO",dicb,"codigo"))

def f_cadastrar_cidade(boxcidade):
    dicc = {}
    dicc["descricao"] = boxcidade
    
    return str(f_inserirDados("CIDADE",dicc,"codigo"))

def f_cadastrar_tl(boxtl):
    dictl = {}
    dictl["descricao"] = boxtl
    
    return str(f_inserirDados("TIPO_LOGRADOURO",dictl,"codigo"))
    
    
def f_cadastrar_produto(nome,tpProduto, valor, descricao, new, cod_func):
    dicP = {}
    dicP["nome"] = nome
    dicP["descricao"] = descricao
    dicP["valor"] = valor
    if(new == 0):
        dicP["fk_tipo_produto_tipo_produto_pk"] = f_cadastar_tpProduto(tpProduto)
    else:
        dicP["fk_tipo_produto_tipo_produto_pk"] = new

    cod_produto = f_inserirDados("PRODUTO", dicP, "codigo")

    dicAdm = {}
    dicAdm['fk_funcionario_codigo'] = cod_func
    dicAdm['fk_produto_codigo'] = cod_produto

    f_inserirDados("ADMINISTRA", dicAdm, "fk_produto_codigo")



def f_cadastar_tpProduto(tpProduto):
    dicTp = {}
    dicTp["descricao"] = tpProduto

    return f_inserirDados("TIPO_PRODUTO", dicTp, "tipo_produto_pk")

def f_validaUser(username, senha, label):
    users = f_retornaInfo(['username', 'senha'], "PESSOA")

    for i in users:
        if(username in i and senha in i):
            #label.config(text="Usuário no sistema", foreground="green")
            tela = f_verificaTela(username)
            return tela
        else:
            label.config(text="Usuário não está no sistema", foreground="red")
            tela = None

    if(len(users) == 0):
        label.config(text="Nenhum usuário cadastrado no sistema", foreground="red")
        tela = None
    
    return tela

def f_verificaTela(user):
    users = f_retornaInfo(['fk_pessoa_username'], "CLIENTE")
    for i in users:
        if (user in i):
            tela = 2

    users = f_retornaInfo(['fk_pessoa_username'], "ENTREGADOR")
    for i in users:
        if (user in i):
            tela = 1

    users = f_retornaInfo(['fk_pessoa_username'], "FUNCIONARIO")
    for i in users:
        if (user in i):
            tela = 0
    
    return tela

def f_editar_pessoa(username):
    info = f_retornaEspc(['nome','telefone','cpf','username','senha','fk_endereco_codigo'],'PESSOA',username, 'username')
    return info

#cep,logradouro,numero,boxbairro,boxcidade,boxtl,complemento
def f_editar_endereco(fk_endereco_codigo):
    info = f_retornaEspc(['cep','logradouro','numero','bairro','cidade','tipo_logradouro','complemento'],'endereco',fk_endereco_codigo, 'codigo')
    return info

def f_retornaLista(t):
    p =list()
    for i in  t:
        p.append(i[0])
    return p

def f_codigo(boxtl, tpLg):
    print(tpLg)
    try:
        tp = tpLg.index(boxtl.get())
    except ValueError:
        tp = 0
    print(tp)
    return tp

def f_funcRes(username):
    cod = f_retornaEspc(['codigo'], 'FUNCIONARIO', username, 'fk_pessoa_username')
    cod = cod[0][0]

    return cod