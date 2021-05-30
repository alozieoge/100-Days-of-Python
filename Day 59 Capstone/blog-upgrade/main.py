from flask import Flask, render_template
import requests

BLOG_URL = "https://api.npoint.io/4889420cb666bd3335db"
response = requests.get(url=BLOG_URL)
all_posts = response.json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template(template_name_or_list="index.html", all_blog_posts=all_posts)


@app.route('/about')
def get_about():
    return render_template(template_name_or_list="about.html")


@app.route('/contact')
def get_contact():
    return render_template(template_name_or_list="contact.html")


@app.route('/post/<int:num>')
def get_post(num):
    post_num = all_posts[num - 1]
    # Add images relative path (static) to json
    post_num["image"] = f"img/post-bg-{num}.jpg"

    return render_template(template_name_or_list="post.html", blog_post=post_num)


if __name__ == "__main__":
    app.run(debug=True)

