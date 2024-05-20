import pygame
import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtGui import QIcon, QImage, QPainter
from PyQt5.QtCore import QTimer

def qt_draw(func, width, height, qimage, surface): 
    '''Decorator that reports the execution time.'''

    data=surface.get_buffer().raw
    image= QImage(data, width, height, QImage.Format_RGB32)

    return image