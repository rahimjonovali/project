from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline import get_social_ibtn
from keyboards.default import get_start_btn

from loader import CHANNEL, bot


class CustomMiddleware(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        print(message.text)
        if not message.text == '/start' and not message.text == '/voice':
            user = message.from_user
            if user.id:
                for channel in CHANNEL:
                    member = await  bot.get_chat_member(chat_id=channel.get('channel_id'), user_id=int(user.id))
                    if member.status == "left":
                        # print(f"You're a really {member.status}")
                        iline_button = InlineKeyboardMarkup()
                        await message.answer(f"Siz ushbu {channel.get('channel_name')} kanalga a'zo bo'lgamagansiz!!!")
                        iline_button.add(InlineKeyboardButton(text=channel.get('channel_name'),
                                                              url=f"https://t.me/{channel.get('channel_url')}",
                                                              reply_markup=iline_button))
                        raise CancelHandler()
                    else:
                        print(member)
                        print(f"{member.status}")
            else:
                await  message.answer("Username is required")
                raise CancelHandler()
        elif message.text == '/voice':
            inline_button = InlineKeyboardMarkup()
            for channel in CHANNEL:
                check = await bot.get_chat_member(chat_id=channel.get('channel_id'), user_id=int(message.from_user.id))
                inline_button.add(InlineKeyboardButton(text=channel.get('channel_name'), url=f"https://t.me/{channel.get('channel_url')}"))
                if check.status == "left":
                    await message.answer("Ushbu servicedan foydalanish uchun\nQuyidagi kanallarga a'zo bo'ling",reply_markup=inline_button)
                    raise CancelHandler()
