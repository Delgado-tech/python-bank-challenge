from controllers.session import Session
from mocks.account_mockup import AccountMockup


def user_account_page_delete_account(_):
    from views.user_account.page import user_account_page

    user = Session.get_user()
    account = Session.get_account()

    print("""
============================================
    Banco Rev

    Você tem certeza que deseja deletar a sua conta?
    Essa ação não poderá ser desfeita!
    
    Caso queira prosseguir confirme digitando a senha da conta:
    
    [x] Cancelar
    
""")
    
    password = input("Senha: ")

    if password.upper() == "X":
        return user_account_page, False

    if account._password != password:
        print("\nAs senhas não batem! - Operação cancelada")
        return user_account_page, False
    
    result = AccountMockup.delete_account(user_id=user.user_id, account_number=account.account_number)
    input()

    if result:
        Session.clear(user_id=False)
        from views.user.page import user_page
        return user_page, False

    return user_account_page, False

