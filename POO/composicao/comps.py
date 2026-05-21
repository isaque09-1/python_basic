class Motor :
    def __init__(self, potencia: float , litragem: float, cilindros: int):
        self.potencia = potencia
        self.litragem = litragem
        self.cilindros = cilindros

    def __repr__(self):
        return f"{self.potencia} | {self.litragem} | {self.cilindros}"

    
class Carro :
    def __init__(self, motor: Motor , marca: str , nome :str):
        self.motor = motor
        self.marca = marca
        self.nome = nome

    def __repr__(self):
        return f"{self.motor} | {self.marca} | {self.nome}"

m1 = Motor(245.00 , 2.67 , 4)

c1 = Carro(m1 , "toyota " , "corola")

print(c1)