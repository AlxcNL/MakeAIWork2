#!/usr/bin/env python

from flask import Flask, flash, request, redirect, url_for, render_template
from numpy import random as rand
from werkzeug.utils import secure_filename
import tensorflow as tf
from os import path, makedirs
from datetime import datetime
from pathlib import Path
import logging
import re

# LOG LEVELS
# DEBUG		Detailed information, useful during bugfixing
# INFO		Just enough information to be able to understand the flow
# WARNING	Information about unexpected conditions that might be solved later
# ERROR		Reporting that the program can perform some task
# CRITICAL	Reporting that the program can not continue

loggingPath = path.join(Path.cwd().parent, "logs")

if not path.exists(loggingPath):
    makedirs(loggingPath)

now, n = re.subn("[/,:]", "", datetime.today().strftime("%Y%m%d_%X"))
loggingFile = path.join(loggingPath, f"{now}.log")

# logging.basicConfig(filename=loggingFile, level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)
# logging.info("Logging to file..")

app = Flask(__name__)


def isSupportedFileType(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in set(
        ["png", "jpg", "jpeg", "gif"]
    )


def predict_label(filePath):
    # img = tf.keras.utils.load_img(filePath, target_size=(100, 100))

    # img_array = tf.keras.utils.img_to_array(img)
    # img_array = tf.expand_dims(img_array, 0)
    # predictions = model.predict(img_array)
    # score = tf.nn.softmax(predictions[0])

    # print(
    #     "This image most likely belongs to {} with a {:.2f} percent confidence.".format(
    #         class_names[np.argmax(score)], 100 * np.max(score)
    #     )
    # )

    # img = image.load_img(img_path, target_size=(100,100))
    # imgArray = image.img_to_array(i)/255.0
    # imgArray = imgArray.reshape(1, 100,100,3)
    # p = model.predict_classes()
    return "label"


@app.route("/")
def uploadForm():
    logging.info("route /")
    return render_template("upload.html")


@app.route("/", methods=["POST"])
def upload_image():
    logging.info("route / with POST")

    if "files[]" not in request.files:
        flash("No file part")
        return redirect(request.url)

    files = request.files.getlist("files[]")
    fileNames, imgLabels = list(), list()

    # batchNumber = 0
    batchSize = min(80, len(files))
    batch = rand.choice(files, batchSize)
    batchNr = 0

    # Generate batches
    for file in batch:
        if file and isSupportedFileType(file.filename):
            fileName = secure_filename(file.filename)
            logging.debug(f"batchNr : {batchNr}")

            batchPath = path.join(app.config["UPLOAD_FOLDER"], str(batchNr))
            # batchPath = app.config["UPLOAD_FOLDER"]
            logging.debug(f"batchPath : {batchPath}")

            if not path.exists(batchPath):
                makedirs(batchPath)

            filePath = path.join(batchPath, fileName)
            file.save(filePath)
            logging.debug(f"filePath : {filePath}")

            fileNames.append(filePath)
            logging.debug(f"filePath : {filePath}")

            label = predict_label(filePath)
            imgLabels.append(label)

        else:
            flash("Allowed image types are -> png, jpg, jpeg, gif")
            return redirect(request.url)

    # logging.debug(f"fileName : {fileName}")
    # logging.debug(f"batchPath : {batchPath}")

    return render_template("upload.html", filenames=fileNames, labels=fileNames)


@app.route("/<filename>")
def display_image(filename):
    logging.info("route /display/<filename>")
    logging.debug(f"fileName : {filename}")

    return redirect(url_for("/", filename=filename), code=301)
    # return redirect(url_for("static", filename=filename), code=301)


if __name__ == "__main__":
    app.config["UPLOAD_FOLDER"] = "static/batches/"
    app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
    app.run(host="127.0.0.1", port="5000", debug=True)
