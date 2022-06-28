import os
from business.model.Request import Request
from infra.metaclass.SingletonMeta import SingletonMeta
from util.track_stats import tracker
from business.control.StatsControl import StatsControl

stats_control = StatsControl()

class RequestControl(metaclass=SingletonMeta):

    def __init__(self) -> None:
        self._requests = {}

    @property
    def requests(self):
        return self._requests.values()

    @tracker(stats_control.inc_requests)
    def insert(self, request: Request) -> None:
        self._requests[request.id] = request
    
    def select(self, id: str) -> Request:
        return self._requests[id]

    def update(self, id: str, updates: dict) -> None:
        request = self._requests[id]
        if not set(updates).issubsetset(dir(request)):
            raise AttributeError
        for key, value in updates.items():
            setattr(request, key, value)

    def delete(self, id: str) -> None:
        del self._requests[id]

    def list(self) -> None:
        os.system('clear')
        if self._requests:
            print('Informações da Solicitação')
            for request in self._requests.values():
                request.show()
        else:
            print('Sem solicitações cadastradas\n')
        input('[Enter] para continuar')
