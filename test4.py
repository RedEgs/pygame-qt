import sys
import pygame
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import QTimer, Qt, pyqtSignal, QThread
from PyQt5.QtGui import QImage, QPixmap

class PygameWorker(QThread):
    update_image = pyqtSignal(QImage)

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.running = True

    def run(self):
        pygame.init()
        # Create an off-screen surface
        screen = pygame.Surface((self.width, self.height))

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            screen.fill((0, 0, 0))
            pygame.draw.circle(screen, (255, 0, 0), (self.width // 2, self.height // 2), 50)

            # Convert the Pygame surface to a QImage
            data = pygame.image.tostring(screen, 'RGB')
            image = QImage(data, self.width, self.height, QImage.Format_RGB888)
            self.update_image.emit(image)

            pygame.time.wait(16)  # Approximately 60 FPS

    def stop(self):
        self.running = False
        self.wait()

class PygameWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.label = QLabel(self)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

        self.pygame_thread = PygameWorker(640, 480)
        self.pygame_thread.update_image.connect(self.setImage)
        self.pygame_thread.start()

    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))

    def closeEvent(self, event):
        self.pygame_thread.stop()
        event.accept()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 and Pygame Integration")
        self.setGeometry(100, 100, 800, 600)
        self.centralWidget = PygameWidget(self)
        self.setCentralWidget(self.centralWidget)

        # Example PyQt5 UI elements
        self.button = QPushButton('PyQt5 Button', self)
        self.button.move(10, 10)
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        print("PyQt5 Button Clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
