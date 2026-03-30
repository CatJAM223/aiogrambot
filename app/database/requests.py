from peewee import *
from app.database.peeweemodel import Admin

async def initadmin(id: int):
    if not Admin:
        admin_id = Admin.create(tg_id = id)

