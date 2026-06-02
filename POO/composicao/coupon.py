from datetime import datetime
from POO.composicao.user import Users
from typing import Optional


class Coupon:
    def __init__(self,title: str,value: float,expiration_date: datetime,description: str,discount: float,
    ):
        self.title = title
        self.value = value
        self.expiration_date = expiration_date
        self.description = description
        self.discount = discount

    @classmethod
    def create_coupon(cls, data: dict) -> "Coupon":
        return cls(
            title=data["title"],
            value=data["value"],
            expiration_date=data["expiration_date"],
            description=data["description"],
            discount=data["discount"],
        )

    def calculate_final_price(self, price: float):
        return price * (1 - (self.discount / 100))

    

 


