from __future__ import annotations
from abc import ABC, abstractmethod

class Memento(ABC):

    @property
    @abstractmethod
    def origin(self) -> str:
        return

    @abstractmethod
    def get_state(self) -> dict:
       return

    @abstractmethod
    def get_name(self) -> str:
        return

    @abstractmethod
    def get_date(self) -> str:
        return

