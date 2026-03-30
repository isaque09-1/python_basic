from db import USERS
class User :
    def __init__(self,id,username,password,email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def __repr__ (self):
        return f'User(id={self.id},username"{self.username}")'
    
    def add (self):
        USERS.append(self)

    def update(self, id , username , password, email):
        update_user = User(id,username,password,email)
        USERS [id-1] = update_user
    
    def delete(self, id):
        del USERS[self.id-1]

    def get_user_by_id (self):
        for user in USERS:
            if user.id == self.id :
                return user
        return None
        



user1 = User(1,'pedro','pedrin123','pedrin@gmail.com')
user1.add()
print(USERS)

user1.update(1,'adalberto','12345','adalberto@gmail.com')
print(USERS)