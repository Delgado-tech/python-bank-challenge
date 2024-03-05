from datetime import datetime

from views.style import Fore_Style

def console_current_time():
    return f"{Fore_Style.GRAY.value}{datetime.now().strftime("%d/%m/%Y %H:%M")}{Fore_Style.PRIMARY.value}"