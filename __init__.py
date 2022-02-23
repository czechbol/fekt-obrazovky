import mimetypes
import os

from flask import Flask, render_template, url_for

from os.path import join, dirname, realpath

PATH = join(dirname(realpath(__file__)), "static/resources/")

path = dirname(realpath(__file__))
app = Flask(__name__)
mimetypes.init()


def is_image(file):
    mimestart = mimetypes.guess_type(file)[0]

    if mimestart != None:
        mimestart = mimestart.split("/")[0]

        if mimestart in ["image"]:
            return True

    return False


def is_video(file):
    mimestart = mimetypes.guess_type(file)[0]

    if mimestart != None:
        mimestart = mimestart.split("/")[0]

        if mimestart in ["video"]:
            return True

    return False


@app.route("/")
def obrazovky():
    images = []
    videos = []
    for file in os.listdir(PATH):
        if is_video(file):
            videos.append(url_for("static", filename=f"resources/{file}"))
        elif is_image(file):
            images.append(url_for("static", filename=f"resources/{file}"))
    videos.sort()
    images.sort()
    if images == [] and videos == []:
        return render_template("empty.html")
    elif images == []:
        return render_template("videos.html", videos=videos)
    elif videos == []:
        return render_template("images.html", images=images)
    else:
        return render_template("both.html", images=images, videos=videos)


@app.route("/precise/<folder>")
def foldered_obrazovky(folder):
    images = []
    videos = []
    if os.path.exists(join(PATH, folder)):
        path_str = join(PATH, folder)
    else:
        path_str = PATH
    for file in os.listdir(path_str):
        if is_video(file):
            videos.append(url_for("static", filename=f"resources/{file}"))
        elif is_image(file):
            images.append(url_for("static", filename=f"resources/{file}"))
    videos.sort()
    images.sort()
    if images == [] and videos == []:
        return render_template("empty.html")
    elif images == []:
        return render_template("videos.html", videos=videos)
    elif videos == []:
        return render_template("images.html", images=images)
    else:
        return render_template("both.html", images=images, videos=videos)


if __name__ == "__main__":
    app.run()
