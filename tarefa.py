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



