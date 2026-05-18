from datetime import datetime
from decimal import Decimal

class Cupom :
    def __init__(self, title:str ,expires_at:datetime , discout:Decimal ):
        self.title = title
        self.expires_at = expires_at
        self.discout = discout

    def __repr__(self):
        return f"{self.title},\n{self.expires_at},\n{self.discout}"
