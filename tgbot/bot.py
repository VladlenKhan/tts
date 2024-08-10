import asyncio
import logging
import sys

from aiogram import Dispatcher

from tgbot.presentation.aiogram_bot.v1.routers import include_all_routers

from tgbot.config import bot


async def main() -> None:

    dp = Dispatcher()
    include_all_routers(dp=dp)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())