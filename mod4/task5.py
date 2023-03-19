import os
from flask import Flask, request
import shlex

app = Flask(__name__)


@app.route('/ps', methods=['GET'])
def get_uptime() -> str:
    args: list[str] = request.args.getlist('arg')
    clean_user_cmd = shlex.quote(''.join(args))
    result = os.popen('ps ' + clean_user_cmd).read()
    return result


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)

