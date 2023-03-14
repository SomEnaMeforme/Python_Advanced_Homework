from flask import Flask

app = Flask(__name__)


@app.route("/max_number/<path:numbers>")
def get_max(numbers) -> str:
    filter_numbers = list(filter(lambda x: x.isnumeric(), numbers.split('/')))
    if len(filter_numbers) != len(list(filter(lambda x: x != '', numbers.split('/')))):
        return 'Проверьте введенные данные'
    max_number = max([int(numb) for numb in filter_numbers])
    return f'Максимальное переданное число <i>{max_number}</i>'

if __name__ == "__main__":
    app.run(debug=True)
