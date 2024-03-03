from datetime import datetime
from controllers.session import Session
from mocks.account_mockup import AccountMockup


def user_page_index(option: str):
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
    
    [q] Deslogar 
    [x] Fechar Aplicação \n
============================================
    """)

    return user_page, option

def user_page_show_accounts(option: str):
    user = Session.get_user()
    accounts = AccountMockup.get_account(user_id=user.get_id())

    print("============================================")
    print("Contas".center(44))
    print("============================================\n")

    if len(accounts) == 0:
        input("Nenhuma conta encontrada!")
    else:
        for acc in accounts:
            print("--------------------------------------------")
            print(f"Saldo: R$ {acc.balance:.2f}\n")
            print(f"Agência: {acc._agency_id}")
            print(f"Número da conta: {acc.account_number}")
            print(f"Aberta em: {acc._created_date.strftime("%d/%m/%Y %H:%M:%S")}")
            print("--------------------------------------------")

        print("\n============================================")
        print(f"Contas: {len(accounts)} / Saldo Geral: R$ {sum(a.balance for a in accounts):.2f}")
        print("============================================")

    return user_page, option
    



def user_page(option: str):
    if option == "Q":
        from views.home_page import home_page
        return home_page, False

    DISPLAY_SCREEN = {
        "1": user_page,
        "2": user_page_show_accounts,
        "3": user_page
    }

    return DISPLAY_SCREEN.get(option, user_page_index)(option)

