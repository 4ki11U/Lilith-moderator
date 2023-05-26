from asyncio import sleep

from config_data.config import channel_to_subscribe
from keyboards.inline_keyboards import sign_up_keybd
from aiogram import types
from loader import dp, bot
from utils.other_func import select_users_from_db, antibot_check


@dp.message_handler()
async def subsrubed_message(message: types.Message):
    if not antibot_check(await bot.get_chat_member(chat_id=5982591281, user_id=message.from_user.id)) :
        await message.reply(f"Прохання реєстрації :", reply_markup=sign_up_keybd)
        await message.delete()

@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def welcome_intro_message(message: types.Message):
    new_member_data = {}

    for new_user in message.new_chat_members:
        new_member_data['telegram_id'] = new_user.id
        new_member_data['first_name'] = new_user.first_name
        new_member_data['last_name'] = new_user.last_name
        new_member_data['full_name'] = new_user.full_name

    await message.reply(f"Вітаю тебе, <b>{new_member_data['full_name']}</b>, "
                        f"у нашому затишному пеклі.\n\n😈🔥  <i>У пеклі раді всім</i> 🔥 😈",
                        reply_markup=sign_up_keybd)

    # if not select_users_from_db(new_member_data['telegram_id']):
    #     print('Такого юзверя нету')
    #     await message.reply(f"Вітаю тебе, <b>{new_member_data['full_name']}</b>, "
    #                         f"у нашому затишному пеклі.\n\n"
    #                         f"😈🔥  <i>У пеклі раді всім</i> 🔥 😈",
    #                         reply_markup=sign_up_keybd)
    # else:
    #     await message.answer(f"Регистрируйся чтобы чет писать",
    #                          reply_markup=sign_up_keybd)
    #     await message.delete()


@dp.message_handler(content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def left_chat_member(message: types.Message):
    await message.answer(f'{message.left_chat_member.get_mention(as_html=True)} вышел из чата')
    # if message.left_chat_member == message.from_user.id :
    #     await message.answer(f'{message.left_chat_member.get_mention(as_html=True)} вышел из чата')
    # else :
    #     mess_to_del = await message.reply(f'{message.left_chat_member.get_mention(as_html=True)} был исключен из чата пользователем {message.from_user.get_mention(as_html=True)}')
    #     # todo : Поменять время на большее
    #     #await sleep(15) # time in secs
    #     await mess_to_del.delete()
    #     await message.delete()
