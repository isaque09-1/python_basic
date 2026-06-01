from typing import Any, Dict, List
from coupon import Coupon
from palestrantes import Palestrante
from user import Users


class Event:
    def __init__(
        self,
        title: str,
        description: str,
        users: List[Users],
        regra: Dict[str, Any],
        price: float = 0.0,
    ):
        self.title = title
        self.description = description
        self.users = users
        self.regra = regra
        self.price = price
        self.coupons: List[Coupon] = []
        self.palestrantes: List[Palestrante] = []

    def __repr__(self):
        return f"title :{self.title} | description :{self.description} | user :{self.users}"

    @classmethod
    def create_event(cls, data: dict) -> "Event":
        return cls(
            title=data["title"],
            description=data["description"],
            users=[],
            regra=data["regra"],
            price=data.get("price", 0.0),
        )

    
    def add_user(self, user: Users):
        self.users.append(user)

    def add_users(self, users: List[Users]):
        for user in users:
            self.users.append(user)

    
    def add_palestrante(self, palestrante: Palestrante):
        self.palestrantes.append(palestrante)

    def add_palestrantes(self, palestrantes: List[Palestrante]):
        for palestrante in palestrantes:
            self.palestrantes.append(palestrante)

    
    def add_coupon(self, coupon: Coupon):
        self.coupons.append(coupon)

    def add_coupons(self, coupons: list[Coupon]):
        for coupon in coupons:
            self.coupons.append(coupon)


    def add_cuopon(self, cuopon: Coupon):
        self.add_coupon(cuopon)

    def apply_coupon(self, title: str):
        for coupon in self.coupons:
            if coupon.title == title:
                final_price = coupon.calculate_final_price(self.price)
                print(f"\n--- Aplicando cupom '{coupon.title}' ---")
                print(f"Preço original: R${self.price:.2f}")
                print(f"Desconto: {coupon.discount}%")
                print(f"Preço com desconto: R${final_price:.2f}")
                return final_price

        print("Cupom não encontrado!")
        return None

    def discount_apply(self, title):
        return self.apply_coupon(title)

    def dicount_apply(self, title):
        return self.discount_apply(title)

