from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def  get_start_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add(KeyboardButton('/start')).insert(KeyboardButton('/voice'))
    btn.add(KeyboardButton('/help')).insert(KeyboardButton('/aboutme'))
    btn.add(KeyboardButton('/contact', request_contact=True)).insert(KeyboardButton('/photo'))
    return btn



async def get_help_btn():
    btn1 = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1.add(KeyboardButton('/photo')).insert(KeyboardButton('/Ibrohim'))
    btn1.add(KeyboardButton('/contact')).insert(KeyboardButton('/sticker'))
    return btn1
