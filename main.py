from utils.clear_console import clear_console
from views.home.page import home_page



def exit_message():
    print("Agradeçemos a sua preferência!")
    input("                   - Banco Rev")
    clear_console()

def main():
    view = home_page
    default_option = "0"
    option = default_option

    while True:
        clear_console()
        
        view, option = view(option)
        
        if option:        
            option = input("> ").upper()
        else:
            option = default_option
            

        if option == "X" or view == False:
            break

    clear_console()
    exit_message()

main()