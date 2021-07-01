import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import time


app = Flask(__name__)

UPLOAD_FOLDER = "static/Images"
ALLOWED_EXTENSIONS = set(["jpg", "jpeg"])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


#def timer():
#    for i in range(10):
#        text = "Выберите другое раширение файла. Вы будете перенаправлены через: 5 секунд"
#        time.sleep(5)
#    return render_template(redirect("/")), 


@app.route("/")
@app.route("/main")
def mainpage() -> "html":
    return render_template("index.html")


@app.route("/upload", methods=["POST", "GET"])
def upload_file():

    if request.method == "POST":
        file = request.files["image"]

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, "{}".format(filename)))
            return render_template("upload.html",
                           the_photo = "static/Images/{}".format(filename))

        else:
            return redirect("/")



#def upload():
    #"""Принимает картинку"""
    #pic = request.files["image"]
    
    #if not pic:
    #    return "Изображение не выбрано", 400
    
    #Настроить проверку формата файла
    #Реализовать модуль time
    #elif allowed_file(pic) == False:
    #    return "Неверное расширение файла"

    #else:
    #    img = Image.open(pic)
    #    img.save("static/Images/pic.JPG")
    #    return render_template("upload.html",
    #                          the_photo = "static/Images/pic.JPG")


#@app.route("/Images/pic.JPEG")
#def image():
#    return render_template("upload.html",
#                           the_photo = "Images/pic.JPEG")


if __name__ == "__main__":
    app.run(debug=True)
