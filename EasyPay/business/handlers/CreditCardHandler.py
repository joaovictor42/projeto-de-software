from business.handlers.Handler import Handler
from business.model.Request import CreditCardRequest
from business.model.Payment import Payment
from business.control.PaymentControl import PaymentControl
from typing import Any
from time import sleep
import random
import os

payment_control = PaymentControl()

class CreditCardHandler(Handler):
    
    def handle(self, request: Any) -> str:
        if isinstance(request, CreditCardRequest):
            os.system('clear')
            print(f'Analisando...\n')
            request.show()
            sleep(5)
            approved = random.choice([True, False])
            if approved:
                print('Solicitação Aprovada!')
                new_payment = Payment(**request.info())
                payment_control.insert(new_payment)
                new_payment.save()
            else:
                print('Solicitação Reprovada!')
        else:
            return super().handle(request)
        sleep(3)

