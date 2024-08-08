from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database import db


class User(db.Model):
    id: Mapped[str] = mapped_column(primary_key=True)
    passwrod: Mapped[str] = mapped_column(nullable=False)

    def get_id(self):
        return self.id

    def check_password(self, password):
        return self.passwrod == password