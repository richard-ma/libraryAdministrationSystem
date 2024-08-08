from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date

from database import db


class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[str] = mapped_column(nullable=False) 
    publisher: Mapped[str] = mapped_column(nullable=False)
    isbn: Mapped[str] = mapped_column(nullable=False)
    can_borrowed: Mapped[bool] = mapped_column(nullable=False, default=True)
    borrowed_by: Mapped[str] = mapped_column(nullable=True)
    return_date: Mapped[date] = mapped_column(nullable=True)