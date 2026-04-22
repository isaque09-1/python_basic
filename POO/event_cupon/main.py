from admin import Admin
from db import EVENTOS, CUPONS , USUARIOS


usuario = Admin.criar_usuario('joao', '123', 'joao@email.com')
admin   = Admin.criar_admin('maria', '456', 'maria@email.com')

print("=== Sistema de Eventos e Cupons ===\n")


print("--- Usuário criando evento ---")
evento1 = usuario.criar_evento("Show de Rock", "Banda ao vivo", "31/12/2025", "Parque Central", 80.0)

print("\n--- Admin criando evento ---")
evento2 = admin.criar_evento("Workshop Python", "Aprenda Python", "15/11/2025", "Centro de Convenções", 150.0)


print("\n--- Criando cupons ---")
usuario.criar_cupom("PROMO_VERAO", 20.0, "30/12/2025", evento1.id)
admin.criar_cupom("DESCONTO_VIP", 50.0, "14/11/2025", evento2.id)


print("\n--- Eventos cadastrados ---")
for e in Admin.listar_eventos():
    print(e, "\n")


print("--- Usuário tentando editar evento do admin ---")
usuario.editar_evento(evento2.id, titulo="Hackeado!")


print("\n--- Usuário editando seu próprio evento ---")
usuario.editar_evento(evento1.id, local="Anfiteatro Municipal")

print("\n--- Admin deletando cupom ---")
admin.deletar_cupom(1)


print("\n--- Cupons restantes ---")
for c in Admin.listar_cupons():
    print(c, "\n")

print("--- Usuários cadastrados ---")
for u in Admin.listar_usuarios():
    print(u, "\n")