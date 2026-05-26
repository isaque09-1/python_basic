class Users:
    def __init__(self,username:str,password:str,email:str):
        self.username = username   
        self.password = password
        self.email = email

    def __repr__(self):
        return f"Username : {self.username} | Password :{self.password} | email :{self.email}"