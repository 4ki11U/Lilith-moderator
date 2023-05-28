from handlers.groups.new_and_left_chat_members import welcome_intro_message, left_chat_member
from handlers.commands.set_bot_commands import set_default_commands
from handlers.commands.start_commands import startius_comandus
from loader import dp, bot, creator_id
from aiogram.utils import executor
from system import logger


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await bot.send_message(creator_id, 'Слуга тьмы вновь на связи !')



if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=False)