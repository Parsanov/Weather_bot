from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import  InlineKeyboardMarkup
from aiogram import Router

router = Router()

def get_weather_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(text="Переглянути погода зараз?", callback_data="weather_now")
    builder.button(text="Переглянути прогноз погоди на 8 годин? ", callback_data="weather_then" )

    builder.adjust(1)

    return builder.as_markup()



def user_redirection_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(text="Перейдіть до пареметрів", callback_data="parameters")

    builder.adjust(1)

    return builder.as_markup()