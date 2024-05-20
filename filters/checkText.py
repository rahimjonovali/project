from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class checkText(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        if message.text.isalpha():
            return True
        else:
            return False
