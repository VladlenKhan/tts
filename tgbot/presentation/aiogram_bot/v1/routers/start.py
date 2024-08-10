from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def command_start(message: Message) -> None:
    await message.answer(
        text="Здравствуйте! Здесь вы будете получать данные из форм, отправленных на сайте AVTOSTANDART!"
    )