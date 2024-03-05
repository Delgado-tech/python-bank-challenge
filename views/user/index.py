from datetime import datetime
from controllers.session import Session


def user_page_index(option: str):
    from views.user.page import user_page

    user = Session.get_user()

    print(f"""
============================================
    Banco Rev
    {datetime.now().strftime("%d/%m/%Y %H:%M")}

    Usuário: {user.name}
    
    Saques diários restantes: {user._daily_withdraws}
    
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
