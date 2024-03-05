from controllers.session import Session
from views.user_account.account_delete import user_account_page_delete_account
from views.user_account.deposit import user_account_page_deposit
from views.user_account.index import user_account_page_index
from views.user_account.show_statements import user_account_page_show_statements
from views.user_account.withdraw import user_account_page_withdraw


def user_account_page(option: str):
    if option == "Q":
        Session.clear()
        from views.home.page import home_page
        return home_page, False
    
    if option == "V":
        Session.clear(user_id=False)
        from views.user.page import user_page
        return user_page, False

    DISPLAY_SCREENS = {
        "1": user_account_page_withdraw,
        "2": user_account_page_deposit,
        "3": user_account_page_show_statements,
        "#": user_account_page_delete_account
    }

    return DISPLAY_SCREENS.get(option, user_account_page_index)(option)