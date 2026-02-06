from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class SlotGame(BoxLayout):
    pass

class SlotApp(App):
    def build(self):
        return SlotGame()

if __name__ == '__main__':
    SlotApp().run()