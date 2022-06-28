from infra.metaclass.SingletonMeta import SingletonMeta
from business.model.Stats import Stats
from business.model.User import User
from business.model.Payment import Payment
from infra.persistence.PersistenceControl import PersistenceControl


class StatsControl(metaclass=SingletonMeta):

    def __init__(self) -> None:
        self.initialize()
        try:
            stats = Stats.select().order_by(Stats.id.desc()).get()
            self._total_accesses = stats.total_accesses
            self._total_requests = stats.total_requests
        except:
            self._total_accesses = 0
            self._total_requests = 0

    def initialize(self) -> None:
        PersistenceControl(Stats).create_table()

    def snapshot(self) -> dict:
        stats = Stats(
            total_users=self.total_users,
            total_accesses=self.total_accesses,
            total_payments=self.total_payments,
            total_requests=self.total_requests
        )
        stats.save()
        return stats.to_dict()

    @property
    def total_users(self) -> int:
        return len(User.select())

    @property
    def total_payments(self) -> int:
        return len(Payment.select())

    @property
    def total_accesses(self) -> int:
        return self._total_accesses

    @property
    def total_requests(self) -> int:
        return self._total_requests

    def inc_accesses(self) -> None:
        self._total_accesses += 1
        
    def inc_requests(self) -> None:
        self._total_requests += 1
    

    
    
