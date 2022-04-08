from http.server import BaseHTTPRequestHandler
import json

from ewallet import Ewallet
from jwt_data import JwtData
from urllib.parse import urlparse

from url_type import UrlType

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
    # Tao 	
    def do_POST(self):
        if(self.path==UrlType.create_merchant.value):
            data=ServiceHandler.get_data_sent(self)
            Ewallet.create_merchant(data)
        elif(self.path==UrlType.create_personal_issuer.value):
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
        elif(self.path==UrlType.create_transaction.value):
            data=ServiceHandler.get_data_sent(self)
            Ewallet.create_transaction(data)
        elif(self.path==UrlType.confirm_transaction.value):
            Ewallet.confirm_transaction()
        elif(self.path==UrlType.verify_transaction.value):
            Ewallet.verify_transaction()
        elif(self.path==UrlType.cancel_transaction.value):
            Ewallet.cancel_transaction()
        else:
            path = urlparse(self.path).path
            path=path.strip().split('/')
            if(path[1] and path[3] and path[1]=="account" and path[3]=="topup"):
                if not path[2]:
                    self.send_response(404)
                    return

                data=ServiceHandler.get_data_sent(self)
                if not data:
                    self.send_response(403)
                    return

                # check account do topup must be issuer
                res=Ewallet.get_account_type_by_account_id(path[2])
                if not res and res[0]!="issuer":
                    self.send_response(403)
                    self.send_header('Content-type', 'text/json')
                    self.end_headers()
                    output_json = json.dumps({"message":"failed"})
                    self.wfile.write(output_json.encode('utf-8'))
                    return
                
                # save to database
                res=Ewallet.do_topup(data)
                if res is False:
                    self.send_response(501)
                    return

                self.send_response(200)
                self.send_header('Content-type', 'text/json')
                self.end_headers()
                output_json = json.dumps({"message":"ok"})
                self.wfile.write(output_json.encode('utf-8'))
            else:
                self.send_response(404)
	