from http.server import HTTPServer
from http_server import ServiceHandler

if __name__== "__main__":
    #Server Initialization
    print ("server is running on port 8080 !!!")
    server = HTTPServer(('127.0.0.1',8080), ServiceHandler)
    server.serve_forever()