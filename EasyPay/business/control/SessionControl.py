from business.model.Session import Session
from infra.metaclass.SingletonMeta import SingletonMeta
from infra.adapter.UserAdapter import UserAdapter
from util.track_stats import tracker
from business.control.StatsControl import StatsControl

stats_control = StatsControl()


class SessionControl(metaclass=SingletonMeta):

    def __init__(self) -> None:
        self.session = None
    
    @property
    def user(self) -> UserAdapter:
        return self.session.user

    @tracker(stats_control.inc_accesses)
    def login(self, user: UserAdapter) -> None:
        self.session = Session(user)

    def logout(self) -> None:
       self.session = None


