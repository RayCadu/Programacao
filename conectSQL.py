import psycopg2
#import pandas as pd
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
