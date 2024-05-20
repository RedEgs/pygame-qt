import sys, time, pygame, os

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer, QRect

class QEmbedWindow(QWidget):
    def __init__(self, Geometry: QRect):
        super.__init__()
        self._rect = Geometry
        
        
    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self._rect)
        
        
        self.show()
        
    def 