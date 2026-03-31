from peewee import *
from app.database.peeweemodel import User

async def init_admin(tg_id: int, username: str):
    admin = User.get_or_none(User.tg_id == id)
    if not admin:
        