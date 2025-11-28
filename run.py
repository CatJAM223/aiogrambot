import asyncio
from config import TOKEN
from aiogram import Bot, Dispatcher
from app.handler import router
from app.database.DataModule import async_main


bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await async_main()
    await dp.start_polling(bot)

    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')