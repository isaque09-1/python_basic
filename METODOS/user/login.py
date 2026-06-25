from db import USERS
from encyption import decrypt_password

async def find_by_username(username):
    for user in USERS:
        if user['username'] == username:
            return user
    return None
    

async def login(username, password):
    user = await find_by_username(username)
    if user is None:
        return 'Usuário não encontrado'
    decrypted_password =await decrypt_password(user['password'])
    if decrypted_password == password:
        return 'Login realizado com sucesso'
    return 'Login falhou'