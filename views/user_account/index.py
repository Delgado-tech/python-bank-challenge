from datetime import datetime
from controllers.session import Session
from utils.date.console_current_time import console_current_time
from views.style import Fore_Style


def user_account_page_index(option: str):
    from views.user_account.page import user_account_page

    user = Session.get_user()
    account = Session.get_account()

    print(Fore_Style.PRIMARY.value, f"""
============================================
    Banco Rev
    {console_current_time()}

    Usuário: {Fore_Style.SECONDARY.value}{user.name}{Fore_Style.PRIMARY.value}
    Agência: {Fore_Style.SECONDARY.value}{account._agency_id}{Fore_Style.PRIMARY.value}
    Número da conta: {Fore_Style.SECONDARY.value}{account.account_number}{Fore_Style.PRIMARY.value}
    
    Saques diários restantes: {Fore_Style.SECONDARY.value}{user._daily_withdraws}{Fore_Style.PRIMARY.value}
    Saldo: {Fore_Style.SUCCESS.value}R$ {account.balance:.2f}{Fore_Style.PRIMARY.value}

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
