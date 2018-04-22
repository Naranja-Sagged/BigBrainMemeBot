import pygame
from random import *
class shootingGame(object):
    def __init__(self):
        super(shootingGame, self).__init__()
        self.last = pygame.time.get_ticks()


    def render(self, screen, events, manager):
        self.image = pygame.image.load("Assets/Minigame1/Start.png")
        self.image = pygame.transform.scale(self.image, (1200, 600))
        screen.blit(self.image, [0, 0])
        rand_num = randint(5, 10)
        pygame.display.flip()
        beforewait = pygame.time.get_ticks()
        waiting = True
        while waiting:
            now = pygame.time.get_ticks()
            if now - self.last >= 1:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                        self.image = pygame.image.load("Assets/Minigame1/LeftEarly.png")
                        self.image = pygame.transform.scale(self.image, (1200, 600))
                        screen.blit(self.image, [0, 0])
                        pygame.display.flip()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_k:
                        self.image = pygame.image.load("Assets/Minigame1/RightEarly.png")
                        self.image = pygame.transform.scale(self.image, (1200, 600))
                        screen.blit(self.image, [0, 0])
                        pygame.display.flip()
            if now - beforewait >= rand_num*1000:
                waiting = False
        self.image = pygame.image.load("Assets/Minigame1/Shoot.png")
        self.image = pygame.transform.scale(self.image, (1200, 600))
        screen.blit(self.image, [0, 0])
        pygame.display.flip()
        running = True

        while running:
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    self.image = pygame.image.load("Assets/Minigame1/LeftWin.png")
                    self.image = pygame.transform.scale(self.image, (1200, 600))
                    screen.blit(self.image, [0, 0])
                    pygame.display.flip()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_k:
                    self.image = pygame.image.load("Assets/Minigame1/RightWin.png")
                    self.image = pygame.transform.scale(self.image, (1200, 600))
                    screen.blit(self.image, [0, 0])
                    pygame.display.flip()





    def update(self):
        pass

    def handle_events(self, events):
        pass