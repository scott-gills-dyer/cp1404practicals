"""
CP1404 Practical
Kivy GUI program to convert kilometers to miles.

"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_RATIO = 1.60934


class MilesConverterApp(App):
    """Kivy App for converting miles to kilometres."""
    output_km = StringProperty()

    def build(self):
        """Build the Kivy App from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """Handle calculation (could be button press or other call), output result to label widget."""
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def update_result(self, miles):
        """Update the result label."""
        self.output_km = str(miles * MILES_TO_KM_RATIO)

    def handle_increment(self, text, change):
        """Handle up/down button press, update the text input with new value, call calculation function."""
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)

    @staticmethod
    def convert_to_number(text):
        """Convert text to float or 0.0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesConverterApp().run()
