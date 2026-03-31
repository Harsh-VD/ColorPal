import cv2

class CameraHandler:
    def __init__(self):
        self.capture = cv2.VideoCapture(0)

    def get_frame(self):
        ret, frame = self.capture.read()
        if not ret:
            return None
        return cv2.flip(frame, 0)
