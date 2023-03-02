from aiogram.types import Message
from aiogram import Dispatcher


async def start_handler(message: Message):
    await message.answer(f'Привет, {message.from_user.full_name}!')


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
