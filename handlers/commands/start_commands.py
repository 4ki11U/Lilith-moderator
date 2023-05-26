from keyboards.inline_keyboards import create_registration_keyboard
from utils.other_func import randomize_number_insert_into_db
from database_files.Telegram_DataUsers import TelegramDB
from loader import bot, dp
from aiogram import types
import random

tg_database = TelegramDB(database_file=r'database_files/tg_datausers.db')


@dp.message_handler(commands=['start', 'help', 'register', 'donate'])
async def startius_comandus(message: types.message):
    user_data = message.from_user

    if message.text == '/start':
        await bot.send_message(message.from_user.id,
                               f"Вітаю тебе, <b>{message.from_user.first_name}</b>, "
                               f"в твоєму особливому Пеклі наодинці зі мною.\n\n"
                               f"<i>Хто входить тут, покинь усю надію (с) Данте Аліг'єрі</i>")
    elif message.text == '/register':
        randomize_number = random.randint(0, 9)
        randomize_number_insert_into_db(randomize_number, user_data)

        await bot.send_message(message.from_user.id,
                               f"Для реєстрації для доступу до чату, <b>{message.from_user.first_name}</b> <b>{message.from_user.last_name}</b>\n\n"
                               f"Натисни на цифру, яку ти наразі бачиш 👉  <b>{randomize_number}</b>",
                               reply_markup=create_registration_keyboard())
    elif message.text == '/help':
        await message.reply('Возникли вопросы ?\nПиши создателю бота ▶ @f0rkillU')
    elif message.text == '/donate':
        await message.reply('Інфа буде трохи пізніше :)')
