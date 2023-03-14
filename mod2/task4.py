from flask import Flask
from datetime import datetime

app = Flask(__name__)

class Wishes:
    WEEKDAYS_WISHES = ('Хорошего понедельника', 'Хорошего вторника', 'Хорошей среды', 'Хорошего четверга',
                       'Хорошей пятницы', 'Хорошей субботы', 'Хорошего воскресенья')
    @staticmethod
    @app.route("/hello-world/<username>")
    def hello_user(username) -> str:
        weekday = datetime.today().weekday()
        return f'Привет, {username}. {Wishes.WEEKDAYS_WISHES[weekday]}!'

if __name__ == "__main__":
    app.run(debug=True)
