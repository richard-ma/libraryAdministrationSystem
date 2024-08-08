from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database import db


class User(db.Model):
    id: Mapped[str] = mapped_column(primary_key=True)
    passwrod: Mapped[str] = mapped_column(nullable=False)