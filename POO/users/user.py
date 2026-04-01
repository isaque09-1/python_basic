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

    @classmethod
    def get_user_by_id (cls, id):
        for user in USERS:
            if user.id ==id:
                return user
        return None
        
    @classmethod    #metodo de classe 
    def get_all_users(cls):
        return USERS
    
user1 = User(1,'pedro','pedrin123','pedrin@gmail.com')
user1.add()

print(User.get_user_by_id(1))   
print(User.get_all_users())



