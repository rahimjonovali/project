from aiogram.dispatcher.filters.state import State,StatesGroup

class MyStates(StatesGroup):
    request_message = State()
    request_phone = State()