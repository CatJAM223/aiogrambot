from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from app.keyboards import students
import app.keyboards as kb
import app.database.requests as rq

user = Router()

@user.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Приветсвую дорогие студенты. Данный бот будет оповещать вас'),
    await message.answer('Выберите свою роль:', reply_markup=kb.rules)

@user.message(F.text == 'Студент')
async def group(message: Message):
    await message.answer('Выберите свою группу:', reply_markup=await kb.inline_students())

@user.message(F.text)
async def stranger_go_away(message: Message):
    if message.text in students:
        if await rq.checkForAdmin(message.from_user.id) == False:
            await message.answer(f'Теперь вы студент группы: {message.text}')
            await rq.set_user(message.from_user.id, message.text)
        else:
            await message.answer('Вы являетесь администратором, а не студентом')
