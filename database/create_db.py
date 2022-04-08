import psycopg2

if __name__== "__create_db__":

    try:
        postgresConnection = psycopg2.connect('dbname=test12_db user=admin password=admin port=5432')
        cursor = postgresConnection.cursor()
        print("Database created and Successfully Connected to Postgres")

        postgres_select_Query = "select postgres_version();"
        cursor.execute(postgres_select_Query)
        record = cursor.fetchall()
        print("Postgres Database Version is: ", record)
        cursor.close()

    except psycopg2.Error as error:
        print("Error while connecting to postgres", error)
    finally:
        if postgresConnection:
            postgresConnection.close()
            print("The Posgresql connection is closed")


