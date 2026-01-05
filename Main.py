import gi
from config import translation

gi.require_version('Gtk', '4.0')
from gi.repository import GLib, Gtk, Gdk

# Config
Translation: dict = translation.get_translation('pt-br')

# Window style
css_provider = Gtk.CssProvider()
css_provider.load_from_path('style.css')
Gtk.StyleContext.add_provider_for_display(
    Gdk.Display.get_default(),
    css_provider,
    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
)


class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, **kargs) -> None:
        super().__init__(**kargs, title='Hello, world!')
        self.set_default_size(400, 100)
        self.set_resizable(False)

        self.num: int = 0   # Num

        ## Boxes
        # Main box
        self.main_box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, spacing=10
        )
        self.main_box.set_margin_top(10)
        self.main_box.set_margin_bottom(10)
        self.main_box.set_margin_start(10)
        self.main_box.set_margin_end(10)
        self.set_child(self.main_box)

        # Label box
        self.label_box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, spacing=2
        )
        self.main_box.append(self.label_box)

        # Button box
        self.button_box = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL, spacing=5
        )
        self.main_box.append(self.button_box)

        # Num label
        self.num_label = Gtk.Label(
            label=f'{Translation["value_label"]} {self.num}'
        )
        self.num_label.set_hexpand(True)
        self.label_box.append(self.num_label)

        # Button Add
        self.button_add = Gtk.Button(label='+1')
        self.button_add.connect('clicked', self.add_num)
        self.button_add.set_hexpand(True)
        self.button_box.append(self.button_add)

        # Button purge
        self.button_purge = Gtk.Button(label='-1')
        self.button_purge.connect('clicked', self.purge_num)
        self.button_purge.set_hexpand(True)
        self.button_box.append(self.button_purge)

    def print_num(self) -> None:
        if self.num < 0:
            self.num = 0

        self.num_label.props.label = f'{Translation["value_label"]} {self.num}'

    def add_num(self, button) -> None:
        self.num += 1
        self.print_num()

    def purge_num(self, button) -> None:
        self.num -= 1
        self.print_num()


def on_activate(app) -> None:
    win = MyWindow(application=app)
    win.present()


if __name__ == '__main__':
    app = Gtk.Application(application_id='com.example.App')
    app.connect('activate', on_activate)

    print(Translation['welcome'])
    app.run()
