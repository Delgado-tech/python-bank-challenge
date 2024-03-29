from datetime import datetime
from controllers.session import Session
from controllers.transaction import Transaction
from utils.date.console_current_time import console_current_time
from utils.parse_float import parse_float
from views.style import Fore_Style


def user_account_page_deposit(_):
    from views.user_account.page import user_account_page

    account = Session.get_account()

    print(Fore_Style.PRIMARY.value, f"""
============================================
    Banco Rev
    {console_current_time()}

    Realizar Deposito

    [x] Cancelar

    """)

    value = input(f"Valor: {Fore_Style.SUCCESS.value}R$ ")

    if value.upper() == "X":
        return user_account_page, False
    
    amount = parse_float(value)

    if amount <= 0:
        input(f"\n{Fore_Style.DANGER.value}O valor informado é inválido!")
        return user_account_page_deposit, False
    
    account.balance += amount
    account.statements.append(Transaction(
        amount=amount,
        type=Transaction.Type.DEPOSIT
    ))

    print(f"\nDeposito de R$ {amount:.2f} realizado com sucesso!")
    print(f"Saldo atual: R$ {account.balance:.2f}")
    input()

    return user_account_page, False

