from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from preview_widget import Ui_Form

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import pygame_app, os

class PygameWindowTest(QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
       
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        
      
        
if __name__ == "__main__":
   app = QApplication([])
   widget = PygameWindowTest()
   widget.show()
   
   app.exec_() 