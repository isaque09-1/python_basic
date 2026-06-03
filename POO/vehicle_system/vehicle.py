class Vehicle:
    def __init__(self, plate: str, brand: str, model: str, daily_rate: float, available: bool = True):
        self.plate = plate
        self.brand = brand
        self.model = model
        self.daily_rate = daily_rate
        self.available = available

    def __repr__(self):
        status = "Available" if self.available else "Rented"
        return (
            f"Plate: {self.plate} | Brand: {self.brand} | Model: {self.model} "
            f"| Daily Rate: ${self.daily_rate:.2f} | Status: {status}"
        )


class Car(Vehicle):
    def __init__(self, plate: str, brand: str, model: str, daily_rate: float, category: str):
        super().__init__(plate, brand, model, daily_rate)
        self.category = category

    def __repr__(self):
        return super().__repr__() + f" | Category: {self.category} | Type: Car"


class Motorcycle(Vehicle):
    def __init__(self, plate: str, brand: str, model: str, daily_rate: float, engine_cc: int):
        super().__init__(plate, brand, model, daily_rate)
        self.engine_cc = engine_cc

    def __repr__(self):
        return super().__repr__() + f" | Engine: {self.engine_cc}cc | Type: Motorcycle"
