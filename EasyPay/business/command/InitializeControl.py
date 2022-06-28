
from business.command.Command import Command
from infra.persistence.PersistenceControl import PersistenceControl
from typing import Any


class InitializeControl(Command):

    def __init__(self, model, control) -> None:
        self.model = model
        self.control = control
        self.execute()
    
    def execute(self) -> Any:
        persistence = PersistenceControl(self.model)
        persistence.create_table()
        records = persistence.retrieve()
        control = self.control()
        control.bulk_insert(records)
