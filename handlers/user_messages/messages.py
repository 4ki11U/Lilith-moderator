from keyboards import reply_keyboards
from aiogram import types

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from loader import dp

### Главное Меню ###
@dp.message_handler(Text(equals=['Тестовая кнопка']))
async def start(message: types.Message, state: FSMContext):
    if message.text == 'Тестовая кнопка':
        await message.answer('Tested', reply_markup=reply_keyboards.start_main_menu_kb)
    else:
        await message.answer('Я пока не знаю как на это реагировать :(', reply_markup=types.ReplyKeyboardRemove())
