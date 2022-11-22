#!/usr/bin/env python

from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename
import urllib.request

app = Flask(__name__)


def isSupportedFileType(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in set(
        ["png", "jpg", "jpeg", "gif"]
    )


@app.route("/")
def uploadForm():
    return render_template("upload.html")


@app.route("/", methods=["POST"])
def upload_image():

    if "files[]" not in request.files:
        flash("No file part")
        return redirect(request.url)

    files = request.files.getlist("files[]")
    fileNames = list()
    imgLabels = list()

    for file in files:
        if file and isSupportedFileType(file.filename):
            filename = secure_filename(file.filename)
            fileNames.append(filename)
            imgLabels.append("label")
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        else:
            flash("Allowed image types are -> png, jpg, jpeg, gif")
            return redirect(request.url)

    return render_template("upload.html", filenames=fileNames, labels=imgLabels)


@app.route("/display/<filename>")
def display_image(filename):
    return redirect(url_for("static", filename="uploads/" + filename), code=301)


if __name__ == "__main__":
    app.config["UPLOAD_FOLDER"] = "static/uploads/"
    app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
    app.run(host="127.0.0.1", port="5000", debug=True)
