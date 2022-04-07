from http.server import BaseHTTPRequestHandler
import json

from ewallet import Ewallet
from urlEnum import UrlEnum
from urllib.parse import urlparse

#open json file and give it to data variable as a dictionary
with open("db.json") as data_file:
	data = json.load(data_file)

#Defining a HTTP request Handler class
class ServiceHandler(BaseHTTPRequestHandler):
	#sets basic headers for the server
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type','text/json')
        #reads the length of the Headers
        length = int(self.headers['Content-Length'])
        #reads the contents of the request
        content = self.rfile.read(length)
        temp = str(content).strip('b\'')
        self.end_headers()
        return temp
		
    def do_GET(self):
        path = urlparse(self.path).path
        path=path.strip().split('/')
        if(path[1]=="account" and path[3]=="token"):
            param=path[2]
            Ewallet.get_token_by_account()
            #defining all the headers
            self.send_response(200)
            self.send_header('Content-type','text/json')
            self.end_headers()
            #prints all the keys and values of the json file
            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_response(404)
		
    def do_POST(self):
        if(self.path==UrlEnum.create_merchant.value):
            Ewallet.create_merchant()
        elif(self.path==UrlEnum.create_personal_issuer.value):
            Ewallet.create_personal_issuer()
        elif(self.path==UrlEnum.create_transaction.value):
            Ewallet.create_transaction()
        elif(self.path==UrlEnum.confirm_transaction.value):
            Ewallet.confirm_transaction()
        elif(self.path==UrlEnum.verify_transaction.value):
            Ewallet.verify_transaction()
        elif(self.path==UrlEnum.cancel_transaction.value):
            Ewallet.cancel_transaction()
        else:
            path = urlparse(self.path).path
            path=path.strip().split('/')
            if(path[1]=="account" and path[3]=="topup"):
                param=path[2]
                Ewallet.get_token_by_account()
            else:
                self.send_response(404)


        temp = self._set_headers()
        key=0
        # print (temp)
        #getting key and value of the data dictionary
        for key,value in data.items():
            pass
        index = int(key)+1
        data[str(index)]=str(temp)
        # print (str(temp))
        #write the changes to the json file
        with open("db.json",'w+') as file_data:
            json.dump(data,file_data)
        #self.wfile.write(json.dumps(data[str(index)]).encode())
	