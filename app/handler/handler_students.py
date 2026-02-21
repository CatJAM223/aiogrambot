from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.filters.command import Command
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
            if await rq.set_user(message.from_user.id, message.text) == True:
                await message.answer(f'Вы уже являетесь студентом группы {await rq.checkForGroup(message.from_user.id)}')
            else:
                await rq.set_user(message.from_user.id, message.text)
                await message.answer(f'Теперь вы студент группы: {await rq.checkForGroup(message.from_user.id)}')
                await message.answer(f'Хотите сменить группу? Отправте команду /change')
        else:
            await message.answer('Вы являетесь администратором, а не студентом')

@user.message(Command('change'))
async def change(message: Message):
    if await rq.changeGroup(message.from_user.id) == True:
        await message.answer('Вы и так не состоите в группе')
    else:
        await message.answer('Теперь вы не состоите в группе')
