from flask import Flask
import logging
import os
from flask import Flask, request
import json
from flask_wtf.form import FlaskForm
from wtforms import fields
from wtforms import validators as v


app = Flask(__name__)

class LogSerser():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    logs_file = os.path.join(base_dir, f'services.log')
    app = app


    @staticmethod
    @app.route('/get_logs', methods=['GET'])
    def get_logs():
        with open(LogSerser.logs_file, 'r') as file:
            return file.read()

    @staticmethod
    @app.route('/post_logs', methods=['POST'])
    def set_logs():
        logs_data = request.form
        with open(LogSerser.logs_file, 'a') as file:
            file.write(f"<br>{logs_data['levelname']} | {logs_data['name']} | {logs_data['asctime']}| {logs_data['lineno']} | {logs_data['msg']} ")


if __name__ == '__main__':
    app.config['TESTING'] = True
    app.config['DEBUG'] = False
    app.config["WTF_CSRF_ENABLED"] = False
    app.run()

