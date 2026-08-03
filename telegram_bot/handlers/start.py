from aiogram import Router, types, F
from aiogram.filters import CommandStart
from keyboards.reply import geo_keyboard
from keyboards.inline import user_redirection_kb
from DB.repository import add_user


router = Router()

@router.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer(f"Hello {message.from_user.first_name}!",
                         reply_markup=geo_keyboard())



@router.message(F.location)
async def handle_location(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    await message.answer("📒 Записую твою геолокацію")

    await add_user(user_id, user_name, lat, lon)

    await message.answer("Твоя геолокація успішно записана", reply_markup=user_redirection_kb())




