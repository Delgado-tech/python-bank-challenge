import mockup
from utils.clear_console import clear_console
from utils.parse_float import parse_float
from datetime import datetime


def withdraw():
    clear_console()

    # caso o número de saques diários seja zero e a data de hoje seja igual ou superior a data da próxima
    # regeneração, os saques voltam ao seu valor máximo e a data da próxima regeneração é marcada para o dia
    # de amanhã
    if mockup.balance.get() <= 0:
        return print("Você não possui um saldo para ser sacado!")

    if mockup.daily_withdraw_count <= 0:
        if datetime.now() > mockup.next_daily_withdraw_regeneration:
            mockup.regenerate_daily_withdraw()
        else:
            return print("Vocês atingiu seu limite de saques diários! Volte amanhã.")

    withdraw_amount = parse_float(input("Informe a quantia que deseja sacar:\nR$ "), -1)

    if withdraw_amount == 0:
        return print("Operação cancelada!")

    if withdraw_amount < 0:
        print("O valor informado deve ser um número e maior que zero!")
        input()
        return withdraw()
    
    if withdraw_amount > mockup.max_withdraw_amount:
        print(f"Só é possível retirar R$ {mockup.max_withdraw_amount:.2f} por saque!")
        input()
        return withdraw()
    
    if withdraw_amount > mockup.balance.get():
        print(f"\nO valor informado é maior que o seu saldo atual!\n(Saldo Atual: R$ {mockup.balance.get():.2f})")
        input()
        return withdraw()


    if mockup.daily_withdraw_count == mockup.max_daily_withdraw_count:
        mockup.next_daily_withdraw_regeneration = mockup.get_next_daily_regeneration()

    clear_console()
    mockup.balance.remove(withdraw_amount)
    mockup.daily_withdraw_count -= 1
    mockup.WITHDRAWS.append(mockup.Transaction(withdraw_amount, datetime.now(), mockup.Transaction.Type.WITHDRAW))

    print(f"Saque de R$ {withdraw_amount:.2f} realizado com sucesso!")
    print(f"Novo saldo: R$ {mockup.balance.get():.2f}")