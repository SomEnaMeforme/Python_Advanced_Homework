from flask import Flask
import os


app = Flask(__name__)


@app.route("/preview/<int:size>/<path:file_path>")
def get_preview_file(size, file_path) -> str:
    abs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_path)
    with open(abs_path, 'r', encoding='utf-8') as file:
        result_text = file.read(size)
        result_size = len(result_text)
    return f'<b>{abs_path} {result_size}</b><br> {result_text}'


if __name__ == "__main__":
    app.run(debug=True)
