from .admin import checkAdmin
from .checkText import checkText
from loader import dp

if __name__ == "filters":
    dp.filters_factory.bind(checkText)