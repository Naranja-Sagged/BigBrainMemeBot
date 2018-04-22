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
        for x in range(0, 3):
            y = random.randint(0, 2)
            #if (y % 2 == 1):
                # Display safety image
                #safe = Image("Assets/safety.jpg", (200 + 300 * x, 125), (400 + 300 * x, 325))
                #safe.draw(screen)
            #else:
                # Display death image
                #death = Image("Assets/safety.jpg", (200 + 300 * x, 125), (400 + 300 * x, 325))
                #death.draw(screen)

    def update(self):
        pass

    def handle_events(self, events):
        pass