class Palestrante:
    def __init__(self, name: str, age: int, curriculum: str, specialty: str, cost: float):
        self.name = name
        self.age = age
        self.curriculum = curriculum
        self.specialty = specialty
        self.cost = cost

    @classmethod
    def create_palestrante(
        cls,
        name: str,
        age: int,
        curriculum: str,
        specialty: str,
        cost: float,
    ):
        return cls(
            name=name,
            age=age,
            curriculum=curriculum,
            specialty=specialty,
            cost=cost,
        )



