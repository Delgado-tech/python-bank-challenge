from datetime import datetime
from controllers.session import Session
from controllers.transaction import Transaction
from mocks.account_mockup import AccountMockup
from utils.parse_float import parse_float


def user_account_page_index(option: str):
    user = Session.get_user()
    account = Session.get_account()

    print(f"""
============================================
    Banco Rev
    {datetime.now().strftime("%d/%m/%Y %H:%M")}

    Usuário: {user.name}
    Agência: {account._agency_id}
    Número da conta: {account.account_number}
    
    Saques diários restantes: {user._daily_withdraws}
    Saldo: R$ {account.balance:.2f}

    Escolha uma opção:
    
    [1] Realizar Saque
    [2] Realizar Deposito
    [3] Visualizar Extrato
    [#] Excluir Conta
    
    [v] Voltar
    [q] Deslogar Usuário 
    [x] Fechar Aplicação \n
============================================
    """)

    return user_account_page, option

def user_account_page_withdraw(_):
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

def user_account_page_deposit(_):
    account = Session.get_account()

    print(f"""
============================================
    Banco Rev
    {datetime.now().strftime("%d/%m/%Y %H:%M")}

    Realizar Deposito

    [x] Cancelar

    """)

    value = input("Valor: R$ ")

    if value.upper() == "X":
        return user_account_page, False
    
    amount = parse_float(value)

    if amount <= 0:
        input("O valor informado é inválido!")
        return user_account_page_withdraw, False
    
    account.balance += amount
    account.statements.append(Transaction(
        amount=amount,
        type=Transaction.Type.DEPOSIT
    ))

    print(f"\nDeposito de R$ {amount:.2f} realizado com sucesso!")
    print(f"Saldo atual: R$ {account.balance:.2f}")
    input()

    return user_account_page, False

def user_account_page_show_statements(_):
    account = Session.get_account()

    print("============================================")
    print("Extrato".center(44))
    print("============================================\n")

    statements = account.statements.copy()
    statements.sort(key=lambda x: x.date)


    if len(statements) == 0:
        input("Nenhuma movimentação encontrada!")
    else:
        for stt in statements:
            print("--------------------------------------------")
            print(f"Tipo: {stt.type.value.upper()}\n")
            print(f"Quantia: R$ {stt.amount:.2f}\n")
            print(f"Realizado em: {stt.date.strftime("%d/%m/%Y %H:%M:%S")}")
            print("--------------------------------------------")

        deposit_count = len([s for s in statements if s.type == Transaction.Type.DEPOSIT])
        withdraw_count = len([s for s in statements if s.type == Transaction.Type.WITHDRAW])

        print("\n============================================")
        print(f"Depositos: {deposit_count} / Saques: {withdraw_count}")
        print("============================================")

    return user_account_page, False

def user_account_page_delete(_):
    user = Session.get_user()
    account = Session.get_account()

    print("""
============================================
    Banco Rev

    Você tem certeza que deseja deletar a sua conta?
    Essa ação não poderá ser desfeita!
    
    Caso queira prosseguir confirme digitando a senha da conta:
    
    [x] Cancelar
    
""")
    
    password = input("Senha: ")

    if password.upper() == "X":
        return user_account_page, False

    if account._password != password:
        print("\nAs senhas não batem! - Operação cancelada")
        return user_account_page, False
    
    result = AccountMockup.delete_account(user_id=user.user_id, account_number=account.account_number)
    input()

    if result:
        Session.clear(user_id=False)
        from views.user_page import user_page
        return user_page, False

    return user_account_page, False


def user_account_page(option: str):
    if option == "Q":
        Session.clear()
        from views.home_page import home_page
        return home_page, False
    
    if option == "V":
        Session.clear(user_id=False)
        from views.user_page import user_page
        return user_page, False

    DISPLAY_SCREENS = {
        "1": user_account_page_withdraw,
        "2": user_account_page_deposit,
        "3": user_account_page_show_statements,
        "#": user_account_page_delete
    }

    return DISPLAY_SCREENS.get(option, user_account_page_index)(option)