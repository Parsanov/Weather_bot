from aiogram import Router, types, F
from aiogram.filters import Command
from keyboards.inline import get_weather_kb
from sevice.weather_service import weather_now, weather_then
from DB.repository import get_user
from datetime import datetime

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



def format_weather_now_data(data):
    return (
        f"📍 <b>{data['city']}</b>\n\n"
        f"🌡 Температура: <b>{round(data['temperature'])}°C</b>\n"
        f"🤔 Відчувається як: {round(data['feels_like'])}°C\n"
        f"☁️ {data['description'].capitalize()}\n"
        f"💧 Вологість: {data['humidity']}%\n"
        f"💨 Вітер: {data['wind_speed']} м/с"
    )


def format_weather_then_data(data: dict) -> str:
    city = data['city']
    forecast = data['forecast']

    lines = [f"📍 <b>Прогноз для {city}</b>\n"]

    for entry in forecast:
        dt = datetime.strptime(entry['datetime'], "%Y-%m-%d %H:%M:%S")
        date_str = dt.strftime("%d.%m")
        time_str = dt.strftime("%H:%M")

        lines.append(
            f"🕐 <b>{date_str} {time_str}</b>\n"
            f"🌡 {round(entry['temperature'])}°C "
            f"(відчувається як {round(entry['feels_like'])}°C)\n"
            f"☁️ {entry['description'].capitalize()}\n"
            f"💧 Вологість: {entry['humidity']}%\n"
        )

    return "\n".join(lines)




@router.callback_query(F.data == "weather_now")
async def user_pick_weather(callback: types.CallbackQuery):
    await callback.answer()
    try:
        user = await get_user(callback.from_user.id)

        if not user:
            await callback.message.answer("Спочатку надішли свою геолокацію 📍")
            return

        data = await weather_now(user.lat, user.lon)
        text = format_weather_now_data(data)

        await callback.message.answer(text, parse_mode="HTML", reply_markup=get_weather_kb())


    except Exception as e:
        await callback.message.answer(f"Сталася помилка: {e}")




@router.callback_query(F.data == "weather_then")
async def user_pick_weather(callback: types.CallbackQuery):
    await callback.answer()

    try:
        user = await get_user(callback.from_user.id)

        if not user:
            await callback.message.answer("Спочатку надішли свою геолокацію 📍")
            return

        data = await weather_then(user.lat, user.lon)
        text = format_weather_then_data(data)

        await callback.message.answer(text, parse_mode="HTML", reply_markup=get_weather_kb())

    except Exception as e:
        await callback.message.answer(f"Сталася помилка: {e}")

