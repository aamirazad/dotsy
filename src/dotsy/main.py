import sys
import time
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit
from PyQt6.QtCore import QProcess, Qt
from PyQt6.QtGui import QCloseEvent

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dotsy")
        self.backend = None
        self.setup_ui()
        self.start_backend()

    def setup_ui(self):
        # Create the central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Setup a button to initialize the repo
        init_button = QPushButton("Initialize Repo")
        init_button.clicked.connect(self.init_repo)
        layout.addWidget(init_button)

        # Add a text area to display backend logs
        self.log_area = QTextEdit()
        self.log_area.setReadOnly(True)
        layout.addWidget(self.log_area)

        # Set the window size
        self.setMinimumSize(400, 300)

    def start_backend(self):
        self.backend = QProcess(self)

        # Connect signals for output and errors from the backend
        self.backend.readyReadStandardOutput.connect(self.handle_backend_output)
        self.backend.readyReadStandardError.connect(self.handle_backend_error)

        # Start the Go backend using 'go run' in the specified folder
        # Make sure the path "./cmd/backend/main.go" is correct for your project directory
        self.backend.start("go", ["run", "./cmd/backend/main.go"])

    def handle_backend_output(self):
        # Capture backend's standard output
        output = self.backend.readAllStandardOutput().data().decode("utf-8", errors="replace")
        self.log_area.append(output.strip())

    def handle_backend_error(self):
        # Capture backend's error output
        err_output = self.backend.readAllStandardError().data().decode("utf-8", errors="replace")
        self.log_area.append(f"Error: {err_output.strip()}")

    def init_repo(self):
        """Send the 'init' command to initialize the repo."""
        if self.is_backend_running():
            # Note the newline at the end so the Go scanner can detect the message
            self.backend.write(b"init\n")
            self.log_area.append("Sent command: init")
        else:
            self.log_area.append("Error: Backend not running")

    def is_backend_running(self):
        return self.backend is not None and self.backend.state() == QProcess.ProcessState.Running

    def closeEvent(self, event: QCloseEvent) -> None:
        """Gracefully handle shutdown when closing the window."""
        if self.is_backend_running():
            # Tell the backend to quit
            self.backend.write(b"quit\n")
            self.log_area.append("Sent command: quit")
            self.backend.waitForFinished(1000)  # wait up to 1 second
            self.backend.kill()                # force kill if still running
        event.accept()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
