from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime as dt
from flask_moment import Moment


## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# SET UP CKEDITOR
app.config['CKEDITOR_PKG_TYPE'] = 'full-all'
ckeditor = CKEditor(app)

# Flask Moment for Time Keeping
moment = Moment(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return "<BlogPost %r>" % self.title


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post_id>", methods=["GET"])
def show_post(post_id):
    posts = db.session.query(BlogPost).all()
    requested_post = None
    for blog_post in posts:
        if blog_post.id == post_id:
            print(blog_post.id)
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=['GET', 'POST'])
def new_post():
    new_form = CreatePostForm()
    today = dt.now()
    if new_form.validate_on_submit():
        blog_post = BlogPost(
            title=request.form.get("title"),
            subtitle=request.form.get("subtitle"),
            author=request.form.get("author"),
            img_url=request.form.get("img_url"),
            date=today.strftime("%B %d, %Y"),
            body=request.form.get("body")
        )

        # print(blog_post)
        db.session.add(blog_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", form=new_form, to_edit=False)


@app.route("/edit/<int:post_id>", methods=['GET', 'POST'])
def edit_post(post_id):
    post_to_edit = db.session.query(BlogPost).get(post_id)
    edit_form = CreatePostForm(
        title=post_to_edit.title,
        subtitle=post_to_edit.subtitle,
        author=post_to_edit.author,
        img_url=post_to_edit.img_url,
        body=post_to_edit.body
    )

    if request.method == "POST":
        today = dt.now()
        post_to_edit.title = request.form.get("title")
        post_to_edit.subtitle = request.form.get("subtitle")
        post_to_edit.author = request.form.get("author")
        post_to_edit.img_url = request.form.get("img_url")
        # post_to_edit.date = today.strftime("%B %d, %Y")  # Keep the original date
        post_to_edit.body = request.form.get("body")

        db.session.commit()
        return redirect(url_for("show_post", post_id=post_to_edit.id))

    return render_template("make-post.html", form=edit_form, to_edit=True)


@app.route('/delete-post/<int:post_id>')
def delete_post(post_id):
    post_to_delete = db.session.query(BlogPost).get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()

    return redirect(url_for("get_all_posts"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)