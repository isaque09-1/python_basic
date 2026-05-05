class User:
    def __intit__(self, id , name , password , email):
        self.id = id
        self.name = name
        self.password = password
        self.email = email

    @classmethod
    def get_all_users(cls):
        return 

    @classmethod
    def get_user_by_id (cls):
        return
    
    @classmethod
    def create_user(cls,user):
        return
    

    @classmethod
    def update_user(cls,id, data):
        return
    

    @classmethod
    def delete_user(cls, id ):
        return