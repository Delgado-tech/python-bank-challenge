from datetime import datetime
from controllers.user import User
from mocks.user_mockup import UserMockup
from controllers.account import Account


class AccountMockup:
    account_list: list[Account] = [
        Account(
            user_id=1,
            agency="0001",
            account_number="1234567",
            password="1234",
            balance=100,
            created_date=datetime(2023,10,3)
        )
    ]

    @staticmethod
    def get_next_id():
        next_id = len(AccountMockup.account_list) + 1
        return f"{next_id:07d}"
    
    @staticmethod
    def get_account(*, user_id: int | None = None, agency_id: int | None = None, account_number: int | None = None):
        search_results: list[Account] = []
        
        if user_id:
            search_results = [a for a in AccountMockup.account_list if a.get_user_id() == user_id]

        if agency_id:
            search_results = [a for a in search_results if a.get_agency_id() == agency_id]
        
        if account_number:
            search_results = [a for a in search_results if a.get_account_number() == account_number]
        
        return search_results if len(search_results) > 0 else None
    
    @staticmethod
    def register_account(*, account: Account):
        user: User = UserMockup.get_user(id=account._user_id)

        if user == None:
            return print("O Usuário solicitante não foi encontrado!")

        account.account_number = AccountMockup.get_next_id()
        AccountMockup.account_list.append(account)
        print(f"A conta foi criada com sucesso! O seu número é: {account.account_number}")

    @staticmethod
    def delete_account(*, user_id: str, account_number: str):
        account = AccountMockup.get_account(user_id=user_id, account_number=account_number)
        
        if account:
            AccountMockup.account_list.remove(account[0])
            print(f"A conta de número {account_number} foi deletado com sucesso!")
        else:
            print(f"A conta de número {account_number} informada não foi encontrada!")
        
    @staticmethod
    def login_account(*, user_id: int, agency_id: str, account_number: str, password: str):
        account = AccountMockup.get_account(user_id=user_id, agency_id=agency_id, account_number=account_number)

        account = [a for a in account if a._password == password]

        if account:
            if len(account) > 0:
                return account[0].account_number

        return False
        
        

        