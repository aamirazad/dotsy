from PySide6.QtWidgets import QApplication, QWidget

# For command line arguments
import sys

app = QApplication(sys.argv)

# Create a qt widget (window)
window = QWidget()
window.show() # Windows are hidden by default

# Start the exec loop
app.exec()
# Code after this will only run after exit
