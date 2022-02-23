import mimetypes
import os

from flask import Flask, render_template, url_for

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
    for file in os.listdir("static/resources"):
        if is_video(file):
            videos.append(url_for("static", filename=f"resources/{file}"))
        elif is_image(file):
            images.append(url_for("static", filename=f"resources/{file}"))
    return render_template("page.html", images=images, videos=videos)


@app.route("/<folder>")
def foldered_obrazovky(folder):
    images = []
    videos = []
    for file in os.listdir(f"static/resources/{folder}"):
        if is_video(file):
            videos.append(url_for("static", filename=f"resources/{file}"))
        elif is_image(file):
            images.append(url_for("static", filename=f"resources/{file}"))
    return render_template("page.html", images=images, videos=videos)


if __name__ == "__main__":
    app.run()
