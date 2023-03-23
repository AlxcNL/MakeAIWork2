#!/usr/bin/env python

from flask import Flask
from flask import request
from flask import render_template
from flask import send_from_directory
import os
import glob
import sys
import binascii
import argparse


app = Flask("Flask Image Gallery")
app.config['IMAGE_EXTS'] = [".png", ".jpg", ".jpeg", ".gif", ".tiff"]


def encode(x):
    return binascii.hexlify(x.encode('utf-8')).decode()

def decode(x):
    return binascii.unhexlify(x.encode('utf-8')).decode()


@app.route('/favicon.ico')
def favicon():
    return send_from_directory( os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon' )

@app.route('/')
def home():
    root_dir = app.config['ROOT_DIR']
    image_paths = list()

    for (root, dirs, files) in os.walk(root_dir):
        for file in files:
            if any(file.endswith(ext) for ext in app.config['IMAGE_EXTS']):
                image_paths.append( encode (os.path.join(root,file) ) )

    return render_template('index.html', paths=image_paths)

@app.route('/00')
def batch():
    root_dir = app.config['ROOT_DIR'] + "/00"
    image_paths = list()

    for (root, dirs, files) in os.walk(root_dir):
        for file in files:
            if any(file.endswith(ext) for ext in app.config['IMAGE_EXTS']):
                image_paths.append( encode (os.path.join(root,file) ) )

    return render_template('index.html', paths=image_paths)

@app.route('/cdn/<path:filepath>')
def download_file(filepath):
    dir,filename = os.path.split(decode(filepath))
    return send_from_directory(dir, filename, as_attachment=False)


if __name__=="__main__":
    parser = argparse.ArgumentParser('Usage: %prog [options]')
    parser.add_argument('root_dir', help='Gallery root directory path')
    parser.add_argument('-l', '--listen', dest='host', default='127.0.0.1', \
                                    help='address to listen on [127.0.0.1]')
    parser.add_argument('-p', '--port', metavar='PORT', dest='port', type=int, \
                                default=5000, help='port to listen on [5000]')
    args = parser.parse_args()
    app.config['ROOT_DIR'] = args.root_dir
    app.run(host=args.host, port=args.port, debug=True)
