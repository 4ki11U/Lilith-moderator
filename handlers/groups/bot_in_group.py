from aiogram import F, Router, Bot, types
from aiogram.client import bot
from aiogram.filters.chat_member_updated import \
    ChatMemberUpdatedFilter, IS_NOT_MEMBER, MEMBER, ADMINISTRATOR
from aiogram.types import ChatMemberUpdated, ChatPermissions, chat, chat_permissions
from aiogram.methods.restrict_chat_member import RestrictChatMember

router = Router()
router.my_chat_member.filter(F.chat.type.in_({"group", "supergroup"}))

chats_variants = {
    "group": "-1001989018449",
    "supergroup": "-1001989018449"
}


@router.my_chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=IS_NOT_MEMBER >> ADMINISTRATOR
    )
)
async def bot_added_as_admin(event: ChatMemberUpdated, bot: Bot):
    # Самый простой случай: бот добавлен как админ.
    # Легко можем отправить сообщение
    await bot.send_message(
        chat_id=event.chat.id,
        text=f"Привет! Спасибо, что добавили меня в "
             f'{chats_variants[event.chat.type]} "{event.chat.title}" '
             f"как администратора. ID чата: {event.chat.id}"
    )


# @router.chat_member()
@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=IS_NOT_MEMBER >> MEMBER))
async def bot_added_as_member(event: ChatMemberUpdated, bot: Bot):
    chat_info = await bot.get_chat(event.chat.id)
    print(chat_info)
    OnlyReadPermissions = types.ChatPermissions(
        can_send_messages=False,
        can_send_media_messages=False,
        can_send_polls=False,
        can_send_other_messages=False,
        can_add_web_page_previews=False,
        can_change_info=False,
        can_invite_users=False,
        can_pin_messages=False
    )

    await bot.send_message(chat_id=event.chat.id, text='Hi buddy')
    await bot.restrict_chat_member(chat_id=event.chat.id, user_id=event.from_user.id, permissions=OnlyReadPermissions)

# @router.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
# async def on_new_chat_members(message: types.Message):
#     for member in message.new_chat_members:
#         logging.info(f"Присоединился новый участник {member.first_name} ({member.username}) в чат {message.chat.title} ({message.chat.id})")
#         await bot.restrich_chat_member(message.chat.id, member.full_name)
#     try:
#         await message.delete()
#     except:
#         pass


# @router.message(F.new_chat_members)
# @router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=IS_NOT_MEMBER >> MEMBER))

# async def bot_added_as_member(event: ChatMemberUpdated, bot: Bot):
#
#     chat_info = await bot.get_chat(event.chat.id)
#     print(chat_info)
#
#     await bot.send_message(chat_id=event.chat.id,text='Hello')
#
#     if chat_info.permissions.can_send_messages:
#         my_per_for_chat = {
#             'can_send_messages': False,
#             'can_send_media_messages': False,
#             'can_send_polls': False,
#             'can_send_other_messages': False,
#             'can_add_web_page_previews': False,
#             'can_change_info': False,
#             'can_invite_users': False,
#             'can_pin_messages': False
#         }
#         await bot.RestrictChatMember(chat_id=-1001989018449, user_id=event.from_user.id, permissions=my_per_for_chat)
#     else:
#         print("Как-нибудь логируем эту ситуацию")
