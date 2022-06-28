from __future__ import annotations
from abc import ABC, abstractmethod
from business.model.Request import (
    Request, CreditCardRequest, DebitCardRequest, PixRequest
)


class RequestCreator(ABC):

    @classmethod
    @abstractmethod
    def factory(self) -> Request:
        return


class CreditCardRequestCreator(RequestCreator):
    
    @classmethod
    def factory(self, request) -> Request:
        return CreditCardRequest(**request)


class DebitCardRequestCreator(RequestCreator):

    @classmethod
    def factory(self, request) -> Request:
        return DebitCardRequest(**request)


class PixRequestCreator(RequestCreator):

    @classmethod    
    def factory(self, name, purchase) -> Request:
        return PixRequest(name, purchase)




