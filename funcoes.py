from concectSQL import f_inserirDados


def f_cadastrar_pessoa(nome,cpf,tel,username,senha,logradouro,numero,cep,boxtl,boxcidade,boxbairro,complemento):
    dicp = {}
    dicp["username"] = username.get()
    dicp["nome"] = nome.get()
    dicp["tel"] = tel.get()
    dicp["cpf"] = cpf.get()
    dicp["senha"] = senha.get()
    dicp["fk_endereco_codigo"] = f_cadastrar_endereco(cep,logradouro,numero,boxbairro,boxcidade,boxtl,complemento)
    f_inserirDados("PESSOA",dicp,"username")

def f_cadastrar_endereco(cep,logradouro,numero,boxbairro,boxcidade,boxtl,complemento):
    dice = {}
    dice["cep"] = cep.get()
    dice["logradouro"] = logradouro.get()
    dice["numero"] = numero.get()
    dice["bairro"] = f_cadastrar_bairro(boxbairro)
    dice["cidade"] = f_cadastrar_cidade(boxcidade)
    dice["tipo_logradouro"] = f_cadastrar_tl(boxtl)
    dice["complemento"] = complemento.get()
    f_inserirDados("endereco",dice,"codigo")

def f_cadastrar_bairro(boxbairro):
    dicb = {}
    dicb["descricao"] = boxbairro.get()
    f_inserirDados("BAIRRO",dicb,"codigo")

def f_cadastrar_cidade(boxcidade):
    dicc = {}
    dicc["descricao"] = boxcidade.get()
    f_inserirDados("CIDADE",dicc,"codigo")

def f_cadastrar_tl(boxtl):
    dictl = {}
    dictl["descricao"] = boxtl.get()
    f_inserirDados("TIPO_LOGRADOURO",dictl,"codigo")
