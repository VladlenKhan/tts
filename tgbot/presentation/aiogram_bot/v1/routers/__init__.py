from aiogram import Dispatcher

# routers
from tgbot.presentation.aiogram_bot.v1.routers.start import router as start_touer

all_routers = [
    start_touer
]


def include_all_routers(dp: Dispatcher) -> None:
    for router in all_routers:
        dp.include_router(router)
