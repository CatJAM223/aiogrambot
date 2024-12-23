from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
router = Router()

class Group(StatesGroup):
    group = State()
    role = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Приветсвую дорогие студенты. Данный бот будет оповещать вас'),
    await message.answer('Выберите свою роль:', reply_markup=kb.rules)
    await Group.role.set()

@router.message(F.text == 'Студент')
async def group(message: Message, state: FSMContext):
    await message.answer('Выберите свою группу:', reply_markup=await kb.inline_students())
    await state.set_(Group.group)

@router.message(Group.group)
async def information(message: Message, state: FSMContext):
    info = await state.get_data()
    await message.answer(f'Теперь вы студент группы: {info["group"]}')
    await state.clear()