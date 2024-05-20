
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def get_social_ibtn():
    ibtn = InlineKeyboardMarkup(resize_keyboard=True)
    ibtn.add(InlineKeyboardButton('youtube', callback_data='youtube'))
    ibtn.add(InlineKeyboardButton('google', url='https://www.google.com/',callback_data='google'))
    ibtn.add(InlineKeyboardButton('geeks', url='https://geeks-online.uz/',callback_data='geeks'))
    return ibtn


async def get_voice_ibtn():
    ibtn1 = InlineKeyboardMarkup(resize_keyboard=True)
    ibtn1.add(InlineKeyboardButton('👍', callback_data='like'))
    ibtn1.add(InlineKeyboardButton('👎', callback_data='dislike'))
    return ibtn1
