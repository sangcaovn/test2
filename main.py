from http.server import HTTPServer
from database import create_merchant_account
from http_server import ServiceHandler
# import create_table_account
import uuid
import jwt_data
import psycopg2
import os

if __name__== "__main__":

    #Server Initialization
    print ("server is running on port 5000 !!!")
    server = HTTPServer(('127.0.0.1',5000), ServiceHandler)
    server.serve_forever()