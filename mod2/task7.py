from flask import Flask
from datetime import datetime


app = Flask(__name__)


class Finance:
    storage = dict()

    @staticmethod
    def validate_year(year: int) -> bool:
        return year >= 1800 and year <= datetime.now().year

    @staticmethod
    def validate_month(month: int) -> bool:
        return month >= 1 and month <= 12

    @staticmethod
    @app.route('/add/<date_str>/<int:expense>')
    def add_month_expense(date_str: str, expense: int) -> str:
        date = datetime.strptime(date_str, '%Y%m%d').date()
        Finance.storage.setdefault(date.year, {}).setdefault(date.month, 0)
        Finance.storage[date.year][date.month] += expense
        return 'Данные успешно обновлены'

    @staticmethod
    @app.route('/calculate/<int:year>')
    def calculate_year_expense(year: int) -> str:
        if not(Finance.validate_year(year)):
            return 'Некорректные значения входных данных'
        if year in Finance.storage:
            return str(sum(Finance.storage[year].values()))
        return str(0)

    @staticmethod
    @app.route('/calculate/<int:year>/<int:month>')
    def calculate_month_expense(year, month) -> str:
        if not(Finance.validate_year(year)) or not(Finance.validate_month(month)) :
            return 'Некорректные значения входных данных'
        if year in Finance.storage and month in Finance.storage[year]:
            return str(Finance.storage[year][month])
        return str(0)


if __name__ == "__main__":
    app.run(debug=True)