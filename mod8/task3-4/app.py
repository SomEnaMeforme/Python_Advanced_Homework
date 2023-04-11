import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

root_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.join(root_dir, '/templates')
js_dir = os.path.join(root_dir, '/static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/templates/<path:path>')
def get_app(path):
    return send_from_directory(app_dir, path)

@app.route('/static/<path:path>')
def get_js(path):
    return send_from_directory(js_dir, path)


if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()