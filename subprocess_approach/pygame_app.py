import pygame
import sys
import os

def main():
    pygame.init()
    hwnd = None

    if len(sys.argv) > 1:
        hwnd = int(sys.argv[1])
        os.environ['SDL_WINDOWID'] = str(hwnd)

    screen = pygame.display.set_mode((640, 480), pygame.NOFRAME)
    pygame.display.set_caption("Pygame Window")

    x = 50
    y = 50
    width = 40
    height = 60
    vel = 5

    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    color_index = 0

    run = True

    keys_pressed = set()

    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                keys_pressed.add(event.key)
            elif event.type == pygame.KEYUP:
                keys_pressed.discard(event.key)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x -= vel

        if keys[pygame.K_RIGHT]:
            x += vel

        if keys[pygame.K_UP]:
            #print("pressed up")
            y -= vel

        if keys[pygame.K_DOWN]:
            y += vel

        color_index = (color_index + 1) % len(colors)
        screen.fill(colors[color_index])  # Change background color each frame
        pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))  # Draw a white rectangle
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
