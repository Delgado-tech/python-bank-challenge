from datetime import datetime
from controllers.session import Session
from controllers.transaction import Transaction
from utils.date.console_current_time import console_current_time
from utils.parse_float import parse_float
from views.style import Fore_Style


def user_account_page_withdraw(_):
    from views.user_account.page import user_account_page

    user = Session.get_user()
    account = Session.get_account()

    if user._daily_withdraws == 0:
        if datetime.now() < user._next_daily_withdraws_regeneration_date:
            input(f"{Fore_Style.DANGER.value}Você atingiu o seu número máximo de saques diários! Tente novamente amanhã!")
            return user_account_page, False
        
        user.regenerate_daily_withdraws()

    print(Fore_Style.PRIMARY.value, f"""
============================================
    Banco Rev
    {console_current_time()}

    Realizar Saque
    Saldo: {Fore_Style.SUCCESS.value}R$ {account.balance:.2f}{Fore_Style.PRIMARY.value}

    [x] Cancelar

    """)

    value = input(f"Valor: {Fore_Style.SUCCESS.value}R$ ")

    if value.upper() == "X":
        return user_account_page, False
    
    amount = parse_float(value)

    if amount <= 0:
        input(f"{Fore_Style.DANGER.value}\nO valor informado é inválido!")
        return user_account_page_withdraw, False
    
    if amount > user.max_withdraw_amount:
        input(f"{Fore_Style.DANGER.value}\nA quantia informada é maior que o valor de R$ {user.max_withdraw_amount:.2f} de saque permitido!")
        return user_account_page_withdraw, False
    
    if amount > account.balance:
        input(f"{Fore_Style.DANGER.value}\nA quantia informada é maior que o saldo da sua conta atual!")
        return user_account_page_withdraw, False
    
    account.balance -= amount
    user._daily_withdraws -= 1
    account.statements.append(Transaction(
        amount=amount,
        type=Transaction.Type.WITHDRAW
    ))

    print(f"\nSaque de R$ {amount:.2f} realizado com sucesso!")
    print(f"Saldo atual: R$ {account.balance:.2f}")
    input()

    return user_account_page, False


