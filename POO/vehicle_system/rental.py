from customer import Customer
from vehicle import Vehicle


class Rental:
    def __init__(self, customer: Customer, vehicle: Vehicle, days: int):
        self.customer = customer
        self.vehicle = vehicle
        self.days = days

    def calculate_total(self) -> float:
        return self.days * self.vehicle.daily_rate

    def __repr__(self):
        return (
            f"\nCustomer : {self.customer.name} | CPF: {self.customer.cpf}"
            f"\nVehicle  : {self.vehicle.brand} {self.vehicle.model} (Plate: {self.vehicle.plate})"
            f"\nDays     : {self.days} | Total: ${self.calculate_total():.2f}"
        )
