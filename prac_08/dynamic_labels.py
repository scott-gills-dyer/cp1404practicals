from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabels(App):
    """"""

    def __init__(self, **kwargs):
        """"""
        super(DynamicLabels, self).__init__(**kwargs)
        self.names = ["John", "Lindsay", "Carl", "Steve", "James", "Snoop Dog"]

    def build(self):
        """"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)

DynamicLabels().run()