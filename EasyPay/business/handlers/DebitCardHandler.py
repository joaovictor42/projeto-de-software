from infra.handler.Handler import Handler
from business.model.Request import DebitCardRequest
from business.model.Payment import Payment
from business.control.PaymentControl import PaymentControl
from time import sleep
from typing import Any
import random
import os
      
payment_control = PaymentControl()

class DebitCardHandler(Handler):
    
    def handle(self, request: Any) -> str:
        if isinstance(request, DebitCardRequest):            
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
