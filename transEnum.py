import enum

class TransactionType(enum.Enum):
    INITIALIZED = "initialized"
    CONFIRMED = "confirmed"
    VERIFIED = "verified"
    COMPLETED = "completed"
    CANCELED = "canceled"
    EXPIRED = 'expired'
    FAILED = "failed"