import asyncio
import logging
from datetime import datetime

import keyboards.for_questions
from aiogram import Bot, Dispatcher, types, html, F
from aiogram.filters import Command, CommandObject
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile
from aiogram.utils.markdown import hide_link

from handlers import questions, different_types
from keyboards.for_questions import get_yes_no_kb
from config_reader import config

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
# импорты
from config_reader import config

# Для записей с типом Secret* необходимо
# вызывать метод get_secret_value(),
# чтобы получить настоящее содержимое вместо '*******'
bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!", reply_markup=get_yes_no_kb())


# Запуск процесса поллинга новых апдейтов
@dp.message(F.new_chat_members)
async def somebody_added(message: types.Message):
    for user in message.new_chat_members:
        await message.reply(f"Привет, {user.full_name}", reply_markup=keyboards.for_questions.get_yes_no_kb())


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    try:
        # dp.include_routers(
        #     in_pm.router, events_in_group.router,
        #     bot_in_group.router, admin_changes_in_group.router
        # )
        # admins = await bot.get_chat_administrators(config.main_chat_id)
        # admin_ids = {admin.user.id for admin in admins}

        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=["message", "inline_query", "chat_member"])
        # await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(), admins=admin_ids)
    finally:
        await dp.storage.close()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped!")
