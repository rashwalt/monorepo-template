from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from ..core import Base
from ..mixin import TimestampMixin


class Message(Base, TimestampMixin):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    content: Mapped[str] = mapped_column(String(100), unique=False)
