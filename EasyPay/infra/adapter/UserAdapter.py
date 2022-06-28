
from business.model.User import User
from business.model.Date import Date
from datetime import date
from playhouse.shortcuts import model_to_dict
from itertools import count
from infra.memento.Memento import Memento
from business.model.UserMemento import UserMemento

class UserAdapter:

    def __init__(self, user: User) -> None:
        self.user = user

    @property
    def id(self) -> str:
        return self.user.id

    @id.setter
    def id(self, id) -> None:
        pass

    @property
    def name(self) -> str:
        return self.user.name

    @name.setter
    def name(self, name: str) -> None:
        self.user.name = name

    @property
    def admin(self) -> bool:
        return self.user.admin

    @admin.setter
    def admin(self, admin: bool) -> None:
        self.user.admin = admin

    @property
    def email(self) -> str:
        return self.user.email

    @email.setter
    def email(self, email: str) -> None:
        self.user.email = email

    @property
    def password(self) -> str:
        return self.user.password

    @password.setter
    def password(self, password: str) -> None:
        self.user.password = password

    @property
    def birth(self) -> Date:
        birth = self.user.birth
        return Date(birth.day, birth.month, birth.year)  

    @birth.setter
    def birth(self, date: date) -> None:
        self.user.birth = date

    @property
    def pix(self) -> str:
        return self.user.pix

    @pix.setter
    def pix(self, pix: str) -> None:
        self.user.pix = pix

    def to_dict(self) -> dict:
        return model_to_dict(self.user)

    def expose(self) -> User:
        return self.user

    def show(self) -> None:
        print(f'ID: {self.id}')
        print(f"Admin: {'Sim' if self.admin else 'Não'}")
        print(f'Nome: {self.name}')
        print(f'Email: {self.email}')
        print(f'Senha: {self.password}')
        print(f'Nascimento: {self.birth}')
        print(f'Pix: {self.pix}\n')

    def save(self) -> Memento:
        return UserMemento(self.to_dict())

    def restore(self, memento: Memento) -> None:
        for key, value in memento.get_state().items():
            setattr(self, key, value)

    def __lt__(self, other):
        if not isinstance(other, UserAdapter):
            return NotImplemented
        return self.name < other.name

    def __le__(self, other):
        if not isinstance(other, UserAdapter):
            return NotImplemented
        return self.name <= other.name

    def __eq__(self, other) -> bool:
        return isinstance(other, UserAdapter) and self.name == other.name

    def __ne__(self, other) -> bool:
        return not isinstance(other, UserAdapter) or self.name != other.name

    def __ge__(self, other):
        if not isinstance(other, UserAdapter):
            return NotImplemented
        return self.name >= other.name

    def __gt__(self, other):
        if not isinstance(other, UserAdapter):
            return NotImplemented
        return self.name > other.name


