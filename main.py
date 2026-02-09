from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label

class SlotGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical' 

        self.grid = GridLayout(cols=3, padding=20, spacing=10)
        self.add_widget(self.grid)
        self.slot_ids = [] 
        for i in range(9):
            img = Image(source='1.png') 
            self.slot_ids.append(img)
            self.grid.add_widget(img)
            self.score_board = BoxLayout(size_hint_y=0.2)
            self.add_widget(self.score_board)

class SlotApp(App):
    def build(self):
        return SlotGame()

if __name__ == '__main__':
    SlotApp().run()