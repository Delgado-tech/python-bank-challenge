from datetime import datetime
from controllers.session import Session
from mocks.account_mockup import AccountMockup
from utils.date.console_current_time import console_current_time
from views.style import Fore_Style


def user_account_login(_):
    from views.user.page import user_page
    from views.user_account.page import user_account_page

    user = Session.get_user()

    print(Fore_Style.PRIMARY.value, f"""
============================================
    Entrar na minha conta
    {console_current_time()}
    
    [c] Cancelar
    [x] Fechar Aplicação
    \n
============================================
""")
    
    inputs = {
        "Agência": "",
        "Número da conta": ""
    }

    for key, value in inputs.items():
        value = input(f"{Fore_Style.SECONDARY.value}{key}: {Fore_Style.WHITE.value}")

        if value.upper() == "C":
            return user_page, False
        
        if value.upper() == "X":
            return False, False
        
        inputs[key] = value

    password = input(f"{Fore_Style.SECONDARY.value}Senha: {Fore_Style.WHITE.value}")

    account_number = AccountMockup.login_account(
        user_id=user.get_id(), 
        agency_id=inputs["Agência"], 
        account_number=inputs["Número da conta"], 
        password=password    
    )

    if account_number == False:
        input(f"{Fore_Style.DANGER.value}\nDados ou Senha inválida!")
        return user_account_login, False

    Session.account_number = account_number

    return user_account_page, False
