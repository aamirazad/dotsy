# For command line arguments
import sys
from random import choice
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

window_titles = [
    "My App",
    "My App",
    "Still My App",
    "Still My App",
    "What on earth",
    "What on earth",
    "This is surprising",
    "This is surprising",
    "Something went wrong",
]

# Create a qt widget (window)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dotsy")

        self.button = QPushButton("Press me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked")
        new_window_title = choice(window_titles)
        print("Setting title: %s" % new_window_title)
        self.setWindowTitle(new_window_title)


    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)

        if (window_title == "Something went wrong"):
            self.button.setDisabled(True)

app = QApplication(sys.argv)

window = MainWindow()
window.show() # Windows are hidden by default

# Start the exec loop
app.exec()
# Code after this will only run after exit
