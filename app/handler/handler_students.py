from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.filters.command import Command
from aiogram.types import Message
from app.keyboards import students
import app.keyboards as kb
import app.database.requests as rq
from asyncio import sleep

user = Router()

@user.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Приветсвую дорогие студенты. Данный бот будет оповещать вас'),
    await sleep(1.5)
    await message.answer('Выберите свою роль:', reply_markup=kb.rules)

