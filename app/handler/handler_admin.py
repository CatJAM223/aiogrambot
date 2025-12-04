from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.filters.command import Command
from aiogram.types import Message
import app.keyboards as kb
import app.database.requests as rq


admin = Router()

@admin.message(F.text == 'Администрация')
async def check(message: Message):
    if await rq.checkForAdmin(message.from_user.id) == True:
        await message.answer('Вы администратор')
        await message.answer('Выберите группу, которую хотите оповестить:', reply_markup=await kb.inline_all())
    else:
        await message.answer('Вы не являетесь администратором')
