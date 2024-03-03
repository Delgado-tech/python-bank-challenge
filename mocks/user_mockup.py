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
            ),
            balance=100.0
        )
    ]

    @staticmethod
    def get_next_id():
        return len(UserMockup.user_list) + 1
    
    @staticmethod
    def get_user(*, id: int):
        search_results: list[User] = [u for u in UserMockup.user_list if u.get_id() == id]
        
        return search_results[0] if len(search_results) > 0 else None

    @staticmethod
    def register_user(*, user: User):
        search_results: list[User] = [u for u in UserMockup.user_list if u.cpf == user.cpf or u.email == user.email]

        if len(search_results) > 0:
            return print("O CPF ou o Email informado já foi cadastrado!")

        user.user_id = UserMockup.get_next_id()
        UserMockup.user_list.append(user)

    @staticmethod
    def delete_user(*, id: int):
        user = UserMockup.get_user(id=id)

        if user:
            UserMockup.user_list.remove(user)
            print(f"Usuário de id {id} foi deletado com sucesso!")
        else:
            print(f"Id {id} não encontrado!")

    @staticmethod
    def login_user(*, email, password):
        user = [u for u in UserMockup.user_list if u.email == email and u._password == password]

        if len(user) == 0:
            return False
        
        return user[0].user_id