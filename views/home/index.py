from datetime import datetime


def home_page_index(option: str):
    from views.home.page import home_page

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
