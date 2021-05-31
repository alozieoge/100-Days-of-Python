from flask import Flask, render_template #, url_for, redirect
from login_form import LoginForm
from flask_bootstrap import Bootstrap

admin_email = "admin@email.com"
admin_password = 12345678

app = Flask(__name__)
app.secret_key = "some secret string"
Bootstrap(app=app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    # login_form.validate_on_submit() # This line forces the login form to be submitted (POST request) irrespective of
    # whether a page loading (GET request) is intended.
    # if request.method == 'POST':
    #     return render_template('login.html')
    if login_form.validate_on_submit():
        # print(login_form.email.data, login_form.password.data)
        if login_form.email.data == admin_email and int(login_form.password.data) == admin_password:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    # else:
    #     print("Loading login.html")
    return render_template('login.html', form=login_form)


@app.route('/test')
def test_page():
    print("Test")
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)

