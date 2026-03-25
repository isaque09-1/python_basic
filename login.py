from db import USERS
from encyption import decrypt_password

def find_by_username(username):
    for user in USERS:
        if user ['username'] == username:
            return user
        return None
    
def login(username, password):
    user =find_by_username(username)
    if user is None:
        return 'usuario nao encontrado'
    decrypt_password = decrypt_password(user[password])
    if decrypt_password == password:
        return 'Login realizado com sucesso'
    return'login incorreto'
    