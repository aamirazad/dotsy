import sys
import subprocess
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import QProcess

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dotsy")
        self.backend = QProcess()  # Initialize QProcess first
        
        # Add error handling for the process
        self.backend.errorOccurred.connect(self.handle_error)
        self.backend.finished.connect(self.handle_finished)
        
        self.setup_ui()
        self.start_backend()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        init_button = QPushButton("Initialize Repo")
        init_button.clicked.connect(self.init_repo)
        layout.addWidget(init_button)

    def handle_error(self, error):
        print(f"Process error occurred: {error}")

    def handle_finished(self, exit_code, exit_status):
        print(f"Process finished with exit code: {exit_code}, status: {exit_status}")

    def start_backend(self):
        try:
            if sys.platform == 'linux':
                # For Linux (adjust terminal as needed)
                self.backend.start('kitty', ['--', 'go', 'run', './backend/main.go'])
            elif sys.platform == 'darwin':
                # For macOS - corrected command
                self.backend = QProcess()
                self.backend.start('go', ['run', './cmd/backend/main.go'])
            
            # Check if process started successfully
            if not self.backend.waitForStarted(3000):  # Wait up to 3 seconds
                print("Failed to start backend process")
                return
            
            print("Backend process started successfully")
            
        except Exception as e:
            print(f"Error starting backend: {str(e)}")

    def init_repo(self):
        if self.backend.state() == QProcess.ProcessState.Running:
            self.backend.write(b"init\n")
        else:
            print("Backend is not running!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
