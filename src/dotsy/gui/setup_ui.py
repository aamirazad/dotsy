from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit


class SetupUi(QWidget):
    def __init__(self):  # Fix the double underscores
        print("setting up")
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create the main layout
        layout = QVBoxLayout()

        # Create a button to run commands
        self.button = QPushButton("Click")
        self.button.clicked.connect(self.on_button_click)  # Add button handler
        layout.addWidget(self.button)

        # Create a text box to display output and command history
        self.outputBox = QTextEdit()
        layout.addWidget(self.outputBox)

        # Set the layout of the main window
        self.setLayout(layout)
        self.setWindowTitle("Dotsy")  # Add a window title
        self.setGeometry(300, 300, 400, 300)  # Set window size and position

    def on_button_click(self):
        # Example of handling button clicks
        self.outputBox.append("Button clicked!")
