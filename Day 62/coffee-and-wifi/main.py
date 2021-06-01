from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL
import csv

DATA_FILE = 'cafe-data.csv'

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField(label="Cafe name", validators=[DataRequired()])
    location = StringField(label="Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    open_time = StringField(label="Opening Time e.g. 8AM", validators=[DataRequired()])
    close_time = StringField(label="Closing Time e.g. 5:30PM", validators=[DataRequired()])
    coffee = SelectField(label="Coffee Rating",
                         choices=['❌', '☕️', '☕️☕️', '☕️☕️☕️',
                                  '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'],
                         validators=[DataRequired()])
    wifi = SelectField(label="Wifi Strength Rating", choices=['❌', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'],
                       validators=[DataRequired()])
    power = SelectField(label="Power Socket Availability", choices=['❌', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'],
                        validators=[DataRequired()])
    submit = SubmitField(label="Submit")

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------
#
#
# class AddForm(FlaskForm):
#     def __init__ (self):
#         super().__init__()
#         self.cafe_name = StringField(label="Cafe name", validators=[DataRequired])
#         self.cafe_location = StringField(label="Cafe Location on Google Maps (URL)", validators=[DataRequired, URL])
#         self.opening_time = StringField(label="Opening Time e.g. 8AM", validators=[DataRequired])
#         self.closing_time = StringField(label="Closing Time e.g. 5:30PM", validators=[DataRequired])
#         self.coffee_rating = StringField(label="Coffee Rating", validators=[DataRequired])
#         self.wifi_rating = StringField(label="Wifi Strength Rating", validators=[DataRequired])
#         self.power_socket = StringField(label="Power Socket Availability", validators=[DataRequired])
#         self.submit = SubmitField(label="Submit")
#
#
# add_form = AddForm()


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    if form.validate_on_submit():
        # print("True")
        new_data = [form.cafe.data, form.location.data, form.open_time.data, form.close_time.data,
                    form.coffee.data, form.wifi.data, form.power.data]
        write_csv(DATA_FILE, new_data)
        # list_of_rows = read_csv(DATA_FILE)
        # return render_template('cafes.html', cafes=list_of_rows)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    list_of_rows = read_csv(DATA_FILE)
    return render_template('cafes.html', cafes=list_of_rows)


def read_csv(csv_filename):
    list_of_rows = []
    with open(csv_filename, newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        for row in csv_data:
            # print(row)
            list_of_rows.append(row)
    return list_of_rows


def write_csv(csv_filename, data):
    with open(file=csv_filename, mode='a', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(data)


if __name__ == '__main__':
    app.run(debug=True)
