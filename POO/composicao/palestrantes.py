class Palestrante:
    def __init__(self, name: str, age: int, curriculum: str, specialty: str, cost: float):
        self.name = name
        self.age = age
        self.curriculum = curriculum
        self.specialty = specialty
        self.cost = cost

    def __repr__(self):
        return f'O nome do palestrante é :{self.name}\n idade:{self.age}\n curriculo:{self.curriculum}\n especialidade:{self.specialty}\n custo:{self.cost}'




    @classmethod
    def create_palestrante(cls,data,name: str,age: int,curriculum: str,specialty: str,cost: float,):
        return Palestrante(
            name=data['name'],
            age=data['age'],
            curriculum=data['curriculum'],
            specialty=data['specialty'],
            cost=data['cost'],
        )






