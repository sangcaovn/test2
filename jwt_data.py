import json
import jwt as jwt_token

class JwtData():

    @staticmethod
    def encode_auth_token(payload: json, key: str):
        try:
            print ("data------",payload,key)
            tmp= jwt_token.encode(
                payload,
                key,
                algorithm='HS256'
            )
            print ("test-------",tmp)
            return tmp
        except Exception as e:
            print (e)
            return e


    @staticmethod
    def decode_auth_token(auth_token: str, key: str):
        try:
            payload = jwt_token.decode(auth_token, key)
            return payload['sub']
        except jwt_token.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt_token.InvalidTokenError:
            return 'Invalid token. Please log in again.'