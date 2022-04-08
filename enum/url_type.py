import enum

class UrlType(enum.Enum):
    create_merchant="/merchant/signup"
    create_personal_issuer="/account"
    create_transaction="/transaction/create"
    confirm_transaction="/transaction/confirm"
    verify_transaction="/transaction/verify"
    cancel_transaction="/transaction/cancel"