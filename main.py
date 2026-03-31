from kivy.app import App
from ui import CameraWidget

class ColorPalApp(App):
    def build(self):
        return CameraWidget()

if __name__ == "__main__":
    ColorPalApp().run()
