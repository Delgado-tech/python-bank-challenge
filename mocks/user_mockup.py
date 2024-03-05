from datetime import datetime
from controllers.address import Address
from controllers.user import User


class UserMockup:
    user_list: list[User] = [
        User(
            user_id=1,
            email="leo@gmail.com", 
            password="1234", 
            name="Leonardo", 
            cpf="12345678901", 
            birtdate=datetime(2003, 6, 3), 
            address=Address(
                street="Rua Landosvaldo",
                number="123",
                neighborhood="Tempora",
                city="Votocity",
                state="SP"
            )
        )
    ]

    @staticmethod
    def get_next_id():
        return len(UserMockup.user_list) + 1
    
    @staticmethod
    def get_user(*, id: int | None = None, cpf: str | None = None, email: str | None = None):
        
        search_results: list[User] = []

        if id:
            search_results = [u for u in UserMockup.user_list if u.get_id() == id]

        if cpf:
            search_results = [u for u in UserMockup.user_list if u.cpf == cpf]

        if email:
            search_results = [u for u in UserMockup.user_list if u.email == email]
        
        return search_results[0] if len(search_results) > 0 else None

    @staticmethod
    def register_user(*, user: User):
        search_results: list[User] = [u for u in UserMockup.user_list if u.cpf == user.cpf or u.email == user.email]

        if len(search_results) > 0:
            print("O CPF ou o Email informado já foi cadastrado!")
            return False

        user.user_id = UserMockup.get_next_id()
        UserMockup.user_list.append(user)

        return user.user_id

    @staticmethod
    def delete_user(*, id: int):
        user = UserMockup.get_user(id=id)

        if user:
            UserMockup.user_list.remove(user)
            print(f"\nUsuário de id {id} foi deletado com sucesso!")
            return True
        
        print(f"\nId {id} não encontrado!")
        return False

    @staticmethod
    def login_user(*, email, password):
        user = [u for u in UserMockup.user_list if u.email == email and u._password == password]

        if len(user) > 0:
            return user[0].user_id
        
        return False
        