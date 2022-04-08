import psycopg2

def open():
    return psycopg2.connect(
        database="test2", user='admin', password='admin', host='127.0.0.1', port= '5432'
    )
