from business.command.Command import Command
from typing import Any

class Prompt(Command):        
    
    def __init__(self, view) -> None:
        self.view = view
        self.execute()

    def execute(self) -> Any:    
        self.view()
