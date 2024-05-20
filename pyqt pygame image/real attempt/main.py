from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from design import Ui_MainWindow

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import pygame_app, os

class PygameWindowTest(QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
       

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.start_button.clicked.connect(self._start_pygame_window)
        self.ui.stop_button.clicked.connect(self._stop_pygame_window)
      
      
    def _start_pygame_window(self):
        self.game = pygame_app.PygameWindow()
        self.ui.pygame_widget.set_process(game=self.game, process=self.game.run_game())
        
    def _stop_pygame_window(self):
        self.ui.pygame_widget.close_process()
        self.game.close_game()
        
        
        
if __name__ == "__main__":
   app = QApplication([])
   widget = PygameWindowTest()
   widget.show()
   
   app.exec_() 