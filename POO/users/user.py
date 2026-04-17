from db import USERS, CARS
from cars import Car

class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email


    def add(self):
        USERS.append(self)
       

    def __repr__(self):
        return f"user_id:{self.id}, \n username:{self.username}, \n user_email :{self.email}, \n user_password :{self.password},\n is_admin : False"
    
    def update_username(self, username):
        user = User.get_user_by_id(self.id)
        if user:
            user.username = username
            return user
        return 'Usuário não encontrado'
    
    def update_password(self, password):
        user = User.get_user_by_id(self.id)
        if user:
            user.password = password
            return user
        return 'Usuário não encontrado'
    
    def update_email(self, email):
        user = User.get_user_by_id(self.id)
        if user:
            user.email = email
            return user
        return 'Usuário não encontrado'
    

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
