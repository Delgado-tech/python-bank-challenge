> A versão 2.0 do projeto Bank Rev deve contemplar os seguintes requisitos abaixo:

## Geral:

- [x] Criar um novo menu para se cadastrar ou entrar no serviço
- [ ] Alteração de funções já existentes
- [x] Criar funções: `cadastrar usuário` (cliente do banco) e `cadastrar conta bancária` (vincular com usuário)

## Funções:

### Saque (Alteração):

- [ ] Criar uma função separada para fazer a operação
- [ ] A função deve receber os argumentos apenas por nome (keyword only)

### Deposito (Alteração):

- [ ] Criar uma função separada para fazer a operação
- [ ] A função deve receber os argumentos apenas por posição (positional only)

### Visualizar Extrato (Alteração):

- [ ] Criar uma função separada para fazer a operação
- [ ] A função deve receber uma parte dos argumentos por posição e a outra por nome

### Cadastrar usuário (NOVO):

- [x] Armazenar o usuário em uma lista, um usuário é composto por: `nome, data_de_nascimento, cpf e endereço`
- [x] O campo endereço é uma string com o formato: `logradouro, número - bairro - cidade/sigla_estado`
- [ ] O campo CPF deve armazenar somente os números
- [x] NÃO deve ser possível cadastrar dois usuários com o mesmo CPF

### Criar conta corrente (NOVO):

- [x] Armazenar as contas em uma lista, uma conta é composta por: `agência, número_da_conta, usuário`
- [x] O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001"
- [x] O usuário pode ter mais de uma conta
- [x] A conta só pode ter apenas um usuário

### Visualizar usuários existentes (NOVO)

- [ ] Mostrar todos usuários registrados em ordem alfabetica

### Visualizar contas existentes (NOVO)

- [x] Mostrar todas as contas existentes ordenado por agência

### Pesquisar Usuário (NOVO)

- [x] Listar todas as informações do usuário junto com todas as contas vinculadas em seu nome ao pesquisar por seu id
