from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

class SlotGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical' 

        self.grid = GridLayout(cols=3, padding=20, spacing=10)
        self.add_widget(self.grid)

class SlotApp(App):
    def build(self):
        return SlotGame()

if __name__ == '__main__':
    SlotApp().run()