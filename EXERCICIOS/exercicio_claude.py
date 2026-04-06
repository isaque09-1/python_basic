# =============================================================================
#  EXERCÍCIOS BÁSICOS DE PYTHON
#  Feitos e corrigidos com auxílio do Claude
# =============================================================================


# -----------------------------------------------------------------------------
# EXERCÍCIO 1 — Par ou ímpar
# -----------------------------------------------------------------------------
# ENUNCIADO:
#   Peça ao usuário um número inteiro.
#   Exiba "par" se for divisível por 2, ou "ímpar" caso contrário.
#
# CONCEITOS USADOS: input(), int(), if/else, operador % (módulo)
# -----------------------------------------------------------------------------

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"{numero} é PAR")
else:
    print(f"{numero} é ÍMPAR")


# -----------------------------------------------------------------------------
# EXERCÍCIO 2 — Calculadora de média
# -----------------------------------------------------------------------------
# ENUNCIADO:
#   Peça 3 notas ao usuário. Calcule a média.
#   Exiba "Aprovado" se média >= 7,
#          "Recuperação" se entre 5 e 6.9,
#          "Reprovado" se abaixo de 5.
#
# CONCEITOS USADOS: input(), float(), if/elif/else, operadores lógicos (and)
# -----------------------------------------------------------------------------

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))

soma  = n1 + n2 + n3
media = soma / 3

print(f"Média: {media:.1f}")  # :.1f exibe apenas 1 casa decimal

if media >= 7:
    print("Aprovado")
elif media >= 5 and media <= 6.9:
    print("Recuperação")
else:
    print("Reprovado")


# -----------------------------------------------------------------------------
# EXERCÍCIO 3 — Lista de compras
# -----------------------------------------------------------------------------
# ENUNCIADO:
#   Crie uma lista vazia. Peça ao usuário para digitar 4 itens (um por vez)
#   e adicione cada um à lista. Ao final, exiba a lista completa e quantos
#   itens ela tem.
#
# CONCEITOS USADOS: lista, append(), len(), for, range()
# -----------------------------------------------------------------------------

lista = []  # lista vazia

for i in range(4):
    item = input(f"Digite o item {i + 1}: ")
    lista.append(item)  # adiciona o item na lista

print("Lista de compras:", lista)
print("Total de itens:", len(lista))


# -----------------------------------------------------------------------------
# EXERCÍCIO 4 — Tupla de dias da semana
# -----------------------------------------------------------------------------
# ENUNCIADO:
#   Crie uma tupla com os 7 dias da semana. Peça ao usuário um dia.
#   Verifique se ele está na tupla e se é fim de semana (Sábado ou Domingo).
#   Exiba mensagens adequadas para cada caso.
#
# CONCEITOS USADOS: tupla, in, if/elif/else, operadores lógicos (or),
#                   lower(), strip()
# -----------------------------------------------------------------------------

diaS   = ("segunda", "terca", "quarta", "quinta", "sexta")
finalS = ("sabado", "domingo")

# .lower() converte para minúsculo, .strip() remove espaços extras
dia = input("Que dia é hoje? ").lower().strip()

if dia in diaS:
    print(f"{dia} é dia de semana.")
elif dia in finalS:
    print(f"{dia} é fim de semana!")
else:
    print("Dia inválido. Digite um dia da semana em português.")


# -----------------------------------------------------------------------------
# EXERCÍCIO 5 — Filtrar números pares de uma lista
# -----------------------------------------------------------------------------
# ENUNCIADO:
#   Dada a lista [3, 8, 15, 4, 22, 7, 10, 1], crie uma nova lista contendo
#   apenas os números pares. Exiba a lista original, a lista filtrada e a
#   soma dos pares.
#
# CONCEITOS USADOS: lista, for, if, append(), sum(), operador %
# -----------------------------------------------------------------------------

lista = [3, 8, 15, 4, 22, 7, 10, 1]
par   = []  # lista vazia para guardar os pares

for i in lista:
    if i % 2 == 0:       # verifica se o número é par
        par.append(i)    # adiciona o número par na nova lista

print("Lista original:", lista)
print("Números pares:", par)
print("Soma dos pares:", sum(par))


# =============================================================================
#  FIM DOS EXERCÍCIOS
# =============================================================================

