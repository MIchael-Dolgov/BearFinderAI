
import os
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)

dir_path = "Images/"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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
    
    #Настроить проверку формата файла
    #elif allowed_file(pic) != True:
    #   
    #   return redirect()

    #сохранить файлы в определённой папке
    else:
        img = Image.open(pic)
        img.save("Images/pic.JPEG")

    return render_template("upload.html")


if __name__ == "__main__":
    app.run(debug=True)
