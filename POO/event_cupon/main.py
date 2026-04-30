from user import User
from db import EVENTOS, CUPONS, USUARIOS


usuario1 = User.criar_usuario('joao', '123', 'joao@email.com')
usuario2 = User.criar_usuario('maria', '456', 'maria@email.com')

print("=== Sistema de Eventos e Cupons ===\n")


print("--- Usuário 1 criando evento ---")
evento1 = usuario1.criar_evento("Show de Rock", "Banda ao vivo", "31/12/2025", "Parque Central", 100.0)

print("\n--- Usuário 2 criando evento ---")
evento2 = usuario2.criar_evento("Workshop Python", "Aprenda Python", "15/11/2025", "Centro de Convenções", 200.0)


print("\n--- Criando cupons ---")

usuario1.criar_cupom("PROMO_VERAO", 0, "30/12/2025", evento1.id)

usuario2.criar_cupom("DESCONTO_VIP", 10, "14/11/2025", evento2.id)


print("\n--- Eventos cadastrados ---")
for evento in User.listar_eventos():
    print(evento, "\n")


print("--- Usuário 1 tentando editar evento do usuário 2 ---")
usuario1.editar_evento(evento2.id, titulo="Hackeado!")


print("\n--- Usuário 1 editando seu próprio evento ---")
usuario1.editar_evento(evento1.id, local="Anfiteatro Municipal")

print("\n--- Usuário 2 deletando cupom ---")
usuario2.deletar_cupom(1)


print("\n--- Cupons restantes ---")
for cupons in User.listar_cupons():
    print(cupons, "\n")

print("--- Usuários cadastrados ---")
for users in User.listar_usuarios():
    print(users, "\n")

