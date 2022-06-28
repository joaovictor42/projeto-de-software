from business.handlers.CreditCardHandler import CreditCardHandler
from business.handlers.DebitCardHandler import DebitCardHandler
from business.handlers.RequestHandler import RequestHandler
from business.control.RequestControl import RequestControl
from business.handlers.PixHandler import PixHandler
from business.command.Command import Command
from typing import Any
import os


class Processing(Command):

    def __init__(self) -> None:
        self.execute()

    def execute(self) -> Any:
        os.system('clear')
        handler = RequestHandler()
        (
            handler
            .set_next(CreditCardHandler())
            .set_next(DebitCardHandler())
            .set_next(PixHandler())
        )
        
        request_control = RequestControl()
        for request in request_control.requests:
            handler.handle(request)
        request_control._requests.clear()
        print('Processamento Concluído!')
        input('[Enter] para continuar')       
        