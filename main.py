import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, send_file
from werkzeug.utils import secure_filename
from bearsAnotate import anotatePhoto


app = Flask(__name__)

TEMP_IMAGES_FOLDER = "static/Images"
UPLOAD_FOLDER = "static/Ready_Images"

ALLOWED_EXTENSIONS = set(["jpg", "jpeg"])


def allowed_file(filename):
    """Проверяет расширение файла"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
@app.route("/main")
def mainpage() -> "html":
    return render_template("index.html")


@app.route("/upload", methods=["POST", "GET"])
def upload_file() -> "html":

    """Смотрит имя файла и выводит соответствующий ответ"""

    global filename

    if request.method == "POST":
        file = request.files["image"]

        if not file:
            return redirect("/notchoised")

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            temp_path = os.path.join(TEMP_IMAGES_FOLDER, "{}".format(filename))
            file.save(temp_path)
            ready_path = os.path.join(UPLOAD_FOLDER, "{}".format(filename))
            #функция с opecv обрабатывает и сохраняет изображение
            anotatePhoto(temp_path, ready_path)
            return render_template("upload.html",
                           the_photo = "static/Ready_Images/{}".format(filename))

        else:
            return redirect("/info")


@app.route("/download")
def download_file() -> "file":
    """Загружает текущий файл из папки"""
    p = "static/Ready_Images/{}".format(filename)
    return send_file(p, as_attachment=True)



@app.route("/info")
def info_page() -> "html":
    return render_template("info.html")


@app.route("/notchoised")
def second_info_page() -> "html":
    return render_template("second_info.html")


if __name__ == "__main__":
    app.run(debug=True)
