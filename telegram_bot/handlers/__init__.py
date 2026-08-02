from aiogram import Router, types
from .start import router as start_command
from .user import router as user_router
from .admin import router as admin


def start_handler() -> Router:
    main_router = Router()

    main_router.include_routers(
        start_command,
        user_router,
        admin
    )

    return main_router