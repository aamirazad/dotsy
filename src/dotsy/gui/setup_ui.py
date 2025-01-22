import os
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QWidget,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QTextEdit,
    QToolBar,
    QStatusBar,
    QDialog,
    QDialogButtonBox,
    QLabel,
)
from PyQt6.QtGui import QAction
from core.config_manager import ConfigManager


class SetupUi(QMainWindow):
    def __init__(self):  # Fix the double underscores
        super().__init__()

        layout = QVBoxLayout()

        # Create a button to run commands
        self.button = QPushButton("Click")
        self.button.clicked.connect(self.on_button_click)  # Add button handler
        layout.addWidget(self.button)

        # Create a text box to display output and command history
        self.outputBox = QTextEdit()
        layout.addWidget(self.outputBox)

        # Toolbar
        toolbar = QToolBar("My main toolbar")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        button_action = QAction("Security mode", self)
        button_action.setStatusTip("Confirm commands before they run")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        button_action.setChecked(True)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Set the layout of the main window
        self.setWindowTitle("Dotsy")  # Add a window title
        self.setGeometry(300, 300, 400, 300)  # Set window size and position

    def on_button_click(self):
        # Example of handling button clicks
        self.outputBox.append("Button clicked!")

        dlg = CustomDialog()
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")

    def onMyToolBarButtonClick(self, s):
        self.outputBox.setVisible(s)


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HELLO!")

        QBtn = (
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)


class ModeSelect(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # Label
        self.label = QLabel(
            "Config not found\nAre you restoring your configuration or setting up a new config?"
        )
        layout.addWidget(self.label)

        # Buttons
        self.mode = None
        button_layout = QHBoxLayout()

        self.restore = QPushButton("Restore")
        self.restore.adjustSize()
        button_layout.addWidget(self.restore)

        self.new = QPushButton("New")
        self.new.adjustSize()
        button_layout.addWidget(self.new)

        layout.addLayout(button_layout)

        # Button connections
        self.restore.clicked.connect(lambda: self.set_mode("restore"))
        self.new.clicked.connect(lambda: self.set_mode("new"))

        # Finalize layout
        self.setLayout(layout)
        self.setWindowTitle("Mode Select")

    def set_mode(self, mode):
        """
        Generic method to handle both restore and new mode selection.

        :param mode: The mode to set ('restore' or 'new')
        """
        config_manager = ConfigManager()
        config = config_manager.get_config
        config["Settings"] = {"mode": mode}
        config_manager.save_config()
        self.close()
