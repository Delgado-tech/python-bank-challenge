from utils.clear_console import clear_console

def view_statement():
    clear_console()
    
    VIEW_STATEMENTS: list[mockup.Transaction] = mockup.DEPOSITS + mockup.WITHDRAWS
    VIEW_STATEMENTS.sort(key=lambda x: x.date)

    if (len(VIEW_STATEMENTS) == 0):
        return print("Nenhum histórico de deposito ou saque encontrado!")
    
    print("============================================")
    print("Extrato".center(44))
    print("============================================\n")

    for statement in VIEW_STATEMENTS:
        print("--------------------------------------------")
        print(f"Operação: {statement.type.value.upper()}")
        print(f"Valor: R$ {statement.amount:.2f}")
        print(statement.date.strftime("%d/%m/%Y %H:%M:%S"))
        print("--------------------------------------------")
    
    print("\n============================================")
    print(f"Depositos: {len(mockup.DEPOSITS)} / Saques: {len(mockup.WITHDRAWS)}")
    print("============================================")



