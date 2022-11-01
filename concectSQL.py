import psycopg2
from config import config

def cursor():
    conn = None
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()

    return cur

def main():
	
    cur = cursor()
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    print(db_version)
    cur.close()
    return 0

if __name__ == '__main__':main()