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
    """dados = {
        "descricao": ['vila velha', 'serra', 'vitória']
    }
    df = pd.DataFrame(dados)
    bairro = "BAIRRO"
    for i in df.index:
        sql = f'''INSERT INTO {bairro}(descricao)
                VALUES('%s') RETURNING codigo;
                '''%(df['descricao'][i])
        f_inserirBairro(sql)"""
    l = ['abacaxi', 'uva', 'morango', 'pera']
    v = str()
    for j in range(len(l)):
        if(j < len(l)-1):
            v += f"df['{l[j]}'][i],"
        else:
            v += f"df['{l[j]}'][i]"
    print(v)
    z = str()
    h = "'%s',"
    for n in range(len(l)):
        if(j < len(l)-1):
            z += h
        else:
            z += h
    z = z[0:len(z)-1]
    print(z)
    te = """'abacaxi', 'uva', 'morango', 'pera'"""
    sql = f"""'''INSERT INTO BAIRRO({te})
                VALUES({z}) RETURNING codigo;
                '''%({v})"""
    print(sql)
    return 0

if __name__ == '__main__':main()