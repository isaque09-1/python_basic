from admin import Admin
from user import User
from db import CARS, USERS
<<<<<<< HEAD

user = Admin.create_user('joao', '123', 'joao@email.com')
admin = Admin.create_admin('maria', '456', 'maria@email.com')
print("\nTodos usuarios cadastrados sao :")
print(f'\n users criados : {user}\n')
print(f'\n admins criados : {admin}\n')
=======
>>>>>>> 31bfd6a19a15db35d37669f6078ef76ae7cae860

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
<<<<<<< HEAD
user.update_car(1, modelo="Palio")
=======
>>>>>>> 31bfd6a19a15db35d37669f6078ef76ae7cae860

print("\nAdmin deletando carro:")
admin.delete_car(2)

print("\nCarros finais:")
for car in CARS:
<<<<<<< HEAD
    print(car)
=======
    print(car)

print("\nUsuarios cadastrados:")
for user in USERS:
    print(user)
>>>>>>> 31bfd6a19a15db35d37669f6078ef76ae7cae860
