from aiogram import types
from loader import dp


@dp.chat_member_handler
@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def welcome_intro_message(message: types.Message):
    current_permissions_for_my_chat = {
        'can_send_messages': False,
        'can_send_media_messages': False,
        'can_send_polls': False,
        'can_send_other_messages': False,
        'can_add_web_page_previews': False,
        'can_change_info': False,
        'can_invite_users': False,
        'can_pin_messages': False
    }

    for member in message.new_chat_members:
        restrict(chat_id=-1001989018449, user_id=member.id, permissions=current_permissions_for_my_chat)
    try:
        await message.delete()
    except:
        pass


@dp.message_handler(content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def left_chat_member(message: types.Message):
    await message.answer(f'{message.left_chat_member.get_mention(as_html=True)} вышел из чата')
    if message.left_chat_member == message.from_user.id:
        await message.answer(f'{message.left_chat_member.get_mention(as_html=True)} вышел из чата')
    else:
        mess_to_del = await message.reply(
            f'{message.left_chat_member.get_mention(as_html=True)} был исключен из чата пользователем {message.from_user.get_mention(as_html=True)}')
        # todo : Поменять время на большее
        # await sleep(15) # time in secs
        await mess_to_del.delete()
        await message.delete()
