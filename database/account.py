import json
import psycopg2
from .connection import open

def get_token(account_id: str):
    pass

def topup(account_id: str, json_data: json):
    pass

def add_new_account(json_data):
    try:
        connection = open()
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (%s,%s,%s)"""
        record_to_insert = json_data #(5, 'One Plus 6', 950)
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


def merchant_sigup(json_data):
    try:
        connection = open()
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO merchant (MERCHANT_ID, MERCHANT_NAME, MERCHANT_URL) VALUES (%s,%s,%s)"""
        record_to_insert = json_data #(5, 'One Plus 6', 950)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into merchant table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def update_account(accountId, json_data):
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

# id = 3
# price = 970
# updateTable(id, price)