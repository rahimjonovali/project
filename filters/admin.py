from aiogram import types
from loader import ADMIN
from aiogram.dispatcher.filters import BoundFilter
class checkAdmin(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        if message.from_user.id == int(ADMIN):
            return True
        else:
            return False
