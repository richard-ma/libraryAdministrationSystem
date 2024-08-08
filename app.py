from flask import Flask
from flask import request, session, render_template, redirect, url_for
from book import Book
from user import User
from database import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "NNTIDUYYCUDIIDLSLEIDL"
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.tpl', **request.args)

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
            return redirect(url_for('index', user_id=id))
        else:
            return redirect(url_for('login'))

@app.route('/logout')
def logout():
    del session['user_id']
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()