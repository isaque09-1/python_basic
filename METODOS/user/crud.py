from db import USERS
from validations import validate_email
from encyption import encyption_password


def list_users():
    return [user for user in USERS]



def create_user(username, email, password):
    if not validate_email(email):
        return 'Email inválido'
    password_hash = encyption_password(password)
    
    id = len(USERS) + 1
    new_user = {
        'id': id,
        'username': username,
        'email': email,
        'password': password
    }
    USERS.append(new_user)
    return 'Usuário criado com sucesso'


def update_user(id, username, email, password):
    if not validate_email(email):
        return 'Email inválido'
    password_hash = encyption_password(password)
    USERS[id -1] = {
        'id': id,
        'username': username,
        'email': email,
        'password': password
    }
    return 'Usuário atualizado com sucesso'


def remove_user(id):
    USERS.pop(id -1)#pop metodo na lista para remover pelo index
    return 'Usuario removido com sucesso'
print(USERS)
remove_user(2)#remove o usuario com o index 1
print(USERS)

