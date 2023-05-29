from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def my_bot_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='start bot'
        ),
        BotCommand(
            command='help',
            description='question for bot'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
