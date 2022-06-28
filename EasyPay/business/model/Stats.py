from infra.persistence.DatabaseModel import DatabaseModel
from playhouse.shortcuts import model_to_dict
from datetime import datetime
from peewee import *


class Stats(DatabaseModel):
    total_users    = IntegerField()
    total_accesses = IntegerField()
    total_payments = IntegerField()
    total_requests = IntegerField()
    created_date   = DateTimeField(default=datetime.now)

    def to_dict(self) -> dict:
        return model_to_dict(self)

    def show(self) -> None:
        print(f'Usuários Totais: {self.total_users}')
        print(f'Acessos Totais: {self.total_accesses}')
        print(f'Pagamentos Totais: {self.total_payments}')
        print(f'Solicitações Totais: {self.total_requests}\n')
        input()

