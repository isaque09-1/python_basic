class User :
    def __init__(self,username,password):
        self.username = username
        self.password = password
    
    def apresentar (self):
        print(f"Ola , meu nome é {self.username}")

u1 = User('bastiao','rosalinda123')
u2 = User('rosalinda','bastiao123')
u1.apresentar()
u2.apresentar()
