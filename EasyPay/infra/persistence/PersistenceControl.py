from infra.persistence.DatabaseModel import database
from typing import Any


class PersistenceControl:

    def __init__(self, cls) -> None:
        self.cls = cls

    def retrieve(self) -> list[Any]:
        return list(self.cls.select())

    def save(self, objs: list[dict]) -> int:
        return self.cls.insert_many(objs).execute()

    def create_table(self) -> None:
        database.create_tables([self.cls])

    def drop_table(self) -> None:
        database.drop_tables([self.cls])
