"""
CP1404 Practical
GUI demo to display input name.

"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """BoxLayoutDemo is a Kivy App for getting input name and displaying in a GUI."""
    def build(self):
        """Build the Kivy App from the kv file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle the greet button returning a greeting with input name."""
        print('test')
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def press_clear(self):
        """Clear the input name and greeting when pressed."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""



BoxLayoutDemo().run()
