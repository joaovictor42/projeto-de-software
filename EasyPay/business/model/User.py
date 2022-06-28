from infra.persistence.DatabaseModel import DatabaseModel
from peewee import *


class User(DatabaseModel):
    admin = BooleanField(default=False)
    name = CharField()
    email = CharField(unique=True)
    password = CharField()
    birth = DateField(formats=['%d/%m/%Y', '%Y-%m-%d'])
    pix = CharField()
