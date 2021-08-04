import cv2
from base_camera import BaseCamera


class Camera(BaseCamera):
    def __init__(self):
        super().__init__()

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            raise RuntimeError("Could not start camera.")

        while True:
            _, frame = camera.read()
            yield cv2.imencode(".png", frame)[1].tobytes()
