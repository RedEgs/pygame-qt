import tkinter as tk
import pygame
import os, random

root = tk.Tk()
button_win = tk.Frame(root, width = 500, height = 25)
button_win.pack(side = tk.TOP)
embed_pygame = tk.Frame(root, width = 500, height = 500)
embed_pygame.pack(side = tk.TOP)

os.environ['SDL_WINDOWID'] = str(embed_pygame.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
print(str(embed_pygame.winfo_id()))
pygame.display.init()
screen = pygame.display.set_mode()

def random_color():
    global circle_color
    circle_color = pygame.Color(0)
    circle_color.hsla = (random.randrange(360), 100, 50, 100)

random_color() 
color_button = tk.Button(button_win, text = 'random color',  command = random_color)
color_button.pack(side=tk.LEFT)

def pygame_loop():
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, circle_color, (250, 250), 125)
    pygame.display.flip()
    root.update()  
    root.after(100, pygame_loop)

pygame_loop()
tk.mainloop()