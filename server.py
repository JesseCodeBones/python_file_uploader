import os
from flask import Flask, render_template, request, send_file
from preview import generate_image_preview, generate_video_preview

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'files/')
    if not os.path.isdir(target):
        os.mkdir(target)
    for file in request.files.getlist("file"):
        filename = file.filename
        destination = "/".join([target, filename])
        file.save(destination)
        try:
            if destination.endswith(".mp4") or destination.endswith(".MP4"):
                generate_video_preview(destination)
            else:
                generate_image_preview(destination)
        except Exception as e:
            print(e)
    return render_template("finish.html")
@app.route("/check")
def check():
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(APP_ROOT, 'files/')
    filelist = os.listdir(target)
    files = []
    for file in filelist:
        if not file.endswith("__preview.jpg") :
            files.append(file)
    return render_template("preview.html", files=files)

@app.route("/preview")
def preview():
    file = request.args.get("file")
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(APP_ROOT, 'files/', file+"__preview.jpg")
    return send_file(target)
@app.route("/play")
def play():
    file = request.args.get("file")
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(APP_ROOT, 'files/', file)
    return send_file(target)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
