from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


async def get_start_admin():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add(KeyboardButton('/start')).insert(KeyboardButton('/help'))
    btn.add(KeyboardButton('/users')).insert(KeyboardButton('/post'))
    return btn