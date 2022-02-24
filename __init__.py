import mimetypes
import os

from flask import Flask, render_template, url_for

from os.path import join, dirname, realpath

PATH = join(dirname(realpath(__file__)), "static/resources/")

path = dirname(realpath(__file__))
app = Flask(__name__)
mimetypes.init()


@app.route("/")
def obrazovky():
    files = []
    for file in os.listdir(PATH):
        typ, encoding = mimetypes.guess_type(file)

        if typ is not None and typ.split("/")[0] in ["video", "image"]:
            files.append(
                {
                    "type": typ,
                    "url": url_for("static", filename=f"resources/{file}"),
                }
            )

    files = sorted(files, key=lambda d: d["url"])

    if files == []:
        return render_template("empty.html")
    else:
        return render_template(
            "page.html",
            files=files,
        )


@app.route("/precise/<folder>")
def foldered_obrazovky(folder):
    files = []
    if os.path.exists(join(PATH, folder)):
        path_str = join(PATH, folder)
    else:
        path_str = PATH

    for file in os.listdir(path_str):
        typ, encoding = mimetypes.guess_type(file)

        if typ is not None and typ.split("/")[0] in ["video", "image"]:
            files.append(
                {
                    "type": typ,
                    "url": url_for("static", filename=f"resources/{file}"),
                }
            )

    files = sorted(files, key=lambda d: d["url"])

    if files == []:
        return render_template("empty.html")
    else:
        return render_template(
            "page.html",
            files=files,
        )


if __name__ == "__main__":
    app.run()