'''
#====================================================================================
 Você concluiu todos os 5 exercícios! Aqui vai um resumo da sua jornada:

Exercício 1 — resolveu de primeira, ótimo início
Exercício 2 — dificuldade com elif e faixas com and, mas chegou lá
Exercício 3 — pegou bem o conceito de for com append()
Exercício 4 — o mais difícil, mas aprendeu o in com tuplas
Exercício 5 — boa evolução com listas e sum()'''
#====================================================================================



# =============================================================================
#  EXERCÍCIOS DE PYTHON — PARTE 2 (Exercícios 6 a 10)
#  Feitos e corrigidos com auxílio do Claude
# =============================================================================


# -----------------------------------------------------------------------------
# EXERCÍCIO 6 — Contador de vogais
# -----------------------------------------------------------------------------
# ENUNCIADO:
#   Peça ao usuário uma palavra. Conte quantas vogais ela tem e exiba
#   o resultado. Considere vogais: a, e, i, o, u (sem acento).
#
# CONCEITOS USADOS: input(), for, if, in, contador, += 
# -----------------------------------------------------------------------------

contador = 0
palavra = input("Digite uma palavra: ").lower()  # .lower() cobre maiúsculas

for i in palavra:           # percorre letra por letra
    if i in "aeiou":        # verifica se a letra é vogal
        contador += 1       # incrementa o contador

print(f"A palavra que você escreveu tem {contador} vogais")


# -----------------------------------------------------------------------------
# EXERCÍCIO 7 — Tabuada
# -----------------------------------------------------------------------------
# ENUNCIADO:
#   Peça ao usuário um número e exiba a tabuada completa dele (de 1 a 10),
#   no formato: 3 x 1 = 3, 3 x 2 = 6, etc.
#
# CONCEITOS USADOS: input(), int(), for, range(), f-string
# -----------------------------------------------------------------------------

numero = int(input("Digite um número para a tabuada: "))

for i in range(1, 11):          # range(1, 11) vai de 1 até 10
    tabuada = numero * i        # calcula o resultado
    print(f"{numero} x {i} = {tabuada}")  # exibe cada linha da tabuada


# -----------------------------------------------------------------------------
# EXERCÍCIO 8 — Maior e menor da lista
# -----------------------------------------------------------------------------
# ENUNCIADO:
#   Peça ao usuário 5 números e armazene em uma lista. Exiba o maior número,
#   o menor número e a média dos valores.
#
# CONCEITOS USADOS: lista, float(), for, range(), append(), max(), min(), sum(), len()
# -----------------------------------------------------------------------------

lista = []  # lista vazia para guardar os números

for i in range(5):
    n = float(input(f"Digite o número {i + 1}: "))  # pede um número novo a cada repetição
    lista.append(n)                                  # adiciona na lista

print("Maior:", max(lista))               # maior valor da lista
print("Menor:", min(lista))               # menor valor da lista
print("Média:", sum(lista) / len(lista))  # soma dividida pela quantidade


# -----------------------------------------------------------------------------
# EXERCÍCIO 9 — Verificar palíndromo
# -----------------------------------------------------------------------------
# ENUNCIADO:
#   Peça uma palavra ao usuário e verifique se ela é um palíndromo
#   (lê-se igual de trás para frente). Ex: arara, ana.
#   Ignore maiúsculas e minúsculas.
#
# CONCEITOS USADOS: input(), lower(), slicing [::-1], if/else
# -----------------------------------------------------------------------------

p = input("Digite uma palavra: ").lower()  # .lower() para ignorar maiúsculas
invertida = p[::-1]                         # [::-1] lê a string de trás para frente

if p == invertida:
    print(f"{p} é um palíndromo!")
else:
    print(f"{p} não é um palíndromo.")


# -----------------------------------------------------------------------------
# EXERCÍCIO 10 — Calculadora simples
# -----------------------------------------------------------------------------
# ENUNCIADO:
#   Peça dois números e uma operação ao usuário (+, -, *, /).
#   Exiba o resultado. Se a operação for inválida, avise o usuário.
#   Se for divisão por zero, trate esse caso separadamente.
#
# CONCEITOS USADOS: input(), float(), if/elif/else, operadores, if aninhado
# -----------------------------------------------------------------------------

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
op = input("Digite a operação (+, -, *, /): ")

if op == "+":
    print(f"{n1} + {n2} = {n1 + n2}")
elif op == "-":
    print(f"{n1} - {n2} = {n1 - n2}")
elif op == "*":
    print(f"{n1} * {n2} = {n1 * n2}")
elif op == "/":
    if n2 == 0:                          # trata divisão por zero antes de calcular
        print("Erro: divisão por zero!")
    else:
        print(f"{n1} / {n2} = {n1 / n2}")
