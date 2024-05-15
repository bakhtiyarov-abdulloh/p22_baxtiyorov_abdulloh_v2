from uuid import uuid4

from aiogram import Router, F
from aiogram.enums import ChatType
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from config import db

main_router = Router()


def write_db(message, username):
    messages_ = db["msg"]
    messages_.append(message)
    db["msg"] = messages_
    users = db['users']
    if not users.get(username):
        users[username] = []
    users[username].append(message)
    db['users'] = users


@main_router.message(Command(commands='msg'))
async def message(message: Message):
    msg = f'gruppada yozilgan xabarlar soni: {len(db['msg'])}'
    await message.answer(msg)
    if message.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
        write_db(message.text, message.from_user.username)
        write_db(msg, 'p22_baxtiyorov_abdulloh_2_bot)')

@main_router.message(F.chat.type.in_({ChatType.GROUP, ChatType.SUPERGROUP}))
async def user_message(message: Message):
    msg = message.text.split(' @')
    if len(msg) == 2 and msg[0] == 'user msg' and db['users'].get(msg[1]):
        msg = f'@{msg[1]} ga tegishli xabarlar soni {len(db["users"][msg[-1]])}'
        await message.answer(text=msg)
