from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters.text import Text
from aiogram import Router

router = Router()


@router.message(Text(text=["да", "нет"], ignore_case=True))
async def answer_yes(message: Message):
    if message.text.lower() == "да":
        await message.answer("Это здорово!", reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer("Жаль...", reply_markup=ReplyKeyboardRemove())
