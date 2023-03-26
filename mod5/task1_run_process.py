import subprocess
import os
from flask import Flask
import signal

app = Flask(__name__)

def run_process(port: int):
    try:
        app.run(debug=True, port=port)
    except:
        with subprocess.Popen(f'lsof -i :{port}', shell=True, stdout=subprocess.PIPE) as proc_start:
            for process in proc_start.stdout.readlines()[1:]:
                pid = int(process.split()[1])
                os.kill(pid, signal.SIGKILL)
    finally:
        app.run(debug=True, port=port)



@app.route('/hello', methods=['GET'])
def hello() -> str:
    return "Hello!"


if __name__ == '__main__':
    port = 5000
    run_process(port)
