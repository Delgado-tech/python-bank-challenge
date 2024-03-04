#`nome, data_de_nascimento, cpf e endereço`

from datetime import datetime, timedelta

from controllers.address import Address
from controllers.transaction import Transaction
from utils.date.string_to_date import string_to_date

default_max_daily_withdraws: int = 3

class User:
    user_id: int
    created_date: datetime

    email: str
    max_daily_withdraws: int = 3

    cpf: str
    name: str
    birtdate: str
    address: Address

    def __init__(self, *, email: str, password: str, name: str, cpf: str, birtdate: datetime, address: Address, created_date: datetime = datetime.now(), user_id: int = None) -> None:
        if user_id: self.user_id = user_id
        if created_date: self.created_date = created_date
        self._daily_withdraws = default_max_daily_withdraws
        self.max_daily_withdraws = default_max_daily_withdraws
        self._next_daily_withdraws_regeneration_date = string_to_date((datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d 00:00:00"))
        # user_info
        self.cpf: str = cpf
        self.name: str = name
        self.birtdate: datetime = birtdate
        self.address: Address = address
        # account
        self.email = email
        self._password = password

    def get_id(self):
        return self.user_id
    
    def set_next_daily_withdraws_regeneration_date(self):
        self._next_daily_withdraws_regeneration_date = string_to_date((datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d 00:00:00"))

    def regenerate_daily_withdraws(self):
        self._daily_withdraws = self.max_daily_withdraws
        self._next_daily_withdraws_regeneration_date = self.set_next_daily_withdraws_regeneration_date()

    def change_password(self, *, current_password, new_password):
        if self._password != current_password:
            return print("A senha informada não coincide com a atual")
        
        self._password = new_password
        print("Senha alterada com sucesso!")

