from admin import Admin
from user import User


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