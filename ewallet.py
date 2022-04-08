from database.account import add_new_account

class Ewallet():
    def create_merchant():
        print ("run api create merchant account!")
        add_new_account()
    def create_personal_issuer():
        print ("run api create personal or issuer account!")
    def get_token_by_account():
        print ("run api get token by account!")
    def account_topup():
        print ("run api topup money for account!")
    def create_transaction():
        print ("run api create transaction!")
    def confirm_transaction():
        print ("run api create confirm transaction!")
    def verify_transaction():
        print ("run api create verify transaction!")
    def cancel_transaction():
        print ("run api create cancel transaction!")
