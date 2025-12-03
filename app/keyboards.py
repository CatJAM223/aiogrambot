from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
rules = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Студент'), 
     KeyboardButton(text='Администрация')]
], resize_keyboard=True, input_field_placeholder='Выберите свою роль')

students = ['1-1П9', '1-2П9', '2-1П9', '2-2П9', '3-1П9','3-2П9', '4-1П9', '4-2П9',
            '1-1П11', '2-1П11', '3-1П11',
            '1-1М11',
            '1-1А9', '2-1А9', '3-1А9', '4-1А9', 
            '1-1Б9', '2-1Б9', '3-1Б9', 
            '1-1Г9', '2-1Г9', '3-1Г9', '4-1Г9',
            '1-1Р9', '1-2Р9', '2-1Р9', '2-2Р9',
            '1-1C9', '2-1C9', '3-1C9', '4-1C9',
            '1-1C11', '2-1C11', '3-1C11',
            '3-1Т9', '4-1Т9']
async def inline_students():
    Keyboard = ReplyKeyboardBuilder()
    for student in students:
        Keyboard.add(KeyboardButton(text=student))
    return Keyboard.adjust(4).as_markup()