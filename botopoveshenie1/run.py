import asyncio
from config import TOKEN
from aiogram import Bot, Dispatcher
from app.handler import router

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    asyncio.run(main())