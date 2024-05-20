from loader import dp, bot, ADMIN
from aiogram import types
from utils.database import users as dbusers
from keyboards.default import get_start_admin,get_start_btn


@dp.message_handler(commands=['users'])
async def users(message: types.Message):
    if message.from_user.id == int(ADMIN):
        info = dbusers.get_user()
        number_of_user = len(info)
        print(f"number of users: {number_of_user}")
        for i in range(number_of_user):
            await message.answer(f"Userlar({number_of_user}) haqidagi malumotlar:\n"
                                 f"{info[i][0]} - {info[i][1]}\n"
                                 f"Username: {info[i][2]}\n"
                                 f"Phone number: {info[i][3]}\n"
                                 f"Chat_id: {info[i][4]}", reply_markup=await get_start_admin())

# @dp.message_handler(commands=['users'])
# async def users(message: types.Message):
#     if message.from_user.id == int(ADMIN):
#         info = dbusers.get_user()
#         number_of_user = len(info)
#         print(f"number of users: {number_of_user}")
#         for i in range(number_of_user):
#             await message.answer(f"Userlar({number_of_user}) haqidagi malumotlar:\n"
#                                  f"{info[i][0]} - {info[i][1]}\n"
#                                  f"Username: {info[i][2]}\n"
#                                  f"Phone number: {info[i][3]}\n"
#                                  f"Chat_id: {info[i][4]}", reply_markup=await get_start_admin())
#

#
# @dp.message_handler(commands=['aboutme'])
# async def aboutme(message: types.Message):
#     user_info = dbusers.get_user_by_id(message.from_user.id)
#     text = (f"Foydalanuvchi haqida ma'lumot:\n"
#             f"ID number:: {user_info[0]}\n"
#             f"Firts/Last name: {user_info[1]}\n"
#             f"Username: {user_info[2]}\n"
#             f"Phone number: {user_info[3]}\n"
#             f"Chat_id: {user_info[4]}")
#     if message.from_user.id == int(ADMIN):
#         await message.answer(text,reply_markup=await get_start_admin())
#     else:
#         await message.answer(text,reply_markup=await get_start_btn())