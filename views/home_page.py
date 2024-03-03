from datetime import datetime
from controllers.session import Session

from mocks.user_mockup import UserMockup
from views.user_page import user_page


def home_page_index(option: str):
    print(f"""
============================================
    Seja bem-vindo ao Banco Rev!
    {datetime.now().strftime("%d/%m/%Y %H:%M")}
    
    Escolha uma opção:
    
    [1] Entrar
    [2] Cadastrar
    
    [x] Fechar Aplicação \n
============================================
    """)

    return home_page, option

def home_page_login(option: str):

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
        input("E-mail ou Senha inválido!")
        return home_page_login, False

    Session.user_id = user_id

    return user_page, option


def home_page_register(_):
    print("register")




def home_page(option: str):

    DISPLAY_SCREEN = {
        "1": home_page_login,
        "2": home_page_register
    }

    return DISPLAY_SCREEN.get(option, home_page_index)(option)