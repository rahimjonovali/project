import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

storage = MemoryStorage()

CHANNEL = [{
    "channel_id": -1002062193429,
    "channel_url": 'new_l0arn0rs',
    "channel_name": 'GeeksForGeeks',
}]
ADMIN = os.getenv('ADMIN')
bot = Bot(token=os.getenv('BOT_TOKEN'))


dp = Dispatcher(bot,storage= storage)
