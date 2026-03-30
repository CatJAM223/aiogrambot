import asyncio 
from config import TOKEN
from aiogram import Bot, Dispatcher
from app.handler.handler_students import user
from app.handler.handler_admin import admin
from app.database.peeweemodel import createTable
from app.database.requests import initadmin

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(admin)
    dp.include_router(user)
    await createTable()
    await initadmin(5619590041)
    await dp.start_polling(bot)

    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')