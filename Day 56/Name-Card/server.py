from flask import Flask
from flask import render_template

app = Flask(import_name=__name__)


@app.route('/')
def home():
    return render_template(template_name_or_list="index.html")


if __name__ == "__main__":
    app.run(debug=True)
