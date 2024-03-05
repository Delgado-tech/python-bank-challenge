from controllers.session import Session
from mocks.account_mockup import AccountMockup


def user_page_show_accounts(_):
    from views.user.page import user_page

    user = Session.get_user()
    accounts = AccountMockup.get_account(user_id=user.get_id())

    print("============================================")
    print("Contas".center(44))
    print("============================================\n")

    if not accounts:
        input("Nenhuma conta encontrada!")
    else:
        for acc in accounts:
            print("--------------------------------------------")
            print(f"Saldo: R$ {acc.balance:.2f}\n")
            print(f"Agência: {acc._agency_id}")
            print(f"Número da conta: {acc.account_number}")
            print(f"Aberta em: {acc._created_date.strftime("%d/%m/%Y %H:%M:%S")}")
            print("--------------------------------------------")

        print("\n============================================")
        print(f"Contas: {len(accounts)} / Saldo Geral: R$ {sum(a.balance for a in accounts):.2f}")
        print("============================================")

    input()

    return user_page, False
    
