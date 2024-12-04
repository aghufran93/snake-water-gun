import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

class SnakeWaterGunApp(App):
    def build(self):
        self.choices = ["Snake", "Water", "Gun"]
        self.user_score = 0
        self.computer_score = 0
        self.rounds = 3  # Hardcoded for now, can be added later via input
        self.round_count = 0

        layout = BoxLayout(orientation='vertical')
        
        self.score_label = Label(text=f"User: {self.user_score} - Computer: {self.computer_score}")
        layout.add_widget(self.score_label)

        self.choice_buttons = BoxLayout(size_hint=(1, 0.6))
        for choice in self.choices:
            btn = Button(text=choice, on_press=self.user_choice)
            self.choice_buttons.add_widget(btn)
        layout.add_widget(self.choice_buttons)

        self.result_label = Label(text="Welcome to Snake Water Gun! by Ahmed Ghufran Choose an option.")
        layout.add_widget(self.result_label)

        return layout

    def user_choice(self, instance):
        user_choice = instance.text
        computer_choice = random.choice(self.choices)
        self.round_count += 1

        if user_choice == computer_choice:
            self.result_label.text = f"It's a tie! Computer chose: {computer_choice}"
        elif (user_choice == "Snake" and computer_choice == "Water") or \
             (user_choice == "Water" and computer_choice == "Gun") or \
             (user_choice == "Gun" and computer_choice == "Snake"):
            self.user_score += 1
            self.result_label.text = f"You win this round! Computer chose: {computer_choice}"
        else:
            self.computer_score += 1
            self.result_label.text = f"Computer wins this round! Computer chose: {computer_choice}"

        self.score_label.text = f"User: {self.user_score} - Computer: {self.computer_score}"

        if self.round_count == self.rounds:
            self.end_game()

    def end_game(self):
        if self.user_score > self.computer_score:
            result = "Congratulations! You are the overall winner! 🏆"
        elif self.user_score < self.computer_score:
            result = "The computer wins! Better luck next time. 🤖"
        else:
            result = "It's an overall tie! Well played. 🤝"
        
        popup = Popup(title="Game Over", content=Label(text=result), size_hint=(0.8, 0.8))
        popup.open()

if __name__ == '__main__':
    SnakeWaterGunApp().run()