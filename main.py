from http.server import HTTPServer
<<<<<<< HEAD
from database import create_merchant_account
from http_server import ServiceHandler
# import create_table_account
import uuid
import jwt_data
import psycopg2
import os
=======

from api.http_server import ServiceHandler
>>>>>>> cab084999412ef449688c83811ab24bc690acc17

if __name__== "__main__":

    #Server Initialization
    print ("server is running on port 5000 !!!")
    server = HTTPServer(('127.0.0.1',5000), ServiceHandler)
    server.serve_forever()