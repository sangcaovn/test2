import psycopg2

def create_merchant_account(item):
    conn = psycopg2.connect('dbname=test12_db user=admin password=admin port=5432')
    c = conn.cursor()
    c.execute('insert into tablename values (?,?,?)', item)