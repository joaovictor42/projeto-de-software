from infra.memento.Memento import Memento
from datetime import datetime

class UserMemento(Memento):
    def __init__(self, state: dict)-> None:
        self._state = state
        self._date = datetime.now()

    @property
    def origin(self) -> str:
        return self._state['id']

    def get_state(self) -> dict:
       return self._state

    def get_name(self) -> str:
        return f"{self._date}-{self._state['name']}"

    def get_date(self) -> datetime:
        return self._date
