from sqlalchemy import select

from DB.dp import async_session
from DB.model_user import User


async def add_user(user_id: int, name: str, lat: float, lon: float):
    async with async_session() as session:
        user = await session.get(User, user_id)

        if user:
            user.user_name = name
            user.lat = lat
            user.lon = lon
        else:
            user = User(user_id=user_id, user_name=name, lat=lat, lon=lon)
            session.add(user)

        await session.commit()


async def get_user(user_id: int) -> User:
    async with async_session() as session:
        return await session.get(User, user_id)


async def get_all_users() -> list[User]:
    async with async_session() as session:
        result = await session.execute(select(User))
        return list(result.scalars().all())
