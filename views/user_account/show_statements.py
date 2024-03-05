from controllers.session import Session
from controllers.transaction import Transaction
from views.style import Fore_Style


def user_account_page_show_statements(_):
    from views.user_account.page import user_account_page

    account = Session.get_account()

    print(Fore_Style.PRIMARY.value)
    print("============================================")
    print("Extrato".center(44))
    print("============================================\n")

    statements = account.statements.copy()
    statements.sort(key=lambda x: x.date)


    if len(statements) == 0:
        input("Nenhuma movimentação encontrada!")
    else:
        for stt in statements:
            print("--------------------------------------------")
            print(f"Tipo: {stt.type.value.upper()}\n")
            print(f"Quantia: {Fore_Style.SUCCESS.value}R$ {stt.amount:.2f}\n", Fore_Style.PRIMARY.value)
            print(f"Realizado em: {Fore_Style.GRAY.value}{stt.date.strftime("%d/%m/%Y %H:%M:%S")}", Fore_Style.PRIMARY.value)
            print("--------------------------------------------")

        deposit_count = len([s for s in statements if s.type == Transaction.Type.DEPOSIT])
        withdraw_count = len([s for s in statements if s.type == Transaction.Type.WITHDRAW])

        print("\n============================================")
        print(f"Depositos: {deposit_count} / Saques: {withdraw_count}")
        print("============================================")

    input()
    
    return user_account_page, False
