import psycopg2
import pandas as pd
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
    v = str()
    z = str()

    for g,j in dic.items():
        l += g + ","
        if(f_verifica(j[0]) == 1):
            z += "'" + str(j[0]) + "'" + ","
        else:
            z += str(j[0]) + ","
         
    l = l[:len(l)-1]
    #v = v[:len(v)-1]
    z = z[:len(z)-1]
    sql = f"""INSERT INTO {table_name}({l})
            VALUES({z}) RETURNING {pk};
            """
    print(sql)
    return sql


def f_inserirDados(table_name, dic, pk):

    sql = f_criarInstrucao(table_name, dic, pk)

    conn = f_conexao()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        id = cur.fetchone()[0]
        print(id)
        conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cur.close()
        #return 1
    cur.close()
    conn.close()


def main():

    pk = "codigo"
    table_name = "PRODUTO"
    dic ={}  
    dic['nome'] = ["Frango"]
    dic['descricao'] = ["Frango desfiado"]
    dic['valor'] = [25.00]
    dic['FK_tipo_produto_tipo_produto_PK'] = [2]

    f_inserirDados(table_name, dic, pk)

    return 0

if __name__ == '__main__':main()
