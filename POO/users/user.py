from db import USERS

class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email


    def add(self):
        USERS.append(self)
       

    def __repr__(self):
        return f"user_id:{self.id}, \n username:{self.username}, \n user_email :{self.email}, \n user_password :{self.password},\n is_admin : False"
    
    def update_username(self, username):
        user = User.get_user_by_id(self.id)
        if user:
            user.username = username
            return user
        return 'Usuário não encontrado'
    
    def update_password(self, password):
        user = User.get_user_by_id(self.id)
        if user:
            user.password = password
            return user
        return 'Usuário não encontrado'
    
    def update_email(self, email):
        user = User.get_user_by_id(self.id)
        if user:
            user.email = email
            return user
        return 'Usuário não encontrado'
    


