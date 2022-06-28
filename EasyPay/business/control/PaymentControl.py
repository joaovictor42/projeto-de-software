import os
from business.model.Payment import Payment
from infra.metaclass.SingletonMeta import SingletonMeta

class PaymentControl(metaclass=SingletonMeta):

    def __init__(self) -> None:
        self._payments = {}

    @property
    def payments(self):
        return self._payments.values()

    def insert(self, payment: Payment) -> None:
        self._payments[payment.id] = payment

    def bulk_insert(self, payments: list[Payment]):
        for payment in payments:
            self.insert(payment)
    
    def select(self, id: str) -> Payment:
        return self._payments[id]

    def update(self, id: str, updates: dict) -> None:
        payment = self._payments[id]
        if not set(updates).issubsetset(dir(payment)):
            raise AttributeError
        for key, value in updates.items():
            setattr(payment, key, value)

    def delete(self, id: str) -> None:
        del self._payments[id]

    def list(self) -> None:
        os.system('clear')
        if self._payments:
            print('Informações do Pagamento')
            for payment in self._payments.values():
                payment.show()
        else:
            print('Sem pagamentos cadastradas\n')
        input('[Enter] para continuar')

    def migrate(self):
        return [payment.to_dict() for payment in self.payments]