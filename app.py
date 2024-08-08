from flask import Flask
from flask import request, session, render_template, redirect
from book import Book
from user import User
from database import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "NNTIDUYYCUDIIDLSLEIDL"
db.init_app(app)


@app.route('/')
def index():
    user_id = request.args.get('user_id')
    return render_template('index.tpl', user_id=user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.tpl')
    else:
        id = request.form.get('id')
        password = request.form.get('password')

        user = db.one_or_404(db.select(User).filter_by(id=id))
        if user.check_password(password):
            session['user_id'] = id
            return redirect('/')
        else:
            return redirect('/login')


if __name__ == "__main__":
    app.run()