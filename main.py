import kivy
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.widget import Widget 

import os

class FileChoose(Popup):
    load = ObjectProperty()


class MyGridLayout(Widget):
    file_path = StringProperty("No file chosen")
    text_input = ObjectProperty()
    popup = ObjectProperty()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.ids.text_input.text = stream.read()
        self.popup.dismiss()
    
    def open(self):
        self.popup = FileChoose(load=self.load)
        self.popup.open()


class MyApp(App):

    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()