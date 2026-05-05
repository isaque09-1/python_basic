from user_entity import User

class UserService :
    
    def get_by_id(id):
        return User.get_user_by_id()
    

    def get_all ():
        return User.get_all_users()
    
    def create(user):
        return User.create_user()
    

    def update(data):
        return User.update_user()
    
    def delete(id):
        return User.delete_user()
    