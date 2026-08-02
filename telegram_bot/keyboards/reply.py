from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def geo_keyboard() -> ReplyKeyboardMarkup:

    builder = ReplyKeyboardBuilder()

    builder.button(text="Поділись своєю геолокацією", request_location=True)

    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)

