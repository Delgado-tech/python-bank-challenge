import mockup
from datetime import datetime
from utils.clear_console import clear_console
from utils.parse_float import parse_float


def deposit():
    clear_console()
    
    deposit_amount = parse_float(input("Informe a quantia que deseja depositar:\nR$ "), -1)

    if deposit_amount == 0:
        return print("Operação cancelada!")

    if deposit_amount < 0:
        print("O valor informado deve ser um número e maior que zero!")
        input()
        return deposit()
    
    clear_console()
    mockup.balance.add(deposit_amount)
    mockup.DEPOSITS.append(mockup.Transaction(deposit_amount, datetime.now(), mockup.Transaction.Type.DEPOSIT))

    print(f"Deposito de R$ {deposit_amount:.2f} realizado com sucesso!")
    print(f"Novo saldo: R$ {mockup.balance.get():.2f}")