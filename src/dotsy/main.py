# main.py
from gui.setup_ui import SetupUi, ModeSelect
from PyQt6.QtWidgets import QApplication, QWidget
import sys
from core.config_manager import ConfigManager


class Dotsy(QWidget):  # Need to inherit from QWidget
    def __init__(self):  # Fix the double underscores
        super().__init__()
        self.ui = SetupUi()  # Create an instance
        self.ui.show()  # Show the window

        config_manager = ConfigManager()
        config = config_manager.get_config
        print(config)

        settings = config.get("Settings", {})
        mode = settings.get("mode", None)

        # Check if mode is None or not set
        if not mode:
            self.mode = ModeSelect()
            self.mode.show()

    # advanced = self.button = QPushButton("Advanced?")
    # advanced.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create QApplication instance
    window = Dotsy()
    sys.exit(app.exec())  # Start the event loop
