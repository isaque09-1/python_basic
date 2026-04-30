
class Car:
    def __init__(self, id, marca, modelo, ano, cor):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def __repr__(self):
        return (
            f"car_id: {self.id}, \n"
            f" marca: {self.marca}, \n"
            f" modelo: {self.modelo}, \n"
            f" ano: {self.ano}, \n"
            f" cor: {self.cor}"
        )

   