else:
    print("Operação inválida! Use +, -, * ou /")


#=====================================================================================
'''
1 — Parênteses abertos sem fechar
Apareceu nos exercícios 2, 7 e 8. Sempre conte os ( e ) — o número tem que ser igual na mesma linha.
2 — Indentação
Foi a dificuldade mais frequente, especialmente no exercício 7. Lembre: tudo dentro de um for ou if precisa ter espaço no início, e todos os comandos do mesmo bloco precisam ter a mesma quantidade de espaço.
3 — else com condição
No exercício 2 você tentou else < 5: várias vezes. else nunca recebe condição — ele pega tudo que sobrou automaticamente.
4 — Variável do for inconsistente
No exercício 6 você usou for i mas dentro do if usou letra. O nome precisa ser o mesmo nos dois lugares.
5 — input() fora do loop
Nos exercícios 3 e 8 você colocou o input() antes do for, o que pede o valor só uma vez. Quando quiser pedir um valor a cada repetição, o input() precisa estar dentro do loop.
6 — Comparar tupla com string
No exercício 4 você tentou diaS == "segunda" várias vezes. Para verificar se um valor está dentro de uma tupla ou lista, usa-se in, não ==.
'''
#========================================================================================


#---------------------------------------------------------------------------------
# EXERCICIO 1 - ADIVINHE O NUMERO
#----------------------------------------------------------------------------------
#Defina um número secreto fixo no código (ex: 7). Peça ao usuário para adivinhar.
#Se errar, diga se o chute foi maior ou menor que o secreto e peça de novo.
#Quando acertar, exiba quantas tentativas foram necessárias.
#------------------------------------------------------------------------------------

secreto = 12
contador = 0

while True :
 tentativa = int(input('tente adivinhar o numero que estou pensando : '))
 contador += 1
 if tentativa == secreto :
  print(f'parabens voce acertou em {contador} vezes')
  break;
 elif tentativa < secreto :
  print('numero maior')
 elif tentativa > secreto :
  print('numero menor') 
 else :
  print('numero invalido')




# ----------------------------------------------------------------------------
# EXERCÍCIO 12 — Soma dos números de uma lista
# -----------------------------------------------------------------------------
# ENUNCIADO:
#   Dada a lista [10, 3, 7, 25, 4, 18, 2, 9], exiba a soma apenas dos
#   números maiores que 5.
#   Não use sum() — faça o acumulador manualmente com uma variável.
#
# CONCEITOS: lista, for, if, operadores, acumulador (+=)
# -----------------------------------------------------------------------------
 
# Seu código aqui:
lista = [10,3,7,25,4,18,2,9]
total = 0

for soma in lista :
    if soma > 5 :
     total += soma
print(total)
 
 
 
# -----------------------------------------------------------------------------
# EXERCÍCIO 13 — Conversor de temperatura
# -----------------------------------------------------------------------------
# ENUNCIADO:
#   Peça ao usuário uma temperatura e a unidade (C para Celsius ou F para
#   Fahrenheit). Converta e exiba o resultado na outra unidade.
#   Fórmulas:
#     Celsius para Fahrenheit → F = C * 9/5 + 32
#     Fahrenheit para Celsius → C = (F - 32) * 5/9
#
# CONCEITOS: input(), float(), if/elif/else, f-string, upper()
# -----------------------------------------------------------------------------
 
# Seu código aqui:

temp = float(input("digite uma temperatura :"))
unidade = input("digite uma unidade :").upper()


if unidade == "C":
    F = temp * 9/5 +32
    print(F)
elif unidade =="F" :
    C = (temp - 32) * 5/9
    print(C)
else:
    print('unidade de medida invalida')
    

 
 
 
 
# -----------------------------------------------------------------------------
# EXERCÍCIO 14 — Remover duplicatas de uma lista
# -----------------------------------------------------------------------------
# ENUNCIADO:
#   Dada a lista [1, 3, 2, 3, 5, 1, 4, 2, 5], crie uma nova lista sem
#   valores repetidos, mantendo a ordem de aparição.
#   Não use set() — faça manualmente.
#
# CONCEITOS: lista, for, if, in, append()
# -----------------------------------------------------------------------------
 
# Seu código aqui:
lista1=[1, 3, 2, 3, 5, 1, 4, 2, 5]
lista2 =[]

for n in lista1 :
    if n not in lista2:
        lista2.append(n)
 
 
