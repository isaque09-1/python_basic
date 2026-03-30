pessoas = [
    {"nome": "João", "idade": 25},
    {"nome": "Maria", "idade": 30},
    {"nome": "Pedro", "idade": 20},
]

nomes = []
nomes.append(pessoas[0]["nome"])
nomes.append(pessoas[1]["nome"])
nomes.append(pessoas[2]["nome"])


nomes = []
idade = []

for pessoa in pessoas:
    nomes.append(pessoa["nome"])
    idade.append(pessoa["idade"])
    print(f'nome: {pessoa["nome"]}, idade: {pessoa["idade"]}')


nomes = [pessoa["nome"] for pessoa in pessoas]
idade = [pessoa["idade"] for pessoa in pessoas]

print(nomes)


users = [
    {"id": 1, "name": "antonio", "active": True},
    {"id": 2, "name": "maria", "active": False},
    {"id": 3, "name": "pedro", "active": True},
    {"id": 4, "name": "ana", "active": False},
    {"id": 5, "name": "lucas", "active": True},
    {"id": 6, "name": "carla", "active": False},
    {"id": 7, "name": "julia", "active": True},
    {"id": 8, "name": "roberto", "active": False},
]

active_users = [user["name"] for user in users if user["active"]]
inactive_users = [user["name"] for user in users if not user["active"]]
names = [user["name"] for user in users]

print(f'NOME DE TODOS OS USUÁRIOS:\n {names}\n')
print(f'USUÁRIOS ATIVOS:\n {active_users}\n')
print(f'USUÁRIOS INATIVOS:\n {inactive_users}\n')


id_all = []
id_active = []
id_inactive = []

id_all = [user["id"] for user in users]
id_active = [user["id"] for user in users if user["active"]]
id_inactive = [user["id"] for user in users if not user["active"]]

print(f'ID DE TODOS OS USUÁRIOS:\n {id_all}\n')
print(f'ID DE USUÁRIOS ATIVOS:\n {id_active}\n')
print(f'ID DE USUÁRIOS INATIVOS:\n {id_inactive}\n')


prices = [100, 250, 305, 470, 580]

for price in prices:
    print(f'Preço original: {price}')
    print(f'Desconto de 10%: {price * 0.9}')
    print(f'Desconto de 20%: {price * 0.8}')
    print(f'Desconto de 30%: {price * 0.7}')
    print(f'Desconto de 40%: {price * 0.6}')
    print(f'Desconto de 50%: {price * 0.5}\n')


raw_emails = [
    "JOAO@gmail.com",
    "MarIA@gmail.com",
    " K e l  W   i n@gmail.com",
    "T I g  a  s  d  oM  a u  @gmail.com"
]

striped_emails = [email.strip() for email in raw_emails]
print(f'EMAILS SEM ESPAÇOS EM BRANCO:\n {striped_emails}\n')

lower_emails = [email.lower() for email in raw_emails]
print(f'EMAILS EM LETRAS MINÚSCULAS:\n {lower_emails}\n')


emails = [
    "     JO AO      @gmail.com",
    "M a rIA  @gmail.com",
    " K e l  W   i n@gmail.com",
    "T I g  a  s  d  oM  a u  @gmail.com"
]

emails_limpos = [
    email.lower()
    .replace(" ", "")
    for email in emails
]
print(f'EMAILS LIMPOS:\n {emails_limpos}\n')


for i in range(5):
    print(f'Número: {i}')

for i in range(1, 6):
    print(f'Número: {i}')

for i in range(0, 10, 2):
    print(f'Número: {i}')

for i in range(10, 0, -2):
    print(f'Número: {i}')

for i in range(30):
    if i % 2 == 0:
        print(f'Número par: {i}')
    else:
        print(f'Número ímpar: {i}')


cadastro = [
    {"username": "joao", "password": "123456"},
    {"username": "maria", "password": "654321"},
    {"username": "pedro", "password": "676767"}
]


def login(username, password):
    for user in cadastro:
        if user["username"] == username and user["password"] == password:
            return "Login bem-sucedido!"
    return "Credenciais inválidas."


if login(input("Digite seu login: "), input("Digite sua senha: ")) == "Login bem-sucedido!":
    print("Bem-vindo ao sistema!")
else:
    print("Tente novamente.")
