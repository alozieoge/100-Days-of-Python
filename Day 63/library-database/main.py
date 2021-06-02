from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title


db.create_all()


@app.route('/')
def home():
    # Read all records by Query
    all_books = db.session.query(Book).all()
    # print(all_books)
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        author = request.form['author']
        rating = request.form['rating']
        # book = {"name": name,
        #         "author": author,
        #         "rating": rating, }
        # all_books.append(book)
        # print(all_books)
        # Create and add new record to table
        book = Book(title=name, author=author, rating=rating)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html')


# @app.route('/submit', methods=['POST'])
# def receive_data():
#     name = request.form['name']
#     author = request.form['author']
#     rating = request.form['rating']
#     book = {"name": name,
#             "author": author,
#             "rating": rating, }
#     all_books.append(book)
#     print(all_books)
#     # NOTE: You can use the redirect method from flask to redirect to another route
#     # e.g. in this case to the 'add' page after the form has been submitted.
#     return redirect(url_for('add'))


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        # Update Record
        book_id = request.form['id']
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('book_id')
    book_object = Book.query.get(book_id)
    return render_template("edit.html", book=book_object)


@app.route('/delete')
def delete():
    book_id = request.args.get('book_id')
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

