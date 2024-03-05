from datetime import datetime
from controllers.session import Session
from controllers.transaction import Transaction
from utils.parse_float import parse_float


def user_account_page_withdraw(_):
    from views.user_account.page import user_account_page

    user = Session.get_user()
    account = Session.get_account()

    if user._daily_withdraws == 0:
        if datetime.now() < user._next_daily_withdraws_regeneration_date:
            print("Você atingiu o seu número máximo de saques diários! Tente novamente amanhã!")
            return user_account_page, False
        
        user.regenerate_daily_withdraws()

    print(f"""
============================================
    Banco Rev
    {datetime.now().strftime("%d/%m/%Y %H:%M")}

    Realizar Saque
    Saldo: R$ {account.balance:.2f}

    [x] Cancelar

    """)

    value = input("Valor: R$ ")

    if value.upper() == "X":
        return user_account_page, False
    
    amount = parse_float(value)

    if amount <= 0:
        input("O valor informado é inválido!")
        return user_account_page_withdraw, False
    
    if amount > user.max_withdraw_amount:
        input(f"A quantia informada é maior que o valor de R$ {user.max_withdraw_amount:.2f} de saque permitido!")
        return user_account_page_withdraw, False
    
    if amount > account.balance:
        input(f"A quantia informada é maior que o saldo da sua conta atual!")
        return user_account_page_withdraw, False
    
    account.balance -= amount
    account.statements.append(Transaction(
        amount=amount,
        type=Transaction.Type.WITHDRAW
    ))

    print(f"\nSaque de R$ {amount:.2f} realizado com sucesso!")
    print(f"Saldo atual: R$ {account.balance:.2f}")
    input()

    return user_account_page, False


