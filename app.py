from flask import Flask
from book import Book
from user import User
from database import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)


@app.route('/')
def index():
    return "hello world"


if __name__ == "__main__":
    app.run()