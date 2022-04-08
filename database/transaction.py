import psycopg2
from .connection import open


def create_transaction():
    try:
        connection = open()
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (%s,%s,%s)"""
        record_to_insert = (5, 'One Plus 6', 950)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def confirm_transaction(token, transaction_id):
    try:
        connection = open()

        cursor = connection.cursor()

        print("Table Before updating record ")
        sql_select_query = """select * from mobile where id = %s"""
        cursor.execute(sql_select_query, (accountId,))
        record = cursor.fetchone()
        print(record)

        # Update single record now
        sql_update_query = """Update mobile set price = %s where id = %s"""
        cursor.execute(sql_update_query, (price, accountId))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

        print("Table After updating record ")
        sql_select_query = """select * from mobile where id = %s"""
        cursor.execute(sql_select_query, (accountId,))
        record = cursor.fetchone()
        print(record)

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def verify_transaction(token, transaction_id):
    try:
        connection = open()

        cursor = connection.cursor()

        print("Table Before updating record ")
        sql_select_query = """select * from mobile where id = %s"""
        cursor.execute(sql_select_query, (accountId,))
        record = cursor.fetchone()
        print(record)

        # Update single record now
        sql_update_query = """Update mobile set price = %s where id = %s"""
        cursor.execute(sql_update_query, (price, accountId))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

        print("Table After updating record ")
        sql_select_query = """select * from mobile where id = %s"""
        cursor.execute(sql_select_query, (accountId,))
        record = cursor.fetchone()
        print(record)

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def cancel_transaction(token, transaction_id):
    try:
        connection = open()

        cursor = connection.cursor()

        print("Table Before updating record ")
        sql_select_query = """select * from mobile where id = %s"""
        cursor.execute(sql_select_query, (accountId,))
        record = cursor.fetchone()
        print(record)

        # Update single record now
        sql_update_query = """Update mobile set price = %s where id = %s"""
        cursor.execute(sql_update_query, (price, accountId))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

        print("Table After updating record ")
        sql_select_query = """select * from mobile where id = %s"""
        cursor.execute(sql_select_query, (accountId,))
        record = cursor.fetchone()
        print(record)

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")