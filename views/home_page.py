import re
from validate_cpf import validate_cpf

from datetime import datetime
from controllers.address import Address
from controllers.session import Session
from controllers.user import User

from mocks.user_mockup import UserMockup
from utils.clamp import clamp
from utils.parse_int import parse_int
from views.user_page import user_page


def home_page_index(option: str):
    print(f"""
============================================
    Seja bem-vindo ao Banco Rev!
    {datetime.now().strftime("%d/%m/%Y %H:%M")}
    
    Escolha uma opção:
    
    [1] Entrar
    [2] Cadastrar
    
    [x] Fechar Aplicação \n
============================================
    """)

    return home_page, option

def home_page_login(_):

    print(f"""
============================================
    Entrar
    {datetime.now().strftime("%d/%m/%Y %H:%M")}
    
    [c] Cancelar
    [x] Fechar Aplicação
    \n
============================================
""")
    
    value = input("E-mail: ")

    if value.upper() == "C":
        return home_page, False
    
    if value.upper() == "X":
        return False, False
    
    email = value.lower()

    password = input("Senha: ")

    user_id = UserMockup.login_user(email=email, password=password)

    if user_id == False:
        input("\nE-mail ou Senha inválido!")
        return home_page_login, False

    Session.user_id = user_id

    return user_page, False

def home_page_register(_):
    print(f"""
============================================
    Cadastrar
    {datetime.now().strftime("%d/%m/%Y %H:%M")}
    
    [c] Cancelar
    [x] Fechar Aplicação
    \n
============================================
""")
    
    inputs = {
        "E-mail": "",
        "CPF": "",
        "Nome": "",
        "Data de Nascimento (Dia)": "",
        "Data de Nascimento (Mês)": "",
        "Data de Nascimento (Ano)": "",
        "Endereço (Rua)": "",
        "Endereço (Número)": "",
        "Endereço (Bairro)": "",
        "Endereço (Cidade)": "",
        "Endereço (Sigla Estado)": "",
    }

    for key, value in inputs.items():
        value = input(f"{key}: ")

        if value.upper() == "C":
            return home_page, False
        
        if value.upper() == "X":
            return False, False
        
        if key == "CPF":
            formated = re.findall("\d+", value)
            if len(formated) > 0:
                value = formated[0]
                if UserMockup.get_user(cpf=value):
                    input("\nO CPF informado já está em uso!")
                    return home_page_register, False
                
                if validate_cpf.is_valid(value) == False:
                    input("\nO CPF informado é inválido")
                    return home_page_register, False  
            else:
                input("\nO CPF informado é inválido")
                return home_page_register, False  
        elif key == "E-mail":
            value = value.replace(" ", "")
            if UserMockup.get_user(email=value):
                input("\nO E-mail informado já está em uso!")
                return home_page_register, False
        
        inputs[key] = value

    password = input("Senha: ")

    result = UserMockup.register_user(
        user=User(
            email=inputs["E-mail"], 
            password=password, 
            name=inputs["Nome"], 
            cpf=inputs["CPF"], 
            birtdate=datetime( 
                clamp(parse_int(inputs["Data de Nascimento (Ano)"]), 1900, datetime.now().year - 18), 
                clamp(parse_int(inputs["Data de Nascimento (Mês)"]), 1, 12),
                clamp(parse_int(inputs["Data de Nascimento (Dia)"]), 1, 31),
            ), 
            address=Address(
                street=inputs["Endereço (Rua)"],
                number=inputs["Endereço (Número)"],
                neighborhood=inputs["Endereço (Bairro)"],
                city=inputs["Endereço (Cidade)"],
                state=inputs["Endereço (Sigla Estado)"].upper()
            ),
        )
    )

    if result == False:
        return home_page_register, False
    
    Session.user_id = result

    print("Usuário cadastrado com sucesso!")
    return user_page, False

def home_page(option: str):

    DISPLAY_SCREEN = {
        "1": home_page_login,
        "2": home_page_register
    }

    return DISPLAY_SCREEN.get(option, home_page_index)(option)