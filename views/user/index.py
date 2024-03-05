from datetime import datetime
from controllers.session import Session
from utils.date.console_current_time import console_current_time
from views.style import Fore_Style


def user_page_index(option: str):
    from views.user.page import user_page

    user = Session.get_user()

    print(Fore_Style.PRIMARY.value, f"""
============================================
    Banco Rev
    {console_current_time()}

    Usuário: {Fore_Style.SECONDARY.value}{user.name}{Fore_Style.PRIMARY.value}
    
    Saques diários restantes: {Fore_Style.SECONDARY.value}{user._daily_withdraws}{Fore_Style.PRIMARY.value}
    
    Escolha uma opção:
    
    [1] Entrar em uma conta
    [2] Visualizar contas
    [3] Abrir uma conta
    [#] Excluir Cadastro
    
    [q] Deslogar Usuário
    [x] Fechar Aplicação \n
============================================
    """)

    return user_page, option
