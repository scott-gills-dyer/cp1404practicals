"""
CP1404 Practical
Kivy GUI program to convert kilometers to miles.

"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_RATIO = 1.60934


class MilesConverterApp(App):
    """"""
    output_km = StringProperty()

    def build(self):
        """"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """"""
        miles = self.convert_to_number(self, text)
        self.update_result(miles)

    def update_result(self, miles):
        """"""
        self.output_km = str(miles * MILES_TO_KM_RATIO)

    def handle_increment(self, text, change):
        """"""
        miles = self.convert_to_number(self, text) + change
        self.root.ids.input_miles.text = str(miles)

    @staticmethod
    def convert_to_number(self, text):
        """"""
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesConverterApp().run()
