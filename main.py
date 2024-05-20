from aiogram import executor
from loader import dp
import filters
import middleware
import handlers

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
