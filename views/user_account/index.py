from datetime import datetime
from controllers.session import Session


def user_account_page_index(option: str):
    from views.user_account.page import user_account_page

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
