import requests
from aiogram.dispatcher import FSMContext
from states import MyStates
from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from keyboards.inline import get_voice_ibtn, get_social_ibtn
from keyboards.default import get_help_btn, get_start_btn, get_start_admin
from loader import dp, bot
from loader import ADMIN
from utils.database import users as dbusers
from filters import checkAdmin

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if checkAdmin():
        await message.answer(f"Assalamu alaykum admin!!!", reply_markup=await get_start_admin())
        await message.delete()
    else:
        user = dbusers.get_user_by_id(message.from_user.id)
        if not user:
            fio = f"{message.from_user.first_name} {message.from_user.last_name}"
            dbusers.create_user(fio, message.from_user.username, message.from_user.id)

        await message.answer("Xush kelibsiz", reply_markup=await get_start_btn())


@dp.message_handler(checkAdmin(),commands=['post'])
async def post(message: types.Message):
     await message.answer("Xabarni kiriting:")
     await MyStates.request_message.set()


@dp.message_handler(checkAdmin(),state=MyStates.request_message)
async def request_message(message: types.Message,state: FSMContext):
    # if message.from_user.id == int(ADMIN):
    info = dbusers.get_user()
    for item in info:
        await  bot.send_message(chat_id=item[4],text=message.text)
    await state.finish()

@dp.message_handler(commands=['voice'])
async def voice(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://yandex.ru/images/search?pos=26&from=tabbar&img_url=https%3A%2F%2Fsun9-5.userapi.com%2Fs%2Fv1%2Fif2%2FaApLuUplYwTks7vk4v4IebfgtFYZuixOCkG7HtBA31XEMffTfvET9kPqTLcwzTGnmBxUUPrIGiF1TpRzO7hMDKi0.jpg%3Fsize%3D75x75%26quality%3D95%26type%3Dalbum&text=real+madrid&rpt=simage&lr=10335',
                          caption="Sizga yoqdimi", reply_markup=await get_voice_ibtn())
    # await message.delete()


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def contact(message: types.Message):
    dbusers.update_user(message.contact.phone_number, message.from_user.id)
    await message.answer("Qabul qilindi!!")
    # await message.delete()

@dp.message_handler(commands=['aboutme'])
async def aboutme(message: types.Message):
    user_info = dbusers.get_user_by_id(message.from_user.id)
    text = f"""Foydalanuchi haqida ma'lumot:\n
     ID number:  {user_info[0]}\n
     Firts/Last name:  {user_info[1]}\n
     Username:  {user_info[2]}\n
     Phone number:  {user_info[3]}\n
     Chat_id:  {user_info[4]}
            """
    await message.answer(text)


# har bir user uchun hisobla
counter1 = 0
counter2 = 0

@dp.callback_query_handler()
async def callback_query(call: types.CallbackQuery):
    global counter1, counter2
    if call.data == 'like':
        counter1 += 1
        await call.answer(f"{counter1} {call.data}")
    elif call.data == 'dislike':
        counter2 += 1
        await call.answer(f"{counter2} {call.data}")

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer("Sizga qanday yordam berolamiz", reply_markup=await get_social_ibtn())
    await message.delete()

@dp.message_handler(commands=['currency'])
async def currency(message: types.Message):
    response = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
    res = response.json()
    for item in res:
        currency = item["Ccy"]
        if currency == "USD" or currency == "EUR" or currency == "RUB":
            name = item["CcyNm_UZ"]
            rate = item["Rate"] #kurs narxi
            date = item["Date"]
            text = f"""
               <em>Shahar</em> - <b>{name}</b>
               <em>Date</em> - <b>{date}</b>
               <em>Price</em> - <b>{rate}</b>
               <em>Currency type</em> - <b>{currency}</b>
               """
            await message.answer(text,parse_mode='HTML')

@dp.message_handler(commands=['weather'])
async def weather(message: types.Message):
    response = requests.get("http://api.weatherapi.com/v1/current.json?key=637a0367057542d9936143247240705&q=Tashkent")
    res = response.json()
    name = res["location"]['name']
    country = res['location' ]['country']
    tz_id = res['location']['tz_id']
    localtime = res['location']['localtime']
    temp_c = res['current']['temp_c']
    wind_mph = res['current']['wind_mph']
    text = await text_weather(name, country, tz_id, localtime, temp_c, wind_mph)
    await message.answer(text,parse_mode='HTML')

async def text_weather(name,country,tz_id,localtime,temp_c,wind_mph):
    text = f"""
    <em>Shahar</em> - <b>{name}</b>
    <em>Davlat</em> - <b>{country}</b>
    <em>Time zone</em> - <b>{tz_id}</b>
    <em>LocatTime</em> - <b>{localtime}</b>
    <em>Xarorat</em>:  <b>{'+' if temp_c > 0 else '-'}{temp_c}</b>
    <em>Shamol tezligi</em> - <b>{wind_mph}</b>
    
    """
    return text

@dp.message_handler(commands=['sticker'])
async def sticker(message: types.Message):
    await bot.send_sticker(message.chat.id,
                           sticker="CAACAgIAAxkBAAEL-dtmJ7V4HZktZ63zL-aLrbCvcORWrAACUQcAAnlc4gnHnvLkisbo0jQE")
    await message.delete()


@dp.message_handler(commands=['photo'])
async def photo(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://avatars.mds.yandex.net/i?id=72cdc5929409f76e7ec2ccc97e91c048b204e319-12371687-images-thumbs&n=13",
                         reply_markup=await get_start_btn())

    await message.delete()


@dp.message_handler(commands=['ibrohim'])
async def photo(message: types.Message):
    with open("D:/PyCharm/Aiogram_newModule/new_features/photo_2023-10-20_11-32-59.jpg", "rb") as photo_file:
        await bot.send_photo(chat_id=message.chat.id, photo=photo_file, )
    await message.delete()


@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=message.text, reply_markup=ReplyKeyboardRemove())
