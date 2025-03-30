"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Lindsay Ward'


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (300, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            value = float(self.root.ids.input_number.text)
            result = value ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass

    def handle_increment(self, change):
        """
        Handle up/down button press, update the text input with new value
        :param change: The amount to change
        """
        try:
            current = float(self.root.ids.input_number.text)
            current += change
            self.root.ids.input_number.text = str(current)
            self.root.ids.output_label.text = ""
        except ValueError:
            pass


SquareNumberApp().run()