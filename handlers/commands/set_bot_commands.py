from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустити Ліліт"),
            types.BotCommand("register", "Реєстрація нового користувача"),
            types.BotCommand("help", "Виникли запитання по боту ?"),
            types.BotCommand("donate", "Допомогти автору фінансово"),
        ]
    )
