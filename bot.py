from handlers.bot_commands.set_bot_commands import my_bot_commands
from handlers.bot_commands import start_commands
from handlers.text_messages import user_answer_messages

from aiogram import Bot, Dispatcher
from config_reader import bot_config
import asyncio
import logging


async def main():
    bot = Bot(token=bot_config.bot_token.get_secret_value(), parse_mode="HTML")
    dp = Dispatcher()

    logging.basicConfig(level=logging.INFO)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    try:
        dp.include_routers(
            user_answer_messages.router,
            start_commands.router
        )

        await my_bot_commands(bot)  # задаем боту команды через /

        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await dp.storage.close()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped!")
