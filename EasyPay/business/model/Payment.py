from business.model.User import User
from infra.persistence.DatabaseModel import DatabaseModel
from playhouse.shortcuts import model_to_dict
from peewee import *


class Payment(DatabaseModel):
    name = CharField()
    purchase = FloatField()
    target = ForeignKeyField(User, backref='payments')

    def to_dict(self) -> dict:
        return model_to_dict(self)

    def show(self) -> None:
        print(f'ID: {self.id}')
        print(f'Titular da Compra: {self.name}')
        print(f'Valor da Compra: {self.purchase}')
        print(f'Conta Destino: {self.target.pix}\n')