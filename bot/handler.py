from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.utils import get_usd_to_rub_rate

router = Router()

@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Добрый день. Как вас зовут?")

@router.message(F.text)
async def start_command(message: Message):
    rate = get_usd_to_rub_rate()
    await message.answer(f"Рад знакомству, {message.text}! Курс доллара сегодня {rate}р")