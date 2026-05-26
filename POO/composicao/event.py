from user import Users
from typing import List

class Event :
    def __init__(self,title: str, description:str, users:List[str]):
        self.title = title
        self.description = description
        self.user = users


    def __repr__(self):
        return f"title :{self.title} | description :{self.description} | user :{self.user}"
    



u1 = Users("pedrinho", "pedrinmiugrau123","pedro@gmail")
u2 = Users("kelvao","matador123", "kelvao@...")
u3 = Users("migro", "cataro", "MIGRAO@...")


e1 = Event("rinha de galo", "apostas",u1.username)

print(e1)


