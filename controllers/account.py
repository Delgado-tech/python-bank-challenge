# Armazenar as contas em uma lista, uma conta é composta por: `agência, número_da_conta, usuário`

from datetime import datetime

from controllers.transaction import Transaction


class Account:
    account_number: str
    balance: float

    deposits: list[Transaction] = []
    withdraws: list[Transaction] = []

    def __init__(self, *, user_id: int, agency: str, password: str, created_date: datetime = datetime.now(), balance: float = 0.0, account_number: str | None = None) -> None:
        if account_number: self.account_number = account_number
        self._user_id: int = user_id
        self._agency_id: str = agency
        self.balance: float = balance
        self._password: str = password
        self._created_date: datetime = created_date

    def get_user_id(self):
        return self._user_id
    
    def get_agency_id(self):
        return self._agency_id
    
    def get_account_number(self):
        return self._account_number
    
    def change_password(self, *, current_password, new_password):
        if self._password != current_password:
            return print("A senha informada não coincide com a atual")
        
        self._password = new_password
        print("Senha alterada com sucesso!")