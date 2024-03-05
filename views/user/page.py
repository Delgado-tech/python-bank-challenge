from controllers.session import Session
from views.user.account_login import user_account_login
from views.user.account_register import user_page_register_account
from views.user.account_show_all import user_page_show_accounts
from views.user.index import user_page_index
from views.user.user_delete import user_page_delete_user


def user_page(option: str):
    if option == "Q":
        Session.clear()
        from views.home.page import home_page
        return home_page, False

    DISPLAY_SCREEN = {
        "1": user_account_login,
        "2": user_page_show_accounts,
        "3": user_page_register_account,
        "#": user_page_delete_user
    }

    return DISPLAY_SCREEN.get(option, user_page_index)(option)

