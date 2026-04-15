from user import User
from db import USERS
from cars import Car, CARS
class Admin(User):

    def __init__(self, id, username, password, email, superuser):
        super().__init__(id, username, password, email)
        self.superuser = superuser

    def __repr__(self):
        return f'admin_id :{self.id}, \n admin_username :{self.username}, \n admin_email :{self.email},admin_password : {self.password},\n is_admin :{self.superuser}'

    @classmethod
    def create_user(cls, username, password, email):
        new_user = User(
            id=len(USERS) + 1,
            username=username,
            password=password,
            email=email
        )
        new_user.add()
        return new_user

    @classmethod
    def create_admin(cls, username, password, email):
        new_admin = Admin(
            id=len(USERS) + 1,
            username=username,
            password=password,
            email=email,
            superuser=True
        )
        new_admin.add()
        return new_admin

    @classmethod
    def update(cls, id, username, password, email):
        index = id -1
        update_user = USERS [index]
        if isinstance(update_user, Admin):
           USERS[index] = Admin(id, username , password , email , superuser=True)
        if isinstance(update_user, User):
            USERS[index] = User(id, username , password, email)

    @classmethod
    def get_user_by_id(cls, id):
        for user in USERS:
            if user.id == id:
                return user
        return None

    @classmethod
    def get_all_users(cls):
        return USERS

    @classmethod
    def delete(cls, id):
        del USERS[id -1]
    
    
    def create_car(self, modelo, ano, cor):
        carro = {"modelo": modelo, "ano": ano, "cor": cor}
        self.meus_carros.append(carro)
        print(f"Carro {modelo} adicionado com sucesso!")

    def update_car(self, indice, modelo=None, ano=None, cor=None):
        if 0 <= indice < len(self.meus_carros):
            if modelo: self.meus_carros[indice]['modelo'] = modelo
            if ano: self.meus_carros[indice]['ano'] = ano
            if cor: self.meus_carros[indice]['cor'] = cor
            print("Carro atualizado!")
        else:
            print("Carro não encontrado.")

    def delete_car(self, id):
        if 0 <= id < len(self.meus_carros):
            removido = self.meus_carros.pop(id)
            print(f"Carro {removido['modelo']} removido.")
        else:
            print("id inválido.")

        

  

    
