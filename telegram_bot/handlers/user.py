from aiogram import Router, types, F
from aiogram.filters import Command
from keyboards.inline import get_weather_kb
from sevice.weather_now_service import weather_now_service
import json

router = Router()



async def show_weather_parameters(message: types.Message):
    await message.answer("Виберіть параметр: ", reply_markup=get_weather_kb())


@router.message(Command("weather"))
async def user_pick_weather(message: types.Message):
    await show_weather_parameters(message)

@router.callback_query(F.data == "parameters")
async def user_pick_weather(callback: types.CallbackQuery):
    await callback.answer()
    await show_weather_parameters(callback.message)



def format_weather_data(data):
    return (
        f"📍 <b>{data['city']}</b>\n\n"
        f"🌡 Температура: <b>{round(data['temperature'])}°C</b>\n"
        f"🤔 Відчувається як: {round(data['feels_like'])}°C\n"
        f"☁️ {data['description'].capitalize()}\n"
        f"💧 Вологість: {data['humidity']}%\n"
        f"💨 Вітер: {data['wind_speed']} м/с"
    )

@router.callback_query(F.data == "weather_now")
async def user_pick_weather(callback: types.CallbackQuery):
    await callback.answer()

    with open("user_data.json", "r") as f:
        data = json.load(f)

    if callback.from_user.id == data["user_id"]:
        weather_data = await weather_now_service(data["lat"], data["lon"])
        text = format_weather_data(weather_data)
        await callback.message.answer(
            text, parse_mode="html"
        )
    else:
        await callback.message.answer("Вашої геолокації не знайдено :(")

@router.callback_query(F.data == "weather_then")
async def user_pick_weather(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Weather then")

