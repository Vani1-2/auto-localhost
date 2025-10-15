#lmao idk if this works
import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw, GLib

from server import LocalServer
import threading
import os

class AutoLocalhostApp(Adw.Application):
    def __init__(self):
        super().__init__(application_id="com.vani.auto_localhost")
        self.server = None

    def do_activate(self):
        win = Adw.ApplicationWindow(application=self)
        win.set_title("Auto Localhost")
        win.set_default_size(400, 200)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10, margin_top=20, margin_bottom=20, margin_start=20, margin_end=20)

        self.folder_chooser = Gtk.FileChooserButton(title="Choose Folder", action=Gtk.FileChooserAction.SELECT_FOLDER)
        self.port_entry = Gtk.Entry(placeholder_text="Port (default: 8000)")
        self.status_label = Gtk.Label(label="Server not running.")

        start_button = Gtk.Button(label="Start Server")
        stop_button = Gtk.Button(label="Stop Server")

        start_button.connect("clicked", self.on_start)
        stop_button.connect("clicked", self.on_stop)

        box.append(self.folder_chooser)
        box.append(self.port_entry)
        box.append(start_button)
        box.append(stop_button)
        box.append(self.status_label)

        win.set_content(box)
        win.present()

    def on_start(self, button):
        folder = self.folder_chooser.get_file()
        if not folder:
            self.status_label.set_text("No folder selected.")
            return
        path = folder.get_path()
        port_text = self.port_entry.get_text()
        port = int(port_text) if port_text.isdigit() else 8000
        self.server = LocalServer(path, port)
        msg = self.server.start()
        self.status_label.set_text(msg)

    def on_stop(self, button):
        if self.server:
            msg = self.server.stop()
            self.status_label.set_text(msg)
        else:
            self.status_label.set_text("Server not running.")

app = AutoLocalhostApp()
app.run()
