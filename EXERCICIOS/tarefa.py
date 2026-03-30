diaS = str(input("Digite o dia da semana: ")).lower().strip()

if diaS == "segunda" or diaS == "terça" or diaS == "quarta" or diaS == "quinta" or diaS == "sexta":
    print("É dia de semana")
else:
    print("Não é dia de semana")

idade = 18
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir")
elif idade >= 18 and not tem_carteira:
    print("Não pode dirigir, falta a carteira")
else:    print("Não pode dirigir, falta a idade")


altura = 1.75

if altura < 1.40:
    print("ANAO")
elif altura >= 1.40 and altura < 1.60:
    print("BAIXO")
elif altura >= 1.60 and altura < 1.80:
    print("MEDIO")
elif altura >= 1.80 and altura < 2.00:
    print("ALTO")
else:    
    print("GIGANTESCO")







usuario_salvo = "admin"
senha_salva = "1234"


usuario_input = input("Usuário: ")
senha_input = input("Senha: ")

if usuario_input == usuario_salvo and senha_input == senha_salva:
    print("LOGIN BEM SUCEDIDO")
elif usuario_input == usuario_salvo and senha_input != senha_salva:
    print("SENHA INCORRETA")
elif senha_input == senha_salva and usuario_input != usuario_salvo:
    print("USUÁRIO INCORRETO")
else:
    print("USUÁRIO E SENHA INCORRETOS")



anos_empresa = int(input("Anos de empresa: "))
escolaridade = input("Escolaridade (graduacao/pos/mestrado): ").lower()
bom_historico = input("Possui bom histórico? (sim/nao): ").lower() == "sim"

if escolaridade == "mestrado" and anos_empresa > 10 and bom_historico:
    print("Pode ser GERENTE GERAL")
elif escolaridade == "pos" and anos_empresa > 8 and bom_historico:
    print("Pode ser GERENTE DO SETOR")
elif escolaridade == "graduacao" and anos_empresa > 5 and bom_historico:
    print("Pode ser SUPERVISOR")
else:
    print("Não elegível para promoção no momento.")



