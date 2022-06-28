from business.handlers.Handler import Handler
from business.model.Request import PixRequest
from business.model.Payment import Payment
from business.control.PaymentControl import PaymentControl
from business.control.RequestControl import RequestControl
from time import sleep
from typing import Any
import random
import os

payment_control = PaymentControl()
request_control = RequestControl()

class PixHandler(Handler):
    
    def handle(self, request: Any) -> str:
        if isinstance(request, PixRequest):
            os.system('clear')
            print(f'\nAnalisando...\n')
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

