from app.database.DataModule import async_session, User, Admin
from sqlalchemy import select


async def set_user(tg_id, group):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id, group = group))
            await session.commit()


#пися
