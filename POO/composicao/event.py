from typing import List, Dict, Any

from user import Users


class Event:
    def __init__(self, title: str, description: str, users: List[Users], regra: Dict[str, Any]):
        self.title = title
        self.description = description
        self.users = users
        self.regra = regra

    def __repr__(self):
        return (
            f"title :{self.title} | description :{self.description} | user :{self.users}"
        )

    @classmethod
    def create_event(cls, data: dict):
        return cls(
            title=data["title"],
            description=data["description"],
            users=[],
            regra=data["regra"],
        )
    
    def add_user(self, user: Users):
        self.users.append(user)

    def add_users(self, users: List[Users]):
        for user in users :
            self.users.append(users)

        