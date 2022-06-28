from business.model.Session import Session
from infra.metaclass.SingletonMeta import SingletonMeta
from infra.adapter.UserAdapter import UserAdapter

class SessionControl(metaclass=SingletonMeta):

    def __init__(self) -> None:
        self.session = None
    
    @property
    def user(self) -> UserAdapter:
        return self.session.user

    def login(self, user: UserAdapter) -> None:
        self.session = Session(user)

    def logout(self) -> None:
       self.session = None


