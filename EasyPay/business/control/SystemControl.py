from infra.adapter.UserAdapter import UserAdapter
from infra.metaclass.SingletonMeta import SingletonMeta
from business.control.PaymentControl import PaymentControl
from business.control.RequestControl import RequestControl
from business.control.SessionControl import SessionControl
from business.command.InitializeControl import InitializeControl
from business.command.TerminateControl import TerminateControl
from business.control.StatsControl import StatsControl
from business.control.UserControl import UserControl
from business.model.Payment import Payment
from business.model.User import User


class SystemControl(metaclass=SingletonMeta):


    def start(self) -> None:
        InitializeControl(User, UserControl)
        InitializeControl(Payment, PaymentControl)
        self.user_control    = UserControl()
        self.payment_control = PaymentControl()
        self.stats_control   = StatsControl()
        self.request_control = RequestControl()
        self.session         = SessionControl()


    def login(self, user) -> UserAdapter:
        user = self.user_control.select(user)
        self.session.login(user)
        return user


    def logout(self) -> None:
        self.session.logout()


    def end(self) -> None:
        TerminateControl(User, UserControl)
        exit()


    


    


