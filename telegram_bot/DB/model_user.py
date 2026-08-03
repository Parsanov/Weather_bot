from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Float, String


class Base(DeclarativeBase):
    pass

class User(Base):

    __tablename__ = "user"

    user_id : Mapped[int] = mapped_column(primary_key=True)
    user_name : Mapped[str] = mapped_column(String, nullable=False)
    lat: Mapped[float] = mapped_column(Float, nullable=False)
    lon: Mapped[float] = mapped_column(Float, nullable=False)

