from crud import create_user, update_user, remove_user, list_users
from login import login
import asyncio


async def ask(prompt):
    return await asyncio.to_thread(input, prompt)


async def main():
    while True:
        opcao = await ask(
            'SISTEMA DE CADASTRO DE USUÁRIOS...\n'
            'Digite uma das opções a seguir:  \n'
            '1 - criar um novo usuário \n'
            '2 - atualizar um usuário \n'
            '3 - listar todos os usuários \n'
            '4 - remover um usuário \n'
            '5 - login \n'
            '0 - sair do programa \n'
        )

        match opcao.strip():
            case '0':
                print('Saindo do programa...')
                return

            case '1':
                username = await ask('Digite o username: ')
                password = await ask('Digite a Password: ')
                email = await ask('Digite o email: ')
                print(await create_user(username, email, password))

            case '2':
                user_id = int(await ask('Digite o id do usuário: '))
                username = await ask('Digite o username: ')
                password = await ask('Digite a Password: ')
                email = await ask('Digite o email: ')
                print(await update_user(user_id, username, email, password))

            case '3':
                print(await list_users())

            case '4':
                user_id = int(await ask('Digite o id do usuário: '))
                print(await remove_user(user_id))

            case '5':
                username = await ask('Digite o Username: ')
                password = await ask('Digite a Password: ')
                print(await login(username, password))

            case _:
                print('Opção inválida. Tente novamente.')


if __name__ == '__main__':
    asyncio.run(main())

