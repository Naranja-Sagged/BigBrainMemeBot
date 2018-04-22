import pygame
import random

from pygame.locals import *
from src.main.Screens.graphics import *

class SlotsScreen(object):
    def __init__(self):
        super(SlotsScreen, self).__init__()

    def render(self, screen, events, manager):
        self.image = pygame.image.load("Assets/deathslotz.png")
        self.image = pygame.transform.scale(self.image, (1200, 600))
        screen.blit(self.image, [0, 0])
        pygame.draw.rect(screen, pygame.Color(0, 0, 0), (200, 50, 200, 350), 10)
        pygame.draw.rect(screen, pygame.Color(0, 0, 0), (500, 50, 200, 350), 10)
        pygame.draw.rect(screen, pygame.Color(0, 0, 0), (800, 50, 200, 350), 10)
        pygame.time.wait(2500)
        deathCount = 0;
        for x in range(0, 3):
            y = random.randint(0, 2)
            if y % 2 == 1:
                # Display safety image
                safe = pygame.image.load("Assets/safety.jpg")
                safe = pygame.transform.scale(safe, (200, 200))
                screen.blit(safe, [200 + 300 * x, 125])
                pygame.display.flip()
            else:
                # Display death image
                death = pygame.image.load("Assets/death.png")
                screen.blit(death, [200 + 300 * x, 100])
                pygame.display.flip()
                deathCount += 1
            pygame.time.wait(2500)

        if deathCount == 3:
            quit(1)

    def update(self):
        pass

    def handle_events(self, events):
        pass