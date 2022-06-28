import os
from functools import cmp_to_key
from business.model.User import User
from sortedcontainers import SortedList
from infra.metaclass.SingletonMeta import SingletonMeta
from infra.adapter.UserAdapter import UserAdapter
from util.DateCompare import DateCompare

class UserControl(metaclass=SingletonMeta):

    def __init__(self) -> None:
        self._users = SortedList()

    @property
    def users(self):
        return self._users

    def insert(self, user: User) -> None:
        self._users.add(UserAdapter(user))

    def bulk_insert(self, users: list[User]):
        for user in users:
            self.insert(user)

    def select(self, id: int) -> User:
        for user in self._users:
            if user.id == id:
                return user 
        raise KeyError

    def update(self, id: int, updates: dict) -> None:
        user = self.select(id)
        if not set(updates).issubset(dir(user)):
            raise AttributeError
        for key, value in updates.items():
            setattr(user, key, value)

    def delete(self, id: int) -> None:
        user = self.select(id)
        self._users.remove(user)

    def list(self) -> None:
        os.system('clear')
        for user in self._users:
            print(f'ID: {user.id}')
            print(f'Nome: {user.name}')
            print(f'Email: {user.email}\n')
        input('[Enter] para continuar')

    def list_by_birth(self) -> None:
        users_by_birth = sorted(self._users, key=cmp_to_key(DateCompare.compare))
        os.system('clear')
        for user in users_by_birth:
            print(f'ID: {user.id}')
            print(f'Nome: {user.name}')
            print(f'Email: {user.email}')
            print(f'Nascimento: {user.birth}\n')
        input('[Enter] para continuar')

    def migrate(self):
        return [user.to_dict() for user in self._users]
            




 
