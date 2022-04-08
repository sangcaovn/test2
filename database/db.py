import psycopg2

class Db:
    
    def __init__(self, db_name):
        self.db_name = db_name  # database name
        self.conn = None        # connection

    def check_table_name(self,table_name):
        pass

    def check_database(self):
        ''' Check if the database exists or not '''

        try:
            print(f'Checking if {self.db_name} exists or not...')
            self.conn = psycopg2.connect(self.db_name, uri=True)
            print(f'Database exists. Succesfully connected to {self.db_name}')

        except psycopg2.OperationalError as err:
            print('Database does not exist')
            print(err)

    def close_connection(self):
        ''' Close connection to database '''

        if self.conn is not None:
            self.conn.close()