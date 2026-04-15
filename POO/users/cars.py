CARS = []


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

    def add(self):
        CARS.append(self)
        return self

    
    def create_car(cls, marca, modelo, ano, cor):
        new_car = cls(
            id=len(CARS) + 1,
            marca=marca,
            modelo=modelo,
            ano=ano,
            cor=cor,
        )
        new_car.add()
        return new_car

    
    def get_by_id(cls, id):
        for car in CARS:
            if car.id == id:
                return car
        return None


    def list_all(cls):
        return CARS


    def delete(cls, id):
        car = cls.get_by_id(id)
        if car:
            CARS.remove(car)
            return f"Carro id {id} removido com sucesso."
        return "Carro não encontrado."

    def update_marca(self, nova_marca):
        self.marca = nova_marca
        return f"Marca atualizada para: {self.marca}"

    def update_modelo(self, novo_modelo):
        self.modelo = novo_modelo
        return f"Modelo atualizado para: {self.modelo}"

    def update_ano(self, novo_ano):
        self.ano = novo_ano
        return f"Ano atualizado para: {self.ano}"

    def update_cor(self, nova_cor):
        self.cor = nova_cor
        return f"Cor atualizada para: {self.cor}"
