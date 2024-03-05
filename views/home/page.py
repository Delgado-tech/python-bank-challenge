from views.home.index import home_page_index
from views.home.user_login import home_page_user_login
from views.home.user_register import home_page_user_register


def home_page(option: str):

    DISPLAY_SCREEN = {
        "1": home_page_user_login,
        "2": home_page_user_register
    }

    return DISPLAY_SCREEN.get(option, home_page_index)(option)