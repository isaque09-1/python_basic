from datetime import datetime
from POO.composicao.coupon import Coupon
from POO.composicao.event import Event
from POO.composicao.user import Users




user1 = Users("Ana", "pass1", "ana@mail.com")
user2 = Users("Bruno", "pass2", "bruno@mail.com")


event = Event(
    title="Hackaton",
    description="Vai ter pt",
    users=[user1, user2],
    regra={"regra1": "teste"},  
    price=200.0,
)


coupon = Coupon(
    title="DESCONTO20",
    value=0.0,
    expiration_date=datetime.now(),
    description="Cupom 20%",
    discount=20.0,
)

event.add_coupon(coupon)


final_price = event.apply_coupon("DESCONTO20")
print(f"\nPreço final retornado: R${final_price:.2f}")

