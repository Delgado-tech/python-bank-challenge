import calendar
import re
import validate_cpf

from datetime import datetime
from controllers.address import Address
from controllers.session import Session
from controllers.user import User
from mocks.user_mockup import UserMockup
from utils.clamp import clamp
from utils.date.console_current_time import console_current_time
from utils.parse_int import parse_int
from views.style import Fore_Style


def home_page_user_register(_):
    from views.home.page import home_page
    from views.user.page import user_page

    print(Fore_Style.PRIMARY.value, f"""
============================================
    Cadastrar
    {console_current_time()}
    
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
        value = input(f"{Fore_Style.SECONDARY.value}{key}: {Fore_Style.WHITE.value}")

        if value.upper() == "C":
            return home_page, False
        
        if value.upper() == "X":
            return False, False
        
        if key == "CPF":
            formated = re.findall("\d+", value)
            if len(formated) > 0:
                value = formated[0]
                if UserMockup.get_user(cpf=value):
                    input(f"\n{Fore_Style.DANGER.value}O CPF informado já está em uso!")
                    return home_page_user_register, False
                
                if validate_cpf.is_valid(value) == False:
                    input(f"\n{Fore_Style.DANGER.value}O CPF informado é inválido")
                    return home_page_user_register, False  
            else:
                input(f"\n{Fore_Style.DANGER.value}O CPF informado é inválido")
                return home_page_user_register, False  
        elif key == "E-mail":
            value = value.replace(" ", "")
            if UserMockup.get_user(email=value):
                input(f"\n{Fore_Style.DANGER.value}O E-mail informado já está em uso!")
                return home_page_user_register, False
        
        inputs[key] = value

    password = input("Senha: ")

    bday_year = clamp(parse_int(inputs["Data de Nascimento (Ano)"]), 1900, datetime.now().year - 18)
    bday_month = clamp(parse_int(inputs["Data de Nascimento (Mês)"]), 1, 12)
    bday_day = clamp(parse_int(inputs["Data de Nascimento (Dia)"]), 1, calendar.monthrange(bday_year, bday_month)[1])

    result = UserMockup.register_user(
        user=User(
            email=inputs["E-mail"], 
            password=password, 
            name=inputs["Nome"], 
            cpf=inputs["CPF"], 
            birtdate=datetime( 
                bday_year,
                bday_month,
                bday_day
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
        return home_page_user_register, False
    
    Session.user_id = result

    input(f"{Fore_Style.SUCCESS.value}\nUsuário cadastrado com sucesso!")
    return user_page, False
