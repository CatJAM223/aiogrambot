from peewee import *

db = SqliteDatabase('peeweebase.db')

class Admin(Model):
    tg_id = BigIntegerField()

    class Meta:
        database = db

class User(Model):
    tg_id = BigIntegerField()
    group = CharField()

    class Meta:
        database = db

async def createTable():
    db.create_tables([User, Admin])