import subprocess
import time
from flask import Flask

from flask_wtf.form import FlaskForm
from wtforms import fields, validators as v

app = Flask(__name__)


class PythonProgram(FlaskForm):
    body = fields.StringField()
    max_time = fields.IntegerField(validators=[v.NumberRange(0, 30)])


def run_code(body: str, max_time: int) -> str:
    command = ['prlimit', '--nproc=1:1', 'python', '-c', body]
    start = time.time()
    with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
        end = time.time() - start
        if (end > max_time):
            raise TimeoutError
        return str(process.stdout.read()) + '/n' + str(process.stderr.read())




@app.route('/python_code', methods=['POST'])
def get_code() -> str:
    form = PythonProgram()
    if form.validate_on_submit():
        body = form.data['body']
        time = form.data['max_time']
        return run_code(body, time)
    else:
        return 'Проверьте введённые данные'


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
