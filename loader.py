from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, types
from os import getenv
from sys import exit

# todo : задать в виртуальное окружение токен бота
bot_token = getenv("BOT_TOKEN")

if not bot_token:
    exit("Error : can't find bot-token")

# todo : в продакшн задам айди создателя для отслеживания его поднятия/падения
creator_id = getenv("creator_id")

bot = Bot(token=bot_token, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)