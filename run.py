import asyncio
from config import TOKEN
from aiogram import Bot, Dispatcher
from app.handler.handler_students import user
from app.handler.handler_admin import admin
from app.database.DataModule import async_main
from app.database.requests import create_admin


bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(admin)
    dp.include_router(user)
    await async_main() # создание таблиц базы данных
    await create_admin(5619590041) # запись тг айди в таблицу базы данных Admin 
    await dp.start_polling(bot)

    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')