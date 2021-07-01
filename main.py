import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, send_file
from werkzeug.utils import secure_filename


app = Flask(__name__)

UPLOAD_FOLDER = "static/Images"
ALLOWED_EXTENSIONS = set(["jpg", "jpeg"])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
@app.route("/main")
def mainpage() -> "html":
    return render_template("index.html")


@app.route("/upload", methods=["POST", "GET"])
def upload_file():

    """Смотрит имя файла и выводит соответствующий ответ"""

    global filename

    if request.method == "POST":
        file = request.files["image"]

        if not file:
            return redirect("/notchoised")

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, "{}".format(filename)))
            return render_template("upload.html",
                           the_photo = "static/Images/{}".format(filename))

        else:
            return redirect("/info")


@app.route("/download")
def download_file():
    """Загружает текущий файл из папки"""
    p = "static/Images/{}".format(filename)
    return send_file(p, as_attachment=True)



@app.route("/info")
def info_page() -> "html":
    return render_template("info.html")


@app.route("/notchoised")
def second_info_page() -> "html":
    return render_template("second_info.html")


if __name__ == "__main__":
    app.run(debug=True)
