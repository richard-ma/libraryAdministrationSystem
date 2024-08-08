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

@app.route('/book/list')
def book_list():
    books = db.paginate(db.select(Book).order_by(Book.id))
    return render_template('book_list.tpl', books=books)

@app.route('/book/add', methods=['GET', 'POST'])
def book_add():
    if request.method == 'POST':
        book = Book()
        book.title = request.form.get('title')
        book.author = request.form.get('author')
        book.publisher = request.form.get('publisher')
        book.isbn = request.form.get('isbn')
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("book_list"))
    return render_template("book_add.tpl")


@app.route('/book/delete/<book_id>')
def book_delete(book_id):
    book = db.one_or_404(db.select(Book).filter_by(id=book_id))
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("book_list"))

@app.route('/book/update/<book_id>', methods=['GET', 'POST'])
def book_update(book_id):
    book = db.one_or_404(db.select(Book).filter_by(id=book_id))
    if request.method == 'POST':
        book.id = request.form.get('id')
        book.title = request.form.get('title')
        book.author = request.form.get('author')
        book.publisher = request.form.get('publisher')
        book.isbn = request.form.get('isbn')
        db.session.commit()
        book = db.one_or_404(db.select(Book).filter_by(id=book_id))
    return render_template('book_detail.tpl', **book.__dict__)


if __name__ == "__main__":
    app.run()