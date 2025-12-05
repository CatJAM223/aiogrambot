from app.database.DataModule import async_session, User, Admin
from sqlalchemy import select

async def set_user(id: int, text: str):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == id))

        if not user:
            session.add(User(tg_id=id, group = text))
            await session.commit()
        else:
            return True

async def create_admin(id: int):
    async with async_session() as session:
        admin = await session.scalar(select(Admin).where(Admin.tg_id == id))

        if not admin:
            session.add(Admin(tg_id=id))

async def checkForAdmin(id: int):
    async with async_session() as session:
        check = await session.scalar(select(Admin).where(Admin.tg_id == id))
        return check is not None
    
async def checkForGroup(id: int):
    async with async_session() as session:
        group = await session.scalar(select(User.group).where(User.tg_id == id))
        if group:
            return group
        
async def changeGroup(id: int):
    async with async_session() as session:
        change = await session.scalar(select(User).where(User.tg_id == id))
        if change:
            await session.delete(change)
            await session.commit()
        else:
            return False
        
async def write(id: int, group: str):
    async with async_session() as session:
        group = await session.scalar(select(User.group).where(User.tg_id == id))
        if group:
            return group