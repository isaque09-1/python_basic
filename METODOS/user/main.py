
from crud import (create_user,update_user,remove_user,list_users)
from login import login

opcao = ''
while True:
    print('=-'*14)
    opcao =int(input(
        'Qual a opçao vc quer :\n' 
        '1 - criar usuario:\n'
        '2- atualizar usuario:\n'
        '3- listar todos os os usuarios:\n'
        '4-Remover usuario: \n'
        '5- login :\n'
        '0- sair:\n'
        'Escolha: '
    ))
    if opcao == 1:
        username = input("digite seu nome : \n")
        password = input( "Digite sua senha :\n")
        email = input("digite seu email :\n")
        print(create_user(username, password, email))
    
    elif opcao == 2 :
        print("Atualizado")
    
    elif opcao == 3 :
        print(list_users)

    elif opcao == 4 :
        user_id = int(input('Digite o ID do usuario : '))
        remove_user(user_id)
    
    elif opcao == 5 :
        username = input("digite seu nome : ")
        password = input("digite sua senha : ")
        print(login(username , password))
    
    elif opcao == 0 :
        break

    else:
        print("opcao invalida")

  

