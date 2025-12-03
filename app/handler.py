from aiogram import Router, F, types
from aiogram.filters import CommandStart
from aiogram.filters.command import Command
from aiogram.types import Message
from app.keyboards import students


import app.keyboards as kb
import app.database.requests as rq
router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Приветсвую дорогие студенты. Данный бот будет оповещать вас'),
    await message.answer('Выберите свою роль:', reply_markup=kb.rules)

@router.message(F.text, Command('info'))
async def cmd_start(message: Message):
    await message.answer(f'Телеграмм ид: {message.from_user.id}')
    await message.answer(f'сообщение: {message.text}')

@router.message(F.text == 'Студент')
async def group(message: Message):
    await message.answer('Выберите свою группу:', reply_markup=await kb.inline_students())

@router.message(F.text == 'Администрация')
async def check(message: Message):
    if await rq.checkForAdmin(message.from_user.id) == True:
        await message.answer('Теперь вы администратор')
    else:
        await message.answer('Вы не являетесь администратором')

@router.message(F.text)
async def stranger_go_away(message: Message):
    if message.text in students:
        await message.answer(f'Телеграмм ид: {message.from_user.id}')
        await message.answer(message.text, message.from_user.id)    
        await rq.set_user(message.from_user.id, message.text)
