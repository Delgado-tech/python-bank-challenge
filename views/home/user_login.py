from datetime import datetime
from controllers.session import Session

from mocks.user_mockup import UserMockup


def home_page_user_login(_):
    from views.home.page import home_page
    from views.user.page import user_page

    print(f"""
============================================
    Entrar
    {datetime.now().strftime("%d/%m/%Y %H:%M")}
    
    [c] Cancelar
    [x] Fechar Aplicação
    \n
============================================
""")
    
    value = input("E-mail: ")

    if value.upper() == "C":
        return home_page, False
    
    if value.upper() == "X":
        return False, False
    
    email = value.lower()

    password = input("Senha: ")

    user_id = UserMockup.login_user(email=email, password=password)

    if user_id == False:
        input("\nE-mail ou Senha inválido!")
        return home_page_user_login, False

    Session.user_id = user_id

    return user_page, False