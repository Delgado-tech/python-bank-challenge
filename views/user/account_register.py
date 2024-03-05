from datetime import datetime
from controllers.account import Account
from controllers.session import Session
from mocks.account_mockup import AccountMockup
from utils.date.console_current_time import console_current_time
from views.style import Fore_Style


def user_page_register_account(_):
    from views.user.page import user_page

    user = Session.get_user()

    print(Fore_Style.PRIMARY.value, f"""
============================================
    Abrir uma nova conta
    {console_current_time()}
    
    [c] Cancelar
    [x] Fechar Aplicação
    \n
============================================
""")

    value = input(f"{Fore_Style.SECONDARY.value}Agência: {Fore_Style.WHITE.value}")

    if value.upper() == "C":
        return user_page, False
    
    if value.upper() == "X":
        return False, False
    
    agency = value

    password = input(f"{Fore_Style.SECONDARY.value}Senha: {Fore_Style.WHITE.value}")

    AccountMockup.register_account(
        account=Account(
            user_id=user.get_id(), 
            agency=agency,
            password=password
        )
    )

    input()

    return user_page, False

