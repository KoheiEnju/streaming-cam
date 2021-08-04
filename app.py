"""排他アクセスに関してはこちらを参照：https://qiita.com/RIckyBan/items/a7dea207d266ef835c48"""
from flask import Flask, Response
from flask.templating import render_template
from camera_handler import Camera


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/feed")
def feed():
    return Response(generator(Camera()), mimetype="multipart/x-mixed-replace; boundary=frame")


def generator(camera: Camera):
    while True:
        frame = camera.get_frame()
        yield b"--frame\r\n"
        yield b"Content-Type: image/png\r\n\r\n" + frame + b"\r\n\r\n"


if __name__ == "__main__":
    app.run(debug=True)
