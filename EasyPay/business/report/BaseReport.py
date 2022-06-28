from abc import ABC, abstractmethod
from business.model.Stats import Stats
from business.control.StatsControl import StatsControl
import pandas as pd


class BaseReport(ABC):

    format: str

    def export(self, name) -> None:
        self.open(name)
        self.hook1()
        self.header()
        self.body(self.collect())
        self.footer()
        self.hook2()
        self.close()

    def open(self, name) -> None:
        self.arq = open(name+self.format, 'w')

    def hook1(self) -> None:
        pass

    @abstractmethod
    def header(self) -> None:
        pass

    def collect(self) -> dict:
        StatsControl().snapshot()
        table = [stats.to_dict() for stats in Stats.select()]
        return pd.DataFrame(table)

    @abstractmethod
    def body(self, data) -> None:
        pass

    @abstractmethod
    def footer(self) -> None:
        pass

    def hook2(self) -> None:
        pass

    def close(self) -> None:
        self.arq.close()