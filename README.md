# Desafio Python

O desafio proposto consiste na criação de um sistema bancario simples com as opções `sacar`, `depositar` e `visualizar extrato`.

### Regras de negócio:

1. Os usuários que realizarem a operação `sacar` só podem realizar 3 saques por dia, onde cada um deve ser de no máximo R$500;
2. Ao realizar a operações `sacar` ou `depositar`, deve-se armazenado o valor e a data/hora da operação para posteriormente poder ser visualizada na operação `visualizar extrato`;
3. A operação `visualizar extrato` deve listar os registros por data em ordem decrescente no terminal (a data mais antiga até a mais atual).

## Funcionalidades

### Sacar (Withdraw)

> #### Etapas
>
> 1 - Verificação de Saques Diários:
>
> Antes de efetuar um saque, o sistema verifica a quantidade de saques diários disponíveis. Se essa quantidade estiver esgotada, é verificado se a última regeneração ocorreu na data atual. Em caso afirmativo, os saques diários são automaticamente regenerados, restabelecendo o valor máximo permitido.
>
> 2 - Solicitação de Valor de Saque:
>
> O usuário é então solicitado a inserir o valor desejado para o saque. Se o valor informado for zero, a operação é cancelada. Se o valor exceder R$500 ou não for um número válido, uma mensagem é exibida, alertando sobre a invalidade dos valores.
>
> 3 - Processamento de Saque Válido:
>
> Caso o valor informado seja válido, o número de saques diários restantes é reduzido, o saldo do usuário é diminuido, e os detalhes da transação, incluindo valor e data/hora, são armazenados em uma variável de extrato.
> ‎![image](https://github.com/Delgado-tech/python-bank-challenge/assets/60985347/f9752e74-0f45-40a8-b11b-05a857435845)


### Depositar (Deposit)

> #### Etapas
>
> 1 - Solicitação de Valor de Deposito
>
> O usuário é solicitado a inserir o valor para o deposito. Se o valor informado for zero, a operação é cancelada. Se o valor não for um número válido, uma mensagem é exibida, alertando sobre a invalidade do valor.
>
> 2 - Caso o valor informado seja válido, o saldo do usuário é aumentado, e os detalhes da transação, incluindo valor e data/hora, são armazenados em uma variável de extrato.
> ‎

### Visualizar Extrato (View Statement)

> É carregado as informações armazenadas da lista de extrato e exibida no terminal em ordem descrescente ordenada pela data/hora, também é mostrado o número total de saques e depositos realizados pela conta.

<br>

## Getting Started

### Pre-requisitos

Para rodar o projeto é necessário ter instalado em sua máquina o `Python v3.12.2+`, você pode realizar a instalação dele [aqui](https://www.python.org/downloads/).

### Instalação

#### Clonando o repositório

```bash
$ git clone https://github.com/Delgado-tech/python-bank-challenge.git
$ cd python-bank-challenge
```

#### Seleção do ambiente virtual

Para configurar o ambiente virtual do projeto no VSCode, siga os passos abaixo:

> 1 - Pressione `[Ctrl+P]` para abrir a caixa de comandos.
>
> 2 - Digite `> Python: Select Interpreter` e pressione `[Enter]`.
>
> 3 - Uma janela será exibida, nela clique na opção `Python 3.12.2 ('.venv':venv)`.

Com essas etapas concluídas, você estará utilizando o ambiente virtual do projeto.

### Inicialização

Com seu projeto configurado, abra o terminal do seu VSCode e rode o comando:

```shell
$ python main.py
```

Se tudo funcionou aparecera o menu da aplicação no seu terminal:

![image](https://github.com/Delgado-tech/python-bank-challenge/assets/60985347/f12b2735-782c-440e-8c68-bd49dee5d8d1)


Pronto! Agora você pode se divertir com o projeto!
