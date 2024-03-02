from datetime import datetime
from enum import Enum


class Transaction():
    class Type(Enum):
        WITHDRAW = "saque"
        DEPOSIT = "deposito"

    amount: int = 0
    date: datetime
    type: Type

    def __init__(self, amount: int, date: datetime, type: Type):
        self.amount = amount
        self.date = date
        self.type = type