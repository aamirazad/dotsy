from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# For command line arguments
import sys

# Create a qt widget (window)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dotsy")

        button = QPushButton("Press me!")

        self.setFixedSize(QSize(400,300))

        self.setCentralWidget(button)

app = QApplication(sys.argv)

window = MainWindow()
window.show() # Windows are hidden by default

# Start the exec loop
app.exec()
# Code after this will only run after exit