# -----------------------------------------------------------------------------
# EXERCÍCIO 15 — Contagem regressiva
# -----------------------------------------------------------------------------
# ENUNCIADO:
#   Peça ao usuário um número inteiro positivo.
#   Faça uma contagem regressiva do número até 0, exibindo cada valor.
#   Ao chegar em 0, exiba "Fogo!".
#   Se o usuário digitar um número negativo, exiba uma mensagem de erro.
#
# CONCEITOS: input(), int(), while, if/else, operadores
# -----------------------------------------------------------------------------
 
# Seu código aqui:
num = int(input('digite um numero inteiro'))

if num >0 :
    while num >= 0 :
        print(num)
        num -= 1
    print("FOGOOOO")    
else :
    print('numero invalido')

'''
#=============================================
Você concluiu os exercícios 11 a 15! Resumo rápido:

Exercício 11 — while com contador, o mais difícil do bloco
Exercício 12 — acumulador com +=, resolveu rápido
Exercício 13 — conversor com fórmulas, pegou bem a lógica
Exercício 14 — not in com listas, excelente
Exercício 15 — contagem regressiva com while e -=
'''
#==============================================


#=================================================
#POO
#=================================================
# =============================================================================
#  EXERCÍCIOS DE POO — Programação Orientada a Objetos
#  Resolva cada exercício no espaço indicado
# =============================================================================


# -----------------------------------------------------------------------------
# EXERCÍCIO 1 — Criar uma classe Pessoa
# -----------------------------------------------------------------------------
# ENUNCIADO:
#   Crie uma classe chamada Pessoa com os atributos nome e idade.
#   Crie dois objetos dessa classe e exiba o nome e a idade de cada um.
#
# CONCEITOS: class, __init__, self, atributos, objetos
#
# EXEMPLO DE USO:
#   p1 = Pessoa("João", 25)
#   print(p1.nome)   # João
#   print(p1.idade)  # 25
# -----------------------------------------------------------------------------
'''
# Seu código aqui:
class Pessoa:
 def __init__ (self, nome, idade):
   self.nome = nome 
   self.idade = idade

p1 = Pessoa('carlos',18)
print(p1.nome)
print(p1.idade)

p2 = Pessoa("pedro",10)
print(f'Ola {p2.nome} sua idade e {p2.idade}')



# -----------------------------------------------------------------------------
# EXERCÍCIO 2 — Adicionar um método
# -----------------------------------------------------------------------------
# ENUNCIADO:
#   Crie uma classe Carro com os atributos marca, modelo e ano.
#   Adicione um método chamado descricao() que exiba uma frase com as
#   informações do carro. Crie um objeto e chame o método.
#
# CONCEITOS: class, __init__, self, método, atributos
#
# EXEMPLO DE USO:
#   carro1 = Carro("Toyota", "Corolla", 2020)
#   carro1.descricao()  # Toyota Corolla 2020
# -----------------------------------------------------------------------------
'''
# Seu código aqui:
class Carro :
   def __init__(self, marca , modelo, ano):
      self.marca = marca
      self.modelo = modelo
      self.ano = ano

   def descricao(self):
      print(f'a marca do seu carro e : {self.marca}')
      print(f'o modelo do seu carro e : {self.modelo}')
      print(f'o ano do seu carro e : {self.ano}')
      
car1 = Carro("Ford","fusca",1920)
car1.descricao()

      
    



# -----------------------------------------------------------------------------
# EXERCÍCIO 3 — Método que modifica atributo
# -----------------------------------------------------------------------------
# ENUNCIADO:
#   Crie uma classe ContaBancaria com o atributo saldo.
#   Adicione dois métodos:
#     - depositar(valor): soma ao saldo
#     - sacar(valor): subtrai do saldo, mas só se houver saldo suficiente
#   Teste os dois métodos e exiba o saldo após cada operação.
#
# CONCEITOS: class, __init__, self, métodos, if/else, atributos
#
# EXEMPLO DE USO:
#   conta = ContaBancaria(1000)
#   conta.depositar(500)   # saldo: 1500
#   conta.sacar(200)       # saldo: 1300
#   conta.sacar(9999)      # saldo insuficiente!
# -----------------------------------------------------------------------------

# Seu código aqui:
class ContaBancaria :
   def __init__(self, saldo):
      self.saldo = saldo

   def depositar(self,valor):
    self.saldo += valor
    print(f'saldo: {self.saldo}')

   def sacar(self,valor):
    if valor <= self.saldo:
      self.saldo -= valor
      print(f"saldo suficiente, voce tem :{self.saldo}")
    else:
      print('saldo insuficiente')

