from datetime import datetime
from controllers.account import Account
from controllers.session import Session
from mocks.account_mockup import AccountMockup


def user_page_register_account(_):
    from views.user.page import user_page

    user = Session.get_user()

    print(f"""
============================================
    Abrir uma nova conta
    {datetime.now().strftime("%d/%m/%Y %H:%M")}
    
    [c] Cancelar
    [x] Fechar Aplicação
    \n
============================================
""")

    value = input("Agência: ")

    if value.upper() == "C":
        return user_page, False
    
    if value.upper() == "X":
        return False, False
    
    agency = value

    password = input("Senha: ")

    AccountMockup.register_account(
        account=Account(
            user_id=user.get_id(), 
            agency=agency,
            password=password
        )
    )

    input()

    return user_page, False

