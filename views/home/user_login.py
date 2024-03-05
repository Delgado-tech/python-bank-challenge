from controllers.session import Session

from mocks.user_mockup import UserMockup
from utils.date.console_current_time import console_current_time
from views.style import Fore_Style


def home_page_user_login(_):
    from views.home.page import home_page
    from views.user.page import user_page

    print(Fore_Style.PRIMARY.value, f"""
============================================
    Entrar
    {console_current_time()}
    
    [c] Cancelar
    [x] Fechar Aplicação
    \n
============================================
""", Fore_Style.RESET.value)
    
    value = input(f"{Fore_Style.SECONDARY.value}E-mail: {Fore_Style.WHITE.value}")

    if value.upper() == "C":
        return home_page, False
    
    if value.upper() == "X":
        return False, False
    
    email = value.lower()

    password = input(f"{Fore_Style.SECONDARY.value}Senha: {Fore_Style.WHITE.value}")

    user_id = UserMockup.login_user(email=email, password=password)

    if user_id == False:
        input(f"{Fore_Style.DANGER.value}\nE-mail ou Senha inválido!")
        return home_page_user_login, False

    Session.user_id = user_id

    return user_page, False