import psycopg2
import pandas as pd
from config import config

def f_conexao():
    conn = None
    params = config()
    conn = psycopg2.connect(**params)

    return conn

def f_inserirBairro(sql):
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
        return 1
    cur.close()

def main():  
    dados = {
        "descricao": ['vila velha', 'serra', 'vitória']
    }
    df = pd.DataFrame(dados)
    for i in df.index:
        sql = '''INSERT INTO BAIRRO(descricao)
                VALUES('%s') RETURNING codigo;
                '''%(df['descricao'][i])
        f_inserirBairro(sql)

    return 0

if __name__ == '__main__':main()