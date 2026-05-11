from db import USERS


class User:
    def __init__(self, id, name, password, email):
        self.id = id
        self.name = name
        self.password = password
        self.email = email


    def add(self):
        USERS.append(self.to_dict())

    @classmethod
    def get_all_users(cls):
        return USERS

    @classmethod
    def get_user_by_id(cls, id):
        for user in USERS:
            if user["id"] == id:
                return user
        return None

    @classmethod
    def create_user(cls, name, password, email):
        new_id = len(USERS) + 1
        user = cls(new_id, name, password, email)
        user.add()
        return user.to_dict()

    @classmethod
    def update_user(cls, id, data):
       
     @classmethod
     def delete_user(cls, id):
        for i, user in enumerate(USERS):
            if user["id"] == id:
                USERS.pop(i)
                print(f"Usuario '{user['name']}' deletado!")
                return True
        print("Usuario não encontrado!")
        return False




