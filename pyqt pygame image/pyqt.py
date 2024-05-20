from PyQt5.QtCore       import *
from PyQt5.QtGui        import *
from PyQt5.QtWidgets    import *

import pygame
import pygame_app
import sys




class PygameWidget(QWidget):
    def __init__(self, process, game: pygame_app.PygameWindow , parent=None):
        super(PygameWidget,self).__init__(parent)
        self.setFocusPolicy(Qt.StrongFocus)
        self.process = process
        self.game = game
        self.redraw()


        self.timer = QTimer(self)
        self.timer.setInterval(0)
        self.timer.timeout.connect(self.redraw)
        self.timer.start()
        
    def keyPressEvent(self, event):
        if isinstance(event, QKeyEvent):
            key_text = event.text()
            print(key_text)
            self.game.send_key(key_text)
            
            
            
    def redraw(self):
        surface = next(self.process)
        w=surface.get_width()
        h=surface.get_height()
        self.data=surface.get_buffer().raw
        self.image= QImage(self.data,w,h, QImage.Format_RGB32)
        
        self.repaint()

    def paintEvent(self,event):
        qp=QPainter()
        qp.begin(self)
        qp.drawImage(0,0,self.image)
        qp.end()


class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        game = pygame_app.PygameWindow()
        self.setCentralWidget(PygameWidget( game.run_game(), game ))
        
        
        




app=QApplication(sys.argv)
w=MainWindow()
w.show()
app.exec_()