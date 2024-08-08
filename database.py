from flask_sqlalchemy import SQLAlchemy # type: ignore
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
