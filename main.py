from handlers.commands.set_bot_commands import set_default_commands
from loader import dp, bot, creator_id
from aiogram.utils import executor


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await bot.send_message(creator_id, 'Слуга тьмы вновь на связи !')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)