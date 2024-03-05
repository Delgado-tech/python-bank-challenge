from utils.date.console_current_time import console_current_time
from views.style import Fore_Style

def home_page_index(option: str):
    from views.home.page import home_page

    print(Fore_Style.PRIMARY.value, f"""
============================================
    Seja bem-vindo ao Banco Rev!
    {console_current_time()}
    
    Escolha uma opção:
    
    [1] Entrar
    [2] Cadastrar
    
    [x] Fechar Aplicação \n
============================================
    """, Fore_Style.RESET.value)

    return home_page, option
