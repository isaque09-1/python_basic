from user import User
from db import USERS, CARS
from cars import Car

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
    

    def create_car(self, id, marca, modelo, ano, cor):
        new_car = Car(id, marca, modelo, ano, cor)
        CARS.append(new_car)
        print(f"Carro criado com sucesso pelo administrador {self.username}!")
        print(f"Detalhes : id = {new_car.id}, marca = {new_car.marca}, modelo = {new_car.modelo}, ano = {new_car.ano}, cor = {new_car.cor}")
        
    
    def delete_car(self, car_id):
        car_to_delete = None
        for car in CARS:
            if car.id == car_id:
                car_to_delete = car
                break
        
        if car_to_delete:
            CARS.remove(car_to_delete)
            print(f"Carro com ID {car_id} deletado com sucesso pelo administrador {self.username}!")
        else:
            print(f"Carro com ID {car_id} não encontrado!")
    
    def update_car(self, car_id, marca=None, modelo=None, ano=None, cor=None):
        car_to_update = None
        for car in CARS:
            if car.id == car_id:
                car_to_update = car
                break
        
        if car_to_update:
            if marca:
                car_to_update.marca = marca
            if modelo:
                car_to_update.modelo = modelo
            if ano:
                car_to_update.ano = ano
            if cor:
                car_to_update.cor = cor
            print(f"Carro com ID {car_id} atualizado com sucesso pelo administrador {self.username}!")
            return car_to_update
        else:
            print(f"Carro com ID {car_id} não encontrado!")
