import pygame
from pygame.locals import *

from src.main.Screens.SceneManager import SceneMananger
from src.main.Screens.TitleScene import TitleScene

DISPLAY = 1200, 600
DEPTH = 0
FLAGS = 0

def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("DEATH SLOTS")
    timer = pygame.time.Clock()
    running = True

    title = TitleScene()
    manager = SceneMananger()

    active_sprite_list = pygame.sprite.Group()
    active_sprite_list.draw(screen)

    while running:
        timer.tick(60)

        if pygame.event.get(QUIT):
            running = False
            return

        events = pygame.event.get()

        manager.scene.render(screen, events, manager)

if __name__ == "__main__":
     main()