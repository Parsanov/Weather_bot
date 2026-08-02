from aiogram import Router, types, F
from aiogram.filters import Command
from config import ADMIN_ID


router = Router()

@router.message(Command("admin"))
async def handle_admin(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        await message.answer("You are not allowed to use this command")
        return
    await message.answer(f"Hello my lord - {message.from_user.first_name}!")


@router.callback_query(F.data == "statistic")
async def handle_statistic(call : types.CallbackQuery):
    await call.message.edit_text("📈 Bot statistics: 100 users.")
