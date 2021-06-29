from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/")
@app.route("/main")
def mainpage() -> "html":
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    """Принимает картинку"""
    pic = request.files["image"]

    if not pic:
        return "Изображение не выбрано", 400
    
    else:
        return "Загружено"


if __name__ == "__main__":
    app.run(debug=True)
