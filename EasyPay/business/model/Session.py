from infra.adapter.UserAdapter import UserAdapter

class Session:

    def __init__(self, user: UserAdapter) -> None:
        self.user = user
