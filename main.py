from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
import random

class SlotGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical' 

        self.grid = GridLayout(cols=3, padding=20, spacing=10)
        self.add_widget(self.grid)
        self.slot_ids = [] 
        self.credit = 1000 

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
        self.cheat_btn.bind(on_press=self.add_money)

        self.cheat_btn = Button(text="+1000", background_color=(0, 1, 0, 1))
        button_box.add_widget(self.cheat_btn)
        self.cheat_btn.bind(on_press=self.add_money)
        def exit_game(self, instance):
            App.get_running_app().stop()
        
        self.reset_btn = Button(text="RESET")
        button_box.add_widget(self.reset_btn)
        self.status_label = Label(text="Status: Ready", font_size=20)
        self.add_widget(self.status_label)
        self.exit_btn = Button(text="EXIT", background_color=(0.5, 0.5, 0.5, 1))
        button_box.add_widget(self.exit_btn)
        self.exit_btn.bind(on_press=self.exit_game)
        
    def spin(self, instance):
        print("Spinning...")
        for img in self.slot_ids:
            number = random.randint(1, 3)
            img.source = f"{number}.png"

        self.check_win()
    
    def check_win(self):
        s1 = self.slot_ids[3].source
        s2 = self.slot_ids[4].source
        s3 = self.slot_ids[5].source

        if s1 == s2 == s3:
            self.credit += 100
            self.money_label.text = f"Money: {self.credit} (WIN!)"
            self.money_label.color = (0, 1, 0, 1) 
        else:
            self.credit -= 10
            self.money_label.text = f"Money: {self.credit}"
            self.money_label.color = (1, 1, 1, 1)
    def add_money(self, instance):
        self.credit += 1000
        self.money_label.text = f"Money: {self.credit}"
class SlotApp(App):
    def build(self):
        return SlotGame()

if __name__ == '__main__':
    SlotApp().run()
