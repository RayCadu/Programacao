from conectSQL import f_inserirDados


def f_cadastrar_pessoa(nome,cpf,tel,username,senha,logradouro,numero,cep,boxtl,boxcidade,boxbairro,complemento):
    dicp = {}
  
    dicp["username"] = username
    dicp["nome"] = nome
    dicp["telefone"] = tel
    dicp["cpf"] = cpf
    dicp["senha"] = senha
    dicp["fk_endereco_codigo"] = f_cadastrar_endereco(cep,logradouro,numero,boxbairro,boxcidade,boxtl,complemento)
    f_inserirDados("PESSOA",dicp,"username")

def f_cadastrar_endereco(cep,logradouro,numero,boxbairro,boxcidade,boxtl,complemento):
    dice = {}
    dice["cep"] = cep
    dice["logradouro"] = logradouro
    dice["numero"] = numero
    dice["bairro"] = f_cadastrar_bairro(boxbairro)
    dice["cidade"] = f_cadastrar_cidade(boxcidade)
    dice["tipo_logradouro"] = f_cadastrar_tl(boxtl)
    dice["complemento"] = complemento
    print(dice)
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
    
    
