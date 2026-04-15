from admin import Admin
from user import User
from cars import Car

print('criacao  ')
new_user =Admin.create_user('carlos','carlin123','carlao@gmail.com')
print(new_user)

new_admin= Admin.create_admin('Roberto','Roberto123','roberto@gmail.com')
print(new_admin)


print('atualizacao ')


Admin.update(new_user.id, 'kelwin','kelwinzin12','kelwinz@gmail.com')
Admin.update(new_admin.id,'pedro','pedro12','pedro@gmail.com')

print(Admin.get_all_users())


print('delecao ')

Admin.delete(1)
print(Admin.get_all_users())


print("==================CREATE CAR =============================")

new_car =Admin.admin_create_car(4 , 'ford','fiesta',1990,'branco')
print(new_car)


new_car1= Admin.user_create_car(5 , 'honda', 'city',2005,'preto')
print(new_car1)

r1= Admin.delete_car()