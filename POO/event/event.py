from datetime import datetime
from cupom import Cupom
from user import User
from decimal import Decimal

class Event :
    def __init__(self , title:str , description:str, price:float , date:datetime , location:str , user:str):
        self.title = title
        self.description = description
        self.price = price
        self.date = date 
        self.location = location
        self.user = user

    def __repr__(self):
     return f"{self.title}, \n {self.description},\n{self.price},\n{self.date},\n{self.location},\n{self.user}"
    


    
    def apply_discount(self , cupom:Cupom):
        new_price = self.price * (self.price - cupom.discout)
        self.price = new_price
    

    