conta = ContaBancaria(1000)
conta.depositar(500)
conta.sacar(500)
       
         



# -----------------------------------------------------------------------------
# EXERCÍCIO 4 — Lista de objetos
# -----------------------------------------------------------------------------
# ENUNCIADO:
#   Crie uma classe Produto com os atributos nome e preco.
#   Crie uma lista com 3 produtos.
#   Percorra a lista com um for e exiba o nome e preço de cada um.
#   No final, exiba o produto mais caro.
#
# CONCEITOS: class, __init__, self, lista, for, objetos
#
# EXEMPLO DE USO:
#   p1 = Produto("Notebook", 3500)
#   p2 = Produto("Mouse", 150)
#   produtos = [p1, p2]
#   for produto in produtos:
#       print(produto.nome, produto.preco)
# -----------------------------------------------------------------------------

# Seu código aqui:
class Produto:
  def __init__(self, nome , preco):
    self.nome = nome 
    self.preco = preco 

p1= Produto("mouse ped",100)
p2= Produto("notbook",4000)    

produtos = [p1,p2]

for produto in produtos:
  print(produto.nome , produto.preco)



# -----------------------------------------------------------------------------
# EXERCÍCIO 5 — Método __str__
# -----------------------------------------------------------------------------
# ENUNCIADO:
#   Crie uma classe Aluno com os atributos nome e nota.
#   Adicione o método especial __str__ que retorna uma frase descrevendo
#   o aluno. Quando você der print(aluno) diretamente, a frase deve
#   aparecer automaticamente.
#
# CONCEITOS: class, __init__, self, __str__, return
#
# EXEMPLO DE USO:
#   a1 = Aluno("Maria", 9.5)
#   print(a1)  # Aluno Maria tem nota 9.5
# -----------------------------------------------------------------------------

# Seu código aqui:
class Aluno:
  def __init__(self, nome, nota):
    self.nome = nome
    self.nota = nota

  def __str__(self):
    return f"o aluno {self.nome} tirou {self.nota} na prova"

    a1 = Aluno("Isaque",8.0)
    print(a1)


# =============================================================================
#  POO — PROGRAMAÇÃO ORIENTADA A OBJETOS
#  Resumo dos conceitos + atividades práticas
# =============================================================================


# -----------------------------------------------------------------------------
# 1. OBJETO
# -----------------------------------------------------------------------------
# Um objeto é uma instância de uma classe. É a "coisa real" criada a partir
# do molde (classe). Ele tem atributos (dados) e métodos (ações).

class Cachorro:
    def __init__(self, nome):
        self.nome = nome

dog = Cachorro("Rex")  # dog é um OBJETO da classe Cachorro
print(dog.nome)        # Rex


# -----------------------------------------------------------------------------
# 2. MÉTODO CONSTRUTOR — __init__
# -----------------------------------------------------------------------------
# É executado automaticamente quando um objeto é criado.
# Define os atributos iniciais do objeto.

class Pessoa:
    def __init__(self, nome, idade):  # construtor
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Carlos", 18)  # __init__ roda aqui automaticamente
print(p1.nome)             # Carlos


# -----------------------------------------------------------------------------
# 3. MÉTODOS ESPECIAIS
# -----------------------------------------------------------------------------
# São métodos com __ no início e no fim. O Python os chama automaticamente
# em situações específicas.
#
#   __init__  → chamado ao criar o objeto
#   __str__   → chamado ao usar print() no objeto
#   __len__   → chamado ao usar len() no objeto

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"Produto: {self.nome} — R${self.preco:.2f}"

p = Produto("Notebook", 3500)
print(p)  # Produto: Notebook — R$3500.00


# -----------------------------------------------------------------------------
# 4. ENCAPSULAMENTO
# -----------------------------------------------------------------------------
# Proteger os dados internos de um objeto, controlando o acesso a eles.
# Atributos privados usam __ (dois underscores) no início.
# Para acessar, crie métodos get e set.

class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # atributo privado — não acessível diretamente

    def get_saldo(self):      # método para LER o saldo
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

conta = ContaBancaria(1000)
# print(conta.__saldo)    # ❌ erro — atributo privado
print(conta.get_saldo())  # ✅ 1000 — acesso pelo método


# -----------------------------------------------------------------------------
# 5. HERANÇA
# -----------------------------------------------------------------------------
# Uma classe pode herdar atributos e métodos de outra classe.
# A classe filha herda tudo da classe mãe e pode adicionar ou modificar.

