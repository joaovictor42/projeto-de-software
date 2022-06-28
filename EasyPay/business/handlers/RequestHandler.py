from business.handlers.Handler import Handler
from typing import Any

class RequestHandler(Handler):
    
    def handle(self, request: Any) -> str:
        return super().handle(request)

