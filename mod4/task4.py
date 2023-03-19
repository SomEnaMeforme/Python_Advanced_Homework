import os
from flask import Flask

app = Flask(__name__)


@app.route('/uptime', methods=['GET'])
def get_uptime() -> str:
    uptime = os.popen('uptime -s').read()
    return f"Current uptime is {uptime}"


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)