class Animal:                      # classe mãe
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print("...")

class Gato(Animal):                # classe filha herda de Animal
    def falar(self):               # sobrescreve o método da mãe
        print(f"{self.nome} diz: Miau!")

class Cachorro2(Animal):           # outra classe filha
    def falar(self):
        print(f"{self.nome} diz: Au au!")

g = Gato("Mimi")
d = Cachorro2("Rex")
g.falar()   # Mimi diz: Miau!
d.falar()   # Rex diz: Au au!


# -----------------------------------------------------------------------------
# 6. POLIMORFISMO
# -----------------------------------------------------------------------------
# Objetos de classes diferentes podem ser tratados da mesma forma.
# O mesmo método se comporta diferente dependendo do objeto.
# (Geralmente usado junto com herança)

animais = [Gato("Mimi"), Cachorro2("Rex"), Gato("Bolinha")]

for animal in animais:
    animal.falar()  # cada um fala do seu jeito!


# -----------------------------------------------------------------------------
# 7. ABSTRAÇÃO
# -----------------------------------------------------------------------------
# Esconder a complexidade e mostrar apenas o necessário.
# O usuário da classe não precisa saber como funciona por dentro,
# só precisa saber o que ela faz.

class Microondas:
    def __init__(self):
        self.__temperatura = 0     # detalhe interno escondido

    def __aquecer(self):           # método privado — detalhe interno
        self.__temperatura = 180

    def ligar(self):               # método público — interface simples
        self.__aquecer()           # complexidade escondida aqui dentro
        print("Microondas ligado!")

m = Microondas()
m.ligar()          # simples para quem usa
# m.__aquecer()    # ❌ não acessível — detalhe interno


# =============================================================================
#  ATIVIDADES PRÁTICAS
# =============================================================================


# -----------------------------------------------------------------------------
# ATIVIDADE 1 — Encapsulamento
# -----------------------------------------------------------------------------
# Crie uma classe Funcionario com os atributos privados __nome e __salario.
# Adicione métodos para ler e alterar o salário (get e set).
# No set, só permita salários maiores que zero.
# Crie um objeto e teste os métodos.

# Seu código aqui:
class funcionario :
   def __init__(self,nome,salario):
      self.__nome = nome 
      self.salario = salario

   def get_salario(self):
      return self.__salario
   
   def set_salario (self,valor):
      if valor > 0 :
         self.__salario = valor 
    
      else :
         print("salario invalido ")
      

f1 = funcionario("Carlos", 2000)
print(f1.get_salario())   # 2000 — lê pelo método
f1.set_salario(3000)      # altera pelo método
f1.set_salario(-500)      # bloqueado! salário inválido




# -----------------------------------------------------------------------------
# ATIVIDADE 2 — Herança
# -----------------------------------------------------------------------------
# Crie uma classe Veiculo com os atributos marca e velocidade_maxima
# e um método descricao() que exibe as informações.
# Crie duas classes filhas: Carro e Moto, cada uma com um atributo extra.
# Crie um objeto de cada e chame descricao().

# Seu código aqui:




# -----------------------------------------------------------------------------
# ATIVIDADE 3 — Polimorfismo
# -----------------------------------------------------------------------------
# Crie uma classe Forma com um método area() que retorna 0.
# Crie duas classes filhas: Retangulo (largura e altura) e Circulo (raio).
# Cada uma deve sobrescrever area() com o cálculo correto.
# Fórmulas: retângulo = largura * altura  |  círculo = 3.14 * raio ** 2
# Crie uma lista com objetos de ambas as classes e exiba a área de cada uma.

# Seu código aqui:




# -----------------------------------------------------------------------------
# ATIVIDADE 4 — Métodos especiais
# -----------------------------------------------------------------------------
# Crie uma classe Livro com os atributos titulo, autor e paginas.
# Adicione o método __str__ que retorna uma descrição do livro.
# Adicione o método __len__ que retorna o número de páginas.
# Teste com print(livro) e len(livro).

# Seu código aqui:




# -----------------------------------------------------------------------------
# ATIVIDADE 5 — Tudo junto
# -----------------------------------------------------------------------------
# Crie uma classe Banco com uma lista privada de contas (__contas).
# Adicione um método criar_conta(nome, saldo) que cria uma ContaBancaria
# e adiciona na lista.
# Adicione um método listar_contas() que exibe todas as contas.
# Crie 3 contas e liste todas.

# Seu código aqui: