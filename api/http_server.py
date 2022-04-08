from http.server import BaseHTTPRequestHandler
import json
from enum.url_type import UrlType

from ewallet import Ewallet
<<<<<<< HEAD:http_server.py
from jwt_data import JwtData
from urlEnum import UrlEnum
=======
>>>>>>> cab084999412ef449688c83811ab24bc690acc17:api/http_server.py
from urllib.parse import urlparse

#Defining a HTTP request Handler class
class ServiceHandler(BaseHTTPRequestHandler):

	#sets basic headers for the server
    def _set_headers(self):
        # 1. gui response 200 va content-type la text/json
        self.send_response(200)
        self.send_header('Content-type','text/json')
        # 2. doc do dai cua headers ra kieu int
        length = int(self.headers['Content-Length'])
        # 3. doc file bang lenh rfile read
        #reads the contents of the request
        content = self.rfile.read(length)
        # 4. tao string cho content vua doc tu file, loai bo 
        temp = str(content).strip('b\'')
        # 5. goi ham end headers
        self.end_headers()
        # 6. tra lai kieu string
        return temp

    def get_data_sent(self):
        content_length = int(self.headers['Content-Length'])
        if content_length:
            input_json = self.rfile.read(content_length)
            input_data = json.loads(input_json)
        else:
            input_data = None
        return input_data
    
    # Tao controller cho 1 url 
    def do_GET(self):
        # Lay path cua phuong thuc do get
        path = urlparse(self.path).path
        # Lay ra dau /
        path=path.strip().split('/')
        # Kiem tra trong URL co account va token
        if(path[1] and path[3] and path[1]=="account" and path[3]=="token"):
            self.send_response(200)
            self.send_header('Content-type','text/json')
            self.end_headers()
<<<<<<< HEAD:http_server.py
            # Tao token cho ewallet??
            # token = Ewallet.get_token_by_account(path[2])
            if not path[2]:
                self.send_response(404)
            api_key=Ewallet.get_api_key_by_account_id(path[2])
            if not api_key:
                self.send_response(404)
            
            if api_key[0]:
                api_key= api_key[0]
            else:
                api_key=api_key[1]

            print ("api_key====",api_key)
            token=JwtData.encode_auth_token({"account_id":path[2]},api_key)
            print ("token>>>>>>>>",str(token))
            self.send_response(200)
            self.send_header('Content-type', 'text/json')
            self.end_headers()
            output_json = json.dumps({"token":token})
            self.wfile.write(output_json.encode('utf-8'))
=======
            #prints all the keys and values of the json file
            self.wfile.write(json.dumps({}).encode())
>>>>>>> cab084999412ef449688c83811ab24bc690acc17:api/http_server.py
        else:
            self.send_response(404)

    # Tao 	
    def do_POST(self):
<<<<<<< HEAD:http_server.py

        if(self.path==UrlEnum.create_merchant.value):
            data=ServiceHandler.get_data_sent(self)
            Ewallet.create_merchant(data)
        elif(self.path==UrlEnum.create_personal_issuer.value):
            data=ServiceHandler.get_data_sent(self)
            if data:
                res= Ewallet.create_personal_issuer(data)
                self.send_response(200)
                self.send_header('Content-type', 'text/json')
                self.end_headers()
                output_json = json.dumps({"message":"saved ok"})
                self.wfile.write(output_json.encode('utf-8'))
            else:
                self.send_response(404) 
        elif(self.path==UrlEnum.create_transaction.value):
            data=ServiceHandler.get_data_sent(self)
            Ewallet.create_transaction(data)
        elif(self.path==UrlEnum.confirm_transaction.value):
=======
        if(self.path==UrlType.create_merchant.value):
            content_len = int(self.headers.get('Content-Length'))
            post_body = self.rfile.read(content_len)
            print ("post_body >>>>>>>>>",post_body)
            Ewallet.create_merchant()
        elif(self.path==UrlType.create_personal_issuer.value):
            Ewallet.create_personal_issuer()
        elif(self.path==UrlType.create_transaction.value):
            Ewallet.create_transaction()
        elif(self.path==UrlType.confirm_transaction.value):
>>>>>>> cab084999412ef449688c83811ab24bc690acc17:api/http_server.py
            Ewallet.confirm_transaction()
        elif(self.path==UrlType.verify_transaction.value):
            Ewallet.verify_transaction()
        elif(self.path==UrlType.cancel_transaction.value):
            Ewallet.cancel_transaction()
        else:
            path = urlparse(self.path).path
            path=path.strip().split('/')
            if(path[1]=="account" and path[3]=="topup"):
                param=path[2]
                # Phai truyen vao user id de generate token
                Ewallet.get_token_by_account(param)
            else:
                self.send_response(404)

<<<<<<< HEAD:http_server.py
        # temp = self._set_headers()
        # key=0
        # # print (temp)
        # #getting key and value of the data dictionary
        # for key,value in data.items():
        #     pass
        # index = int(key)+1
        # data[str(index)]=str(temp)
        # # print (str(temp))
        # #write the changes to the json file
        # with open("db.json",'w+') as file_data:
        #     json.dump(data,file_data)
=======

        temp = self._set_headers()
        key=0
        # print (temp)
        #getting key and value of the data dictionary
        for key,value in {}.items():
            pass
        index = int(key)+1
        {}[str(index)]=str(temp)
        # print (str(temp))
        #write the changes to the json file
        with open("db.json",'w+') as file_data:
            json.dump({},file_data)
>>>>>>> cab084999412ef449688c83811ab24bc690acc17:api/http_server.py
        #self.wfile.write(json.dumps(data[str(index)]).encode())
	