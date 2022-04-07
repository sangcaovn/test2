import sqlite3

def create_merchant_account(item):
    conn = sqlite3.connect('test3.db')
    c = conn.cursor()
    c.execute('insert into tablename values (?,?,?)', item)