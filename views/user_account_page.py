from datetime import datetime
from controllers.session import Session


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

def user_account_page_delete(option: str):
    from views.user_page import user_page
    return user_page, False

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
        "1": user_account_page,
        "2": user_account_page,
        "3": user_account_page,
        "#": user_account_page
    }

    return DISPLAY_SCREENS.get(option, user_account_page_index)(option)