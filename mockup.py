from datetime import datetime, timedelta
from enum import Enum
from controllers.balance import Balance
from controllers.transaction import Transaction
from utils.date.string_to_date import string_to_date
from utils.parse_int import parse_int

def get_next_daily_regeneration():
    return string_to_date((datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d 00:00:00"))


DEPOSITS: list[Transaction] = [Transaction(parse_int(1), datetime(2023,10,11), Transaction.Type.DEPOSIT)]
WITHDRAWS: list[Transaction] = [Transaction(parse_int(2), datetime(2024,1,15), Transaction.Type.WITHDRAW)]

balance = Balance(1000.0)

max_withdraw_amount: float = 500.0
max_daily_withdraw_count: int = 3
daily_withdraw_count: int = max_daily_withdraw_count
next_daily_withdraw_regeneration = get_next_daily_regeneration()


def regenerate_daily_withdraw():
    global daily_withdraw_count 
    global next_daily_withdraw_regeneration
    
    daily_withdraw_count = max_daily_withdraw_count
    next_daily_withdraw_regeneration = get_next_daily_regeneration()
