from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_session, AsyncSession

students = ['1-1П9', '1-2П9', '2-1П9', '2-2П9', '3-1П9','3-2П9', '4-1П9', '4-2П9',
            '1-1П11', '2-1П11', '3-1П11',
            '1-1М11',
            '1-1А9', '2-1А9', '3-1А9', '4-1А9', 
            '1-1Б9', '2-1Б9', '3-1Б9', 
            '1-1Г9', '2-1Г9', '3-1Г9', '4-1Г9',
            '1-1Р9', '1-2Р9', '2-1Р9', '2-2Р9',
            '1-1C9', '2-1C9', '3-1C9', '4-1C9',
            '1-1C11', '2-1C11', '3-1C11',
            '3-1Т9', '4-1Т9']


engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

class Base(AsyncAttrs, DeclarativeBase):
    pass
    
class User(Base):

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    group: Mapped[int] = mapped_column(ForeignKey('groups.group'))


class Group(Base):

    __tablename__ = 'groups'

    id: Mapped[int] = mapped_column(primary_key=True)
    group: Mapped[str] = mapped_column()

class Admin(Base):

    __tablename__ = 'admins'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)

async def lolka():
    for i in students:
        await AsyncSession.add(Group(group = i))
        await AsyncSession.commit()

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)