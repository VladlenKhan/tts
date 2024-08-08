from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

bot = Bot(token="7282874608:AAGRjppODJm9AVgrUIEzhDW9I0ZAnXtzv1o",
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))