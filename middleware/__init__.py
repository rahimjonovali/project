from  loader import dp
from .channel import  CustomMiddleware

if __name__ == "middleware":
    dp.middleware.setup(CustomMiddleware())