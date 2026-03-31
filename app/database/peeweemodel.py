from peewee import *

db = SqliteDatabase('peeweebase.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    tg_id = IntegerField(unique=True)
    username = CharField()
    name = CharField(null = True)
    surname = CharField(null = True)
    is_admin = BooleanField(default=False)
    group = CharField(null = True)

async def createTable():
    db.create_tables([User])