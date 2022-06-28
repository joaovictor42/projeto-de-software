from business.command.Command import Command
from infra.persistence.PersistenceControl import PersistenceControl
from typing import Any


class TerminateControl(Command):

    def __init__(self, model, control) -> None:
        self.model = model
        self.control = control
        self.execute()
    
    def execute(self) -> Any:
        persistence = PersistenceControl(self.model)
        persistence.drop_table()
        persistence.create_table()
        records = self.control().migrate()
        persistence.save(records)             
