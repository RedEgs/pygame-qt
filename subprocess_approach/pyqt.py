import sys
import os
from PyQt5.QtCore import QProcess, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QKeyEvent


class PygameWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pygame Embedded in PyQt5")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.start_button = QPushButton("Start Pygame")
        self.start_button.clicked.connect(self.start_pygame)
        self.layout.addWidget(self.start_button)

        self.pygame_container = QWidget(self)
        self.pygame_container.setFixedSize(640, 480)
        self.layout.addWidget(self.pygame_container)

        self.pygame_process = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_focus)

        def keyPressEvent(self, event):
            if isinstance(event, QKeyEvent):
                key_text = event.text()
                print(key_text)
                    #pygame.event.post(pygame.event.Event(pygame.KEYUP, {'key': key_text}))

        def keyReleaseEvent(self, event):
            if isinstance(event, QKeyEvent):
                pass
            
    def start_pygame(self):
        if self.pygame_process is None:
            self.pygame_process = QProcess(self)
            self.pygame_process.setProcessChannelMode(QProcess.MergedChannels)

            python_executable = sys.executable
            script_path = os.path.join(os.path.dirname(__file__), "pygame_app.py")

            hwnd = int(self.pygame_container.winId())
            self.pygame_process.start(python_executable, [script_path, str(hwnd)])
            self.start_button.setEnabled(False)

            # Start the timer to check for focus
            self.timer.start(100)

    def check_focus(self):
        if self.pygame_container and self.pygame_process:
            self.pygame_container.setFocus()
            self.activateWindow()  # Ensures the PyQt5 window is active
            self.pygame_container.setFocus()  # Set focus to the Pygame container
            self.timer.stop()  # Stop the timer after setting focus

    def closeEvent(self, event):
        if self.pygame_process:
            self.pygame_process.terminate()
            self.pygame_process.waitForFinished()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = PygameWidget()
    widget.show()
    sys.exit(app.exec_())
