import mockup

from datetime import datetime, timedelta

from bank_actions.deposit import deposit
from bank_actions.withdraw import withdraw
from bank_actions.view_statement import view_statement

from utils.clear_console import clear_console
from utils.parse_int import parse_int


BANK_ACTIONS = list([withdraw, deposit, view_statement])


option: int = None

while option != 0:
    clear_console()

    print(f"""
============================================
    Banco Rev
    {datetime.now().strftime("%d/%m/%Y %H:%M")}

    Usuário: Leonardo Delgado
    - Agência: 1234-5
    - Conta Corrente: 67890-1
    
    Saldo atual: R$ {mockup.balance.get():.2f}
    Saques diários restantes: {mockup.daily_withdraw_count}
    
    Escolha uma opção:
    
    [1] Realizar Saque
    [2] Realizar Deposito
    [3] Visualizar extrato
    
    [0] Sair \n
============================================
    """)

    option = parse_int(input("> "), -1)

    if option > 0 and option <= len(BANK_ACTIONS):
        BANK_ACTIONS[option - 1]()
        input()


clear_console()
print("Agradeçemos a sua preferência!")
input("                   - Banco Rev")

clear_console()
