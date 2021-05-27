from flask import Flask, render_template
import requests
from post import Post

blog_url = ""
response = requests.get(url=blog_url)
all_posts = response.json()

posts = []
for post in all_posts:
    post_object = Post(post["id"], post["title"], post["subtitle"], post["body"])
    posts.append(post_object)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template(template_name_or_list="index.html", posts=posts)


@app.route('/post/<int:blog_id>')
def post_page(blog_id):
    return render_template(template_name_or_list="post.html", id=blog_id, one_post=posts[blog_id - 1])


if __name__ == "__main__":
    app.run(debug=True)
