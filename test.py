import sys, time

import pygame, os

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer

# https://www.pygame.org/docs/tut/PygameIntro.html
class Game():
    def __init__(self, win_id):
        pygame.init()
        self.window_init(win_id)

    def window_init(self, win_id):
        self.size = self.width, self.height = 1000, 1000
        
        os.environ['SDL_WINDOWID'] = str(win_id)
        os.environ['SDL_VIDEODRIVER'] = 'windib'
        self.screen = pygame.display.set_mode(self.size, pygame.NOFRAME)

        self.game_init()

    # pygame initialization
    def game_init(self):
        self.speed = [1, 1]
        self.black = 0, 0, 0

        self.ball = pygame.image.load("pygame_qt/ball.gif")
        self.ballrect = self.ball.get_rect()

    # pygame main loop
    def loop(self, window):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

        self.ballrect = self.ballrect.move(self.speed)
        if self.ballrect.left < 0 or self.ballrect.right > self.width:
            self.speed[0] = -self.speed[0]
        if self.ballrect.top < 0 or self.ballrect.bottom > self.height:
            self.speed[1] = -self.speed[1]

        self.screen.fill(self.black)
        self.screen.blit(self.ball, self.ballrect)
        pygame.display.flip()
        return False

# https://pythonspot.com/en/pyqt5-buttons
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window - pythonspot.com'
        self.left = 10
        self.top = 100
        self.width = 1000
        self.height = 720
        self.init_ui()
 
    def get_window_id(self):
        return int(self.winId())

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)



        self.show()

    def init_pygame(self, game):
        # https://stackoverflow.com/questions/46656634/pyqt5-qtimer-count-until-specific-seconds
        self.game = game
        self.timer = QTimer()
        self.timer.timeout.connect(self.pygame_loop)
        self.timer.start(0)

    def pygame_loop(self):
        if self.game.loop(self):
            self.close()

    def on_click(self):
        self.game.speed[0] = -self.game.speed[0]
        self.game.speed[1] = -self.game.speed[1]
        print('You clicked :\'(')

# make sure to call innit_py to init pygame loop
    
def main():
    app = QApplication(sys.argv)
    
    ex = Window()
    
    win_id = ex.get_window_id()
    game = Game(win_id)

    ex.init_pygame(game)

    result = app.exec_()
    print("Qt finished: " + str(result))
    sys.exit(result)

if __name__ == "__main__":
    main()