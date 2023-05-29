from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.reply_keyboards import get_yes_no_kb

router = Router()


@router.message(Command("start"))  # [2]
async def cmd_start(message: Message):
    await message.answer(
        "Вы довольны своей работой?",
        reply_markup=get_yes_no_kb()
    )


@router.message(Command("help"))  # [2]
async def cmd_start(message: Message):
    await message.reply('Возникли вопросы ?\nПиши создателю бота ▶ @f0rkillU')
