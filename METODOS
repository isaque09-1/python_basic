"""Metodos sao blocos de codigos que realizam
uma tarefa especifica, eles podem receber parametros de entrada e retornar um resultado.
em diferentes partes do programa . eles sao definidos 
usando a palavra "def" seguida do nome do metodo e parenteses, onde podem ser definidos os parametros de entrada.
os parametros sao variaveis que sao passadas
para o metodo quando ele e chamado, e podem ser usados dentro do metodo para realizar a tarefa especifica.

def saudacao (nome):
    print(f'Ola, {nome}!')

saudacao('pedrin')
saudacao('kelwin')
saudacao('maria')
saudacao('joao')
saudacao('erick')
"""
cadastro = [
    {
        "username": "joao",
        "password": "123456"
    },
    {
        "username": "maria",
        "password": "654321"
    },
    {
        "username": "pedro",
        "password": "676767"
    }
]

def formatacao(username):
    return username.replace(' ', "").lower()


def cadastrar(valid_username, password):
    valid_username = formatacao(valid_username)
    print(valid_username)
    for usuario in cadastro:
        if usuario["username"] == valid_username:
          return"Usuario ja cadastrado"
    cadastro.append({"username": valid_username, "password": password,})
    return "Usuario cadastrado com sucesso"   

print(cadastrar("joao", "123456"))
print(cadastrar("rogerio","peixe123"))
print(cadastrar("m  aria", "654321"))


def update_password(lista,username, new_password):
    valid_username = formatacao(username)
    for user in lista:
        if user["username"] == valid_username:
            user["password"] = new_password
            return "Senha atualizada com sucesso"
            return "Usuario nao encontrado"
print(update_password(cadastro, "pedro", "newpassword123"))



usuario=[
   {
        "username": "joao",
        "password": "123456",
        "id": 1
    
    },
    {
        "username": "paulin",
        "password": "654321",
        "id":2
    },
    {
        "username": "rodolfo",
        "password":"password13",
        "id":3
    },
    {
        "username":"kelwin",
        "password": "yoga",
        "id":4
    },
    {
        "username": "maria",
        "password": "432111",
        "id":5
    },  
]
def formatacao(username):
    return username.replace(' ', "").lower()


def register_user(username, password):
    valid_username = formatacao(username)
    for user in usuario:
        if user["username"] == valid_username:
            if user ["password"] == update_password(usuario, valid_username, password):
                return "Username and password updated successfully"
            return "Usuario ja cadastrado"
    usuario.append({"username": valid_username, "password": password})
    return "Usuario cadastrado com sucesso"


print(register_user("joao", "123456"))
