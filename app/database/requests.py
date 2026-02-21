from app.database.DataModule import async_session, User, Admin
from sqlalchemy import select


async def set_user(tg_id, group):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id, group = group))
            await session.commit()

async def create_admin(tg_id):
    async with async_session() as session:
        admin = await session.scalar(select(Admin).where(Admin.tg_id == tg_id))

        if not admin:
            session.add(Admin(tg_id=tg_id))
            await session.commit()

async def checkForAdmin(id: int):
    async with async_session() as session:
        check = await session.scalar(select(Admin).where(Admin.tg_id == id))
        return check is not None

