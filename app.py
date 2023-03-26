from flask import Flask, send_file, render_template, request, redirect
import os
from werkzeug.utils import secure_filename
import random
from network import get_ip
import qrcode
import time

from getPin import renameAndCheck, getDataByPin

app = Flask(__name__)
getip = get_ip()


dataFolder = os.path.abspath(os.getcwd()) + "/data/"
file = dataFolder + "test.txt"
filename = "test.txt"
    

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/storeData")
def storeData():
    return render_template("upload.html")

@app.route("/storeDataUploader", methods=["POST"])
def storeDataUploader():
    if request.method == "POST":
        file = request.files["file"]
        return render_template("loadPin.html", name=renameAndCheck(file, dataFolder))
    else:
        return "Error!"



@app.route("/getData", methods=["GET", "POST"])
def getData():
    return render_template("getData.html")


@app.route("/downloadDataByPin", methods=["POST", "GET"])
def downloadDataByPin():
    if request.method == "POST":
        pin = request.form.get("pin")
        file = getDataByPin(pin, dataFolder)
        print("file:", file)
        if file is not None:
            return send_file(file, as_attachment=True, download_name=file)
        else:
            return "file not found"
    else:
        return render_template("getData.html")


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")






if __name__ == "__main__":
    app.run(host=getip, debug=True)