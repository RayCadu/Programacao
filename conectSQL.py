import psycopg2
from config import config

def f_conexao():
    conn = None
    params = config()
    conn = psycopg2.connect(**params)

    return conn

def f_verifica(a):
    if(type(a) == type(str())):
        return 1
    else:
        return 0

def f_criarInstrucao(table_name, dic, pk):
    l = str()
    z = str()
    for g,j in dic.items():
        l += g + ","

        if(f_verifica(j) == 1):
            z += "'" + str(j) + "'" + ","
        else:
            z += str(j) + ","
         
    l = l[:len(l)-1]
    z = z[:len(z)-1]
    sql = f"""INSERT INTO {table_name}({l})
            VALUES({z}) RETURNING {pk};
            """
    return sql


def f_inserirDados(table_name, dic, pk):
    sql = f_criarInstrucao(table_name, dic, pk)

    conn = f_conexao()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return id
    except(Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cur.close()
        return None

def f_retornaInfo(campos, nome_tabela):
    ca = str()
    for i in campos:
        ca += i + ","
    ca = ca[:len(ca)-1]

    sql = f""" SELECT {ca} FROM {nome_tabela}"""
    conn = f_conexao()
    cur = conn.cursor()
    cur.execute(sql)

    recset = cur.fetchall()
    values = list()

    for rec in recset:
        values.append(rec)

    cur.close()
    conn.close()

    return values

def f_retornaEspc(campos, nome_tabela,username, campo_condi):
    ca = str()
    for i in campos:
        ca += i + ","
    ca = ca[:len(ca)-1]

    sql = f""" SELECT {ca} FROM {nome_tabela} WHERE {campo_condi} = '{username}'"""
    conn = f_conexao()
    cur = conn.cursor()
    cur.execute(sql)

    recset = cur.fetchall()
    values = list()

    for rec in recset:
        values.append(rec)

    cur.close()
    conn.close()

    return values

def f_retornar_info_compra(cod_compra):
    sql = f"""select pessoa.nome, pessoa.telefone, endereco.cep, endereco.logradouro, endereco.numero, endereco.complemento, bairro.descricao, cidade.descricao, tipo_logradouro.descricao
    from pessoa
    inner join endereco
    on endereco.codigo = pessoa.fk_endereco_codigo
    inner join bairro
    on bairro.codigo = endereco.bairro
    inner join cidade
    on cidade.codigo = endereco.cidade
    inner join tipo_logradouro
    on tipo_logradouro.codigo = endereco.tipo_logradouro
    inner join cliente
    on pessoa.username = cliente.fk_pessoa_username
    inner join cliente_compra
    on cliente.codigo = cliente_compra.fk_cliente_codigo
    inner join compra
    on compra.codigo = cliente_compra.fk_compra_codigo
    where compra.codigo = {cod_compra};"""

    conn = f_conexao()
    cur = conn.cursor()
    cur.execute(sql)

    recset = cur.fetchall()
    values = list()

    for rec in recset:
        values.append(rec)

    cur.close()
    conn.close()

    return(values)

def f_update_compra(cod, compra):
    sql = f"""update compra set fk_entregador_codigo = {cod} where codigo = {compra}"""
    conn = f_conexao()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cur.close()

    sql = f"""update compra set estado = 'Em entrega' where codigo = {compra}"""
    conn = f_conexao()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cur.close()