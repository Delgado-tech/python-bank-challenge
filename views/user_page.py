from datetime import datetime
from controllers.account import Account
from controllers.session import Session
from mocks.account_mockup import AccountMockup
from mocks.user_mockup import UserMockup
from views.user_account_page import user_account_page


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
    
    [q] Deslogar Usuário
    [x] Fechar Aplicação \n
============================================
    """)

    return user_page, option

def user_account_login(_):
    user = Session.get_user()

    print(f"""
============================================
    Entrar na minha conta
    {datetime.now().strftime("%d/%m/%Y %H:%M")}
    
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
        value = input(f"{key}: ")

        if value.upper() == "C":
            return user_page, False
        
        if value.upper() == "X":
            return False, False
        
        inputs[key] = value

    password = input("Senha: ")

    account_number = AccountMockup.login_account(
        user_id=user.get_id(), 
        agency_id=inputs["Agência"], 
        account_number=inputs["Número da conta"], 
        password=password    
    )

    if account_number == False:
        input("\nDados ou Senha inválida!")
        return user_account_login, False

    Session.account_number = account_number

    return user_account_page, False

def user_page_show_accounts(_):
    user = Session.get_user()
    accounts = AccountMockup.get_account(user_id=user.get_id())

    print("============================================")
    print("Contas".center(44))
    print("============================================\n")

    if not accounts:
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

    return user_page, False
    
def user_page_create_account(_):
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

def user_page_delete_account(_):
    user = Session.get_user()

    print("""
============================================
    Banco Rev

    Você tem certeza que deseja deletar o seu cadastro?
    Essa ação não poderá ser desfeita!
    
    Caso queira prosseguir confirme digitando a senha dele:
    
    [x] Cancelar
    
""")
    
    password = input("Senha: ")

    if password.upper() == "X":
        return user_account_page, False

    if user._password != password:
        print("\nAs senhas não batem! - Operação cancelada")
        return user_account_page, False
    
    result = UserMockup.delete_user(id=user.user_id)
    input()

    if result:
        Session.clear()
        from views.home_page import home_page
        return home_page, False

    return user_page, False


def user_page(option: str):
    if option == "Q":
        Session.clear()
        from views.home_page import home_page
        return home_page, False

    DISPLAY_SCREEN = {
        "1": user_account_login,
        "2": user_page_show_accounts,
        "3": user_page_create_account
    }

    return DISPLAY_SCREEN.get(option, user_page_index)(option)

