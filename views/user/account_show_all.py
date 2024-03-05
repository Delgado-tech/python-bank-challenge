from controllers.session import Session
from mocks.account_mockup import AccountMockup
from views.style import Fore_Style


def user_page_show_accounts(_):
    from views.user.page import user_page

    user = Session.get_user()
    accounts = AccountMockup.get_account(user_id=user.get_id())

    print(Fore_Style.PRIMARY.value)
    print("============================================")
    print("Contas".center(44))
    print("============================================\n")

    if not accounts:
        print("Nenhuma conta encontrada!")
    else:
        for acc in accounts:
            print("--------------------------------------------")
            print(f"Saldo: {Fore_Style.SECONDARY.value}R$ {acc.balance:.2f}\n", Fore_Style.PRIMARY.value)
            print(f"Agência: {Fore_Style.SECONDARY.value}{acc._agency_id}", Fore_Style.PRIMARY.value)
            print(f"Número da conta: {Fore_Style.SECONDARY.value}{acc.account_number}", Fore_Style.PRIMARY.value)
            print(f"Aberta em: {Fore_Style.GRAY.value}{acc._created_date.strftime("%d/%m/%Y %H:%M:%S")}", Fore_Style.PRIMARY.value)
            print("--------------------------------------------")

        print("\n============================================")
        print(f"Contas: {len(accounts)} / Saldo Geral: R$ {sum(a.balance for a in accounts):.2f}")
        print("============================================")

    input()

    return user_page, False
    
