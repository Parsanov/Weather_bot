from aiogram import Router, types, F
from aiogram.filters import CommandStart
from keyboards.reply import geo_keyboard
from keyboards.inline import user_redirection_kb
import json


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

    await message.answer("📒 Записую твою геолокацію", reply_markup=user_redirection_kb())

    data = {
        "lat": lat,
        "lon": lon,
        "user_id": user_id,
        "user_name": user_name
    }

    with open("user_data.json", "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)




