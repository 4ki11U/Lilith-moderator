from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from loader import dp
from utils.other_func import randomize, randomize_number_select_from_db, delete_from_db_randomize_number

slava_ykraine_btn = InlineKeyboardButton('🇺🇦 Слава Україні ! 🇺🇦', url='https://t.me/Daughter_of_Mephisto_bot')
sign_up_keybd = InlineKeyboardMarkup(row_width=1).add(slava_ykraine_btn)

sign_in_btn = InlineKeyboardButton('Реєстрація!', callback_data='sign_in')
sign_in_keybd = InlineKeyboardMarkup(row_width=1).add(sign_in_btn)


@dp.callback_query_handler(text="sign_in_btn")
async def send_random_value(call: types.CallbackQuery):
    await call.answer(text="Welcome to the club, buddy ;)", show_alert=True)


def create_registration_keyboard():
    button_list = [types.InlineKeyboardButton(text=f'{number}', callback_data=f'{number}') for number in range(0, 9)]

    registration_keyboard = types.InlineKeyboardMarkup(row_width=3)
    registration_keyboard.add(*button_list)

    return registration_keyboard


ten_numbers = [f'{number}' for number in range(0, 9)]


@dp.callback_query_handler(text=ten_numbers)
async def accept_registration(call: types.CallbackQuery):
    number_from_start = randomize_number_select_from_db(call.from_user.id)

    if int(call.data) == int(number_from_start[0][1]):
        delete_from_db_randomize_number(call.from_user.id)
        await call.answer(text="Ты успешно зарегистрировался!\n\nWelcome to the club, buddy ;)", show_alert=True)
        await call.message.delete()
    else:
        delete_from_db_randomize_number(call.from_user.id)
        await call.answer(text="Регистрация НЕ пройдена\n\nНажмите /register для повторной регистрации",
                          show_alert=True)
        await call.message.delete()
