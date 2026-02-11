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

        self.money_label = Label(text="Money: 1000", font_size=30)
        self.score_board.add_widget(self.money_label)
        
        self.bet_label = Label(text="Bet: 10", font_size=30)
        self.score_board.add_widget(self.bet_label)
        
        button_box = BoxLayout(size_hint_y=0.2, padding=10, spacing=10) 
        self.add_widget(button_box)
        
        self.spin_btn = Button(text="SPIN!", background_color=(1,0,0,1))
        button_box.add_widget(self.spin_btn)
        
        self.reset_btn = Button(text="RESET")
        button_box.add_widget(self.reset_btn)

class SlotApp(App):
    def build(self):
        return SlotGame()

if __name__ == '__main__':
    SlotApp().run()
