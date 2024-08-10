from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
test_token = "7282874608:AAGRjppODJm9AVgrUIEzhDW9I0ZAnXtzv1o"
prod_token = "7238640608:AAF7VPTrFhqO1Jhhm6p2-vuIiShNDTykG4E"
bot = Bot(token=prod_token,
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))

user_ids = [1277329197, 314646803]