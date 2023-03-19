from flask import Flask
from flask_wtf.form import FlaskForm
from wtforms import fields
from wtforms import validators as v
from task2 import number_length, NumberLength

app = Flask(__name__)


class RegistrationFields(FlaskForm):

    email = fields.StringField(validators=[v.InputRequired(message='Поле является обязательным'),
                                           v.Email("Почта не соответствует формату")])
    phone = fields.IntegerField(validators=[v.InputRequired(message='Поле является обязательным'),
                                            number_length(10, 10)])
    name = fields.StringField(validators=[v.InputRequired(message='Поле является обязательным')])
    address = fields.StringField(validators=[v.InputRequired(message='Поле является обязательным')])
    index = fields.IntegerField(validators=[v.InputRequired(message='Поле является обязательным')])
    comment = fields.StringField()


@app.route('/registration', methods=['POST'])
def registration():
    form = RegistrationFields()

    if form.validate_on_submit():
        return "Данные успешно получены"
    else:
        return form.errors


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
