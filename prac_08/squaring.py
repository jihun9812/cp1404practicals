from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class SquareNumberApp(App):
    def build(self):
        Window.size = (200, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = f"{value} squared is {result:.2f}"
        except ValueError:
            self.root.ids.output_label.text = "Please enter a valid number"


SquareNumberApp().run()
