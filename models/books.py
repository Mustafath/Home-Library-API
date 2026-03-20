from datetime import date
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, Mapped, mapped_column

class Model(MappedAsDataclass, DeclarativeBase):
    ...


class Book(Model):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    title: Mapped[str]
    author: Mapped[str]
    description: Mapped[str]
    publication_date: Mapped[date]
    pages: Mapped[int]
    is_read: Mapped[bool]