from admin import Admin
from user import User
from db import CARS, USERS

user = Admin.create_user('joao', '123', 'joao@email.com')
admin = Admin.create_admin('maria', '456', 'maria@email.com')

print("=== Sistema de Carros ===")

print("\nUsuario criando carro:")
user.create_car(1, "Fiat", "Uno", 2020, "Branco")

print("\nAdmin criando carro:")
admin.create_car(2, "BMW", "X1", 2021, "Preto")

print("\nCarros cadastrados:")
for car in CARS:
    print(car)

print("\nUsuario atualizando carro:")
user.update_car(1, cor="Azul")

print("\nAdmin deletando carro:")
admin.delete_car(2)

print("\nCarros finais:")
for car in CARS:
    print(car)

print("\nUsuarios cadastrados:")
for user in USERS:
    print(user)
