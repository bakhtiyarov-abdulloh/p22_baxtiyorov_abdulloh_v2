from uuid import uuid4

from aiogram import Router, F, Bot
from aiogram.enums import ChatType
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, message

from config import db

main_router = Router()

save_user = {}
class Msg(StatesGroup):
    user_id = State()
    msg = State()

@main_router.message(Command(commands='msg'))
async def msg(message: Message, bot:Bot):
    await message.answer(text=db['user_id'])


@main_router.message(F.chat.type.in_({ChatType.GROUP, ChatType.SUPERGROUP}))
async def user_message(message: Message, bot:Bot):
    user_id = message.from_user.id
    db[user_id] = message.text
    await message.answer(text='saqalndi')


