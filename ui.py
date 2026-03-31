from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2

from camera import CameraHandler
from color_utils import get_color_name
from tts import speak

class CameraWidget(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera = CameraHandler()
        self.last_spoken = ""
        Clock.schedule_interval(self.update, 1.0 / 30)

    def update(self, dt):
        frame = self.camera.get_frame()
        if frame is None:
            return

        h, w, _ = frame.shape
        b, g, r = frame[h//2, w//2]

        color_name = get_color_name((int(r), int(g), int(b)))

        if color_name != self.last_spoken:
            speak(color_name)
            self.last_spoken = color_name

        cv2.circle(frame, (w//2, h//2), 10, (255, 255, 255), 2)

        buf = cv2.flip(frame, 0).tobytes()
        texture = Texture.create(size=(w, h), colorfmt='bgr')
        texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')

        self.texture = texture
