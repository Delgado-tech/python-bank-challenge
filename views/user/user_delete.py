from controllers.session import Session
from mocks.user_mockup import UserMockup
from views.style import Fore_Style


def user_page_delete_user(_):
    from views.user.page import user_page
    
    user = Session.get_user()

    print(Fore_Style.DANGER.value, """
============================================
    Banco Rev

    Você tem certeza que deseja deletar o seu cadastro?
    Essa ação não poderá ser desfeita!
    
    Caso queira prosseguir confirme digitando a senha dele:
    
    [x] Cancelar
    
""")
    
    password = input("Senha: ")

    if password.upper() == "X":
        return user_page, False

    if user._password != password:
        input("\nAs senhas não batem! - Operação cancelada")
        return user_page, False
    
    result = UserMockup.delete_user(id=user.user_id)
    input()

    if result:
        Session.clear()
        from views.home.page import home_page
        return home_page, False

    return user_page, False
