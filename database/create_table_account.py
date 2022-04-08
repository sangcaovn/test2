import psycopg2

if __name__== "__create_table_account__":
    try:
        postgresConnection = psycopg2.connect('dbname=test12_db user=admin password=admin port=5432')
        postgres_create_table_query = '''CREATE TABLE account (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    email text NOT NULL UNIQUE,
                                    joining_date datetime,
                                    salary REAL NOT NULL);'''

        cursor = postgresConnection.cursor()
        print("Successfully Connected to Postgres")
        cursor.execute(postgres_create_table_query)
        postgresConnection.commit()
        print("Postgres table created")

        cursor.close()

    except psycopg2.Error as error:
        print("Error while creating a postgres table", error)
    finally:
        if postgresConnection:
            postgresConnection.close()
            print("Postgres connection is closed")