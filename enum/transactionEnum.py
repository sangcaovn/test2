import enum

class TransactionEnum(enum.Enum):
    Initialized="initialized"
    Confirmed="confirmed"
    Verified="verified"
    Completed="completed"
    Expired="expired"
    Canceled="canceled"
    Failed="failed"