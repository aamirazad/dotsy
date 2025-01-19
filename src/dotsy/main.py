# main.py
from gui.setup_ui import SetupUi
from PyQt6.QtWidgets import QApplication, QWidget
import sys


class Dotsy(QWidget):  # Need to inherit from QWidget
    def __init__(self):  # Fix the double underscores
        super().__init__()
        self.ui = SetupUi()  # Create an instance
        self.ui.show()  # Show the window


if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create QApplication instance
    window = Dotsy()
    sys.exit(app.exec())  # Start the event loop
