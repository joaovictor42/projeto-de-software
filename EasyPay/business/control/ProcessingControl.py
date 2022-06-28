from business.control.RequestControl import RequestControl
from business.handlers.RequestHandler import RequestHandler
from business.handlers.CreditCardHandler import CreditCardHandler
from business.handlers.DebitCardHandler import DebitCardHandler
from business.handlers.PixHandler import PixHandler


def process():
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
    
    


