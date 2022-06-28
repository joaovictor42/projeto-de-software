from peewee import *


database = SqliteDatabase('EasyPay.db')


class DatabaseModel(Model):
    class Meta:
        database = database
