from requests import session
from infra.adapter.UserAdapter import UserAdapter
from infra.metaclass.SingletonMeta import SingletonMeta
from infra.persistence.PersistenceControl import PersistenceControl
from business.control.PaymentControl import PaymentControl
from business.control.RequestControl import RequestControl
from business.control.SessionControl import SessionControl
from business.control.UserControl import UserControl
from business.control.StatsControl import StatsControl
from business.handlers.PixHandler import PixHandler
from business.handlers.RequestHandler import RequestHandler
from business.handlers.DebitCardHandler import DebitCardHandler
from business.handlers.CreditCardHandler import CreditCardHandler
from business.model.Payment import Payment
from business.model.User import User
import os


class SystemControl(metaclass=SingletonMeta):

    def __init__(self) -> None:
        pass

    def start(self) -> None:
        self.user_control    = self.init_control(User, UserControl)
        self.payment_control = self.init_control(Payment, PaymentControl)
        self.stats_control   = StatsControl()
        self.request_control = RequestControl()
        self.session = SessionControl()


    def init_control(self, model, control) -> None:
        persistence = PersistenceControl(model)
        persistence.create_table()
        records = persistence.retrieve()
        control = control()
        control.bulk_insert(records)
        return control


    def prompt(self, view):
        view()


    def processing(self):
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


    def login(self, user) -> UserAdapter:
        user = self.user_control.select(user)
        self.session.login(user)
        return user


    def logout(self) -> None:
        self.session.logout()


    def end(self) -> None:
        self.terminate_control(User, UserControl)
        exit()


    def terminate_control(self, model, control) -> None:
        persistence = PersistenceControl(model)
        persistence.drop_table()
        persistence.create_table()
        records = control().migrate()
        persistence.save(records)



    


