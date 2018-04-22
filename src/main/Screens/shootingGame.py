import pygame
from random import *
class shootingGame(object):
    def __init__(self):
        super(shootingGame, self).__init__()

    def render(self, screen, events, manager):
        self.image = pygame.image.load("Assets/Minigame1/Start.png")
        self.image = pygame.transform.scale(self.image, (1200, 600))
        screen.blit(self.image, [0, 0])
        rand_num = randint(5, 10)
        pygame.display.flip()
        pygame.time.wait(rand_num*1000)
        self.image = pygame.image.load("Assets/Minigame1/Shoot.png")
        self.image = pygame.transform.scale(self.image, (1200, 600))
        screen.blit(self.image, [0, 0])
        pygame.display.flip()
        running = True
        while running:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_d]:
                self.image = pygame.image.load("Assets/Minigame1/LeftWin.png")
                self.image = pygame.transform.scale(self.image, (1200, 600))
                screen.blit(self.image, [0, 0])
                pygame.display.flip()
            if keys[pygame.K_k]:
                self.image = pygame.image.load("Assets/Minigame1/RightWin.png")
                self.image = pygame.transform.scale(self.image, (1200, 600))
                screen.blit(self.image, [0, 0])
                pygame.display.flip()





    def update(self):
        pass

    def handle_events(self, events):
        pass