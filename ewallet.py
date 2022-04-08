<<<<<<< HEAD
import hashlib
import json
import os
import uuid
import psycopg2
import jwt_data
import transEnum

key = os.getenv('SECRET_KEY', "secret")
conn = psycopg2.connect("dbname=test12_db user=admin password=admin port=5432")
cur= conn.cursor()
=======
from database.account import add_new_account
>>>>>>> cab084999412ef449688c83811ab24bc690acc17

class Ewallet():
    # Tao merchant moi /merchant/signup
    def create_merchant(data):

        id = uuid.uuid4()
        account_id = data['account_id']
        merchant_id = data['merchant_id']
        merchant_name = data['merchant_name']
        api_key = data['api_key']
        merchant_url = data['merchant_url']
        
        # Du lieu dang json duoc truyen vao tu server
        command_insert = f"""INSERT INTO merchant (id,account_id,merchant_id,merchant_name,api_key,merchant_url) 
                                        VALUES ('{id}','{account_id}','{merchant_id}','{merchant_name}','{api_key}','{merchant_url}') RETURNING merchant_id"""
        cur.execute(command_insert)
        conn.commit()

        print ("run api create merchant account!")
<<<<<<< HEAD
    def get_api_key_by_account_id(account_id):
        # Create new account with type issuer
        command_insert = f""" SELECT m.api_key, a.account_type 
                            FROM account a left join merchant m 
                            on a.merchant_id=m.id 
                            where a.account_id='{account_id}' """
        cur.execute(command_insert)
        res=cur.fetchone()
        return res
    # /account
    def create_personal_issuer(data):
        uuid_val = uuid.uuid4()
        print ("data>>>>>>>",data)
        account_type = data['accountType']

        print ("account_type???>>>>",account_type)

        # Create new account with type issuer
        command_insert = f"""INSERT INTO account (account_id, amount, account_type) 
                            VALUES ('{str(uuid_val)}','0','{str(account_type)}') 
                            """
        cur.execute(command_insert)
        conn.commit()
        print (cur.rowcount,"run api create personal or issuer account!")
        return cur.rowcount

    def get_token_by_account(account_id):
        # print(type(account[1]))
        token = encode_auth_token(account_id)
        return token

    def account_topup(auth_token,account_id,amount):
        command_iusser_id = f"SELECT * FROM account WHERE account_type='issuer'" 
        cur.execute(command_iusser_id)
        issuers = cur.fetchall()

        id=decode_auth_token(auth_token)

        for issue in issuers:
            issueType=issue[1]
            if id == issueType:
                command_exe = f"UPDATE account SET balance='{amount}' WHERE account_id='{account_id}' RETURNING account_id'"
                cur.execute(command_exe)
                conn.commit()
                account = cur.fetchone()

=======
        add_new_account()
    def create_personal_issuer():
        print ("run api create personal or issuer account!")
    def get_token_by_account():
        print ("run api get token by account!")
    def account_topup():
>>>>>>> cab084999412ef449688c83811ab24bc690acc17
        print ("run api topup money for account!")

    # Tao transaction: /transaction/create
    def create_transaction(data):

        # Lay du lieu json tu http
        jwt_token = data['token']
        merchant_id = data['merchant_id']
        amount = data['amount']
        extra_data = data['extra_data']

        conn = psycopg2.connect("dbname=test12_db user=admin password=admin port=5432")
        cur= conn.cursor()

        id = decode_auth_token(jwt_token)
        command_merchant_id = f"SELECT * FROM merchant WHERE merchant_id='{merchant_id}'"
        cur.execute(command_merchant_id)
        merchants = cur.fetchall()

        for merchant in merchants:
            merchant_account_id = merchant[1]
            print(merchant_account_id)
            # tao data theo dang json khi lay tu database
            data = {
                "merchant_id": merchant_id,
                "amount": amount,
                "extra_data" : extra_data
            }

        data_json = json.dumps(data).encode('utf-8')
        signature = hashlib.md5(data_json).hexdigest()

        # so sanh id voi merchant id trong database neu co se insert vao database
        if id == merchant_account_id:
            command_insert = f"INSERT INTO transaction(merchant_id, income_account, amount, extra_data, signature, status) \
                VALUES('{merchant_id}','{merchant_account_id}','{amount}', '{extra_data}', '{signature}', '{transEnum.TransactionType.INITIALIZED.value}') \
                RETURNING transaction_id"
            cur.execute(command_insert)
            conn.commit()
            return cur.fetchone()
        
        print ("run api create transaction!")
    
    # /transaction/confirm
    def confirm_transaction():
        print ("run api create confirm transaction!")
    # /transaction/verify
    def verify_transaction():
        print ("run api create verify transaction!")
    # /transaction/cancel
    def cancel_transaction():
        print ("run api create cancel transaction!")

def encode_auth_token(account_id: str):
    try:
        payload = {
            'account_id': account_id
                }
        return jwt_data.encode(
                payload,
                key,
                algorithm='HS256'
            )
    except Exception as e:
        return e

def decode_auth_token(token: str):
    try:
        payload = jwt_data.decode(token, key, algorithms='HS256')
        return payload['account_id']
    except jwt_data.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt_data.InvalidTokenError:
        return 'Invalid token. Please log in again.'