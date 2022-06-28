from __future__ import annotations
from abc import ABC, abstractmethod
from business.control.SessionControl import SessionControl
from uuid import uuid4
from itertools import count

session = SessionControl()


class Request(ABC):

    id = count()

    @abstractmethod
    def info(self) -> dict:
        return
    
    @abstractmethod
    def show(self) -> None:
        return


class CreditCardRequest(Request):

    def __init__(self, name, card_number, security_code, purchase, expiry, flag) -> None:
        self.id = next(self.id)
        self.purchase = purchase
        self.name = name
        self.card_number = card_number
        self.security_code = security_code
        self.expiry = expiry
        self.flag = flag
        self.target = session.user.expose()

    def info(self) -> dict:
        return {
            'name': self.name, 
            'purchase': self.purchase,
            'target': self.target
        }

    def show(self) -> None:
        print(f'ID: {self.id}')
        print(f'Valor da Compra: {self.purchase}')
        print(f'Nome do Titular: {self.name}')
        print(f'Número do Cartão: {self.card_number}')
        print(f'Código do Cartão: {self.security_code}')
        print(f'Validade do Cartão: {self.expiry}')
        print(f'Bandeira do Cartão: {self.flag}')
        print(f'Conta Destino: {self.target.pix}\n')


class DebitCardRequest(Request):

    def __init__(self, name, card_number, security_code, purchase, expiry, flag) -> None:
        self.id = next(self.id)
        self.purchase = purchase
        self.name = name
        self.card_number = card_number
        self.security_code = security_code
        self.expiry = expiry
        self.flag = flag
        self.target = session.user.expose()

    def info(self) -> dict:
        return {
            'name': self.name, 
            'purchase': self.purchase,
            'target': self.target
        }

    def show(self) -> None:
        print(f'ID: {self.id}')
        print(f'Valor da Compra: {self.purchase}')
        print(f'Nome do Titular: {self.name}')
        print(f'Número do Cartão: {self.card_number}')
        print(f'Código do Cartão: {self.security_code}')
        print(f'Validade do Cartão: {self.expiry}')
        print(f'Bandeira do Cartão: {self.flag}')
        print(f'Conta Destino: {self.target.pix}\n')


class PixRequest(Request):

    def __init__(self, name, purchase) -> None:
        self.id = next(self.id)
        self.name = name
        self.purchase = purchase
        self.code = uuid4().hex
        self.target = session.user.expose()

    def info(self) -> dict:
        return {
            'name': self.name, 
            'purchase': self.purchase,
            'target': self.target
        }

    def show(self) -> None:
        print(f'ID: {self.id}')
        print(f'Nome: {self.name}')
        print(f'Valor da Compra: {self.purchase}')
        print(f'Código Pix: {self.code}')
        print(f'Conta Destino: {self.target.pix}\n')
    