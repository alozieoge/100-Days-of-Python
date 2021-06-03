from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import os
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

TMDB_API_KEY = os.environ.get("TMDB_API_KEY")
TMDB_AUTH_TOKEN = os.environ.get("TMDB_AUTH_TOKEN")

TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
TMDB_MOVIE_URL = "https://api.themoviedb.org/3/movie/"
TMDB_IMAGE_BASE = "https://image.tmdb.org/t/p/w500"

TMDB_API_KEY = "b901f89ef2025f956490f1896fa3f103"
TMDB_AUTH_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiOTAxZjg5ZWYyMDI1Zjk1NjQ5MGYxODk2ZmEzZjEwMyIsInN1YiI6IjYwYjkxYWJkY2FkYjZiMDA2ZjAwNjZkYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.iF-u1kx_ouURQhZJosEILeMtIBOiEdfm2SDjVrwn_u4"

search_params = {
    "api_key": TMDB_API_KEY,
    "language": "en-US",
    "query": "",
    "page": 1,
}

movie_params = {
    "api_key": TMDB_API_KEY,
    "language": "en-US",
}


# Create table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, unique=True, nullable=False)
    rating = db.Column(db.Float, default=None)
    ranking = db.Column(db.Integer, default=None)
    review = db.Column(db.String, default=None)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Movie %r>' % self.title


db.create_all()

# # New entry
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's
#     sniper rifle. Unable to leave or receive outside help,
#     Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
#
# db.session.add(new_movie)
# db.session.commit()


# Create a WTForm to edit a movie rating and review
class RateMovieForm(FlaskForm):
    rating = FloatField(label="Your Rating Out of 10 e.g. 8.5", validators=[DataRequired()])
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


# Create a WTForm to add movies
class AddMovieForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


@app.route("/")
def home():
    all_movies = db.session.query(Movie).all()
    # all_movies.sort(key=lambda x: x.rating, reverse=False)
    sorted_movies = sorted(all_movies, key=lambda x: (x.rating is not None, x.rating), reverse=False)
    ranked_movies = []
    for i, movie in enumerate(sorted_movies):
        movie.ranking = i + 1
        ranked_movies.append(movie)
    return render_template("index.html", all_movies=ranked_movies)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    edit_form = RateMovieForm()
    movie_id = id
    movie = Movie.query.get(movie_id)
    if edit_form.validate_on_submit():
        movie.rating = edit_form.rating.data
        movie.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', edit_form=edit_form, movie=movie)


@app.route('/delete/<int:id>')
def delete(id):
    movie_id = id
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()

    all_movies = db.session.query(Movie).all()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    add_form = AddMovieForm()
    if add_form.validate_on_submit():
        # print(add_form.title.data)
        search_params["query"] = add_form.title.data
        response = requests.get(url=TMDB_SEARCH_URL, params=search_params)
        results = response.json()["results"]
        return render_template('select.html', search_results=results)
    return render_template('add.html', add_form=add_form)


@app.route('/select/<int:result_id>')
def select(result_id):
    response = requests.get(url="".join([TMDB_MOVIE_URL, str(result_id)]), params=movie_params)
    result = response.json()
    movie = Movie()
    movie.title = result["original_title"]
    movie.description = result["overview"]
    movie.year = int(result["release_date"].split("-")[0])
    movie.img_url = "".join([TMDB_IMAGE_BASE, result["backdrop_path"]])
    movie.rating = None
    movie.review = None
    movie.ranking = None

    # print(movie.title, movie.year, movie.img_url, movie.description)
    db.session.add(movie)
    db.session.commit()

    return redirect(url_for('edit', id=movie.id))

# def tmdb_search(query):
#
#
#
#     return



if __name__ == '__main__':
    app.run(debug=True)
