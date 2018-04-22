import pygame
from random import *
from src.main.Screens.SlotsScreen import SlotsScreen
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
            defeat = False
            now = pygame.time.get_ticks()
            if now - self.last >= 1:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                        self.image = pygame.image.load("Assets/Minigame1/LeftEarly.png")
                        self.image = pygame.transform.scale(self.image, (1200, 600))
                        screen.blit(self.image, [0, 0])
                        pygame.display.flip()
                        defeat = True
                        pygame.time.wait(3000)
                        manager.go_to(SlotsScreen)
                        manager.scene.render(self, screen, events, manager)
                        pygame.display.flip()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_k:
                        self.image = pygame.image.load("Assets/Minigame1/RightEarly.png")
                        self.image = pygame.transform.scale(self.image, (1200, 600))
                        screen.blit(self.image, [0, 0])
                        pygame.display.flip()
                        defeat = True
                        pygame.time.wait(3000)
                        manager.go_to(SlotsScreen)
                        manager.scene.render(self, screen, events, manager)
                        pygame.display.flip()
            if now - beforewait >= rand_num*1000 and not defeat:
                waiting = False
        self.image = pygame.image.load("Assets/Minigame1/Shoot.png")
        self.image = pygame.transform.scale(self.image, (1200, 600))
        screen.blit(self.image, [0, 0])
        pygame.display.flip()
        running = True
        slotsScreen = SlotsScreen()
        victory = False
        while running:
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_d and not victory:
                    self.image = pygame.image.load("Assets/Minigame1/LeftWin.png")
                    self.image = pygame.transform.scale(self.image, (1200, 600))
                    screen.blit(self.image, [0, 0])
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    manager.go_to(SlotsScreen)
                    manager.scene.render(self, screen, events, manager)
                    pygame.display.flip()
                    victory = True

                if event.type == pygame.KEYDOWN and event.key == pygame.K_k and not victory:
                    self.image = pygame.image.load("Assets/Minigame1/RightWin.png")
                    self.image = pygame.transform.scale(self.image, (1200, 600))
                    screen.blit(self.image, [0, 0])
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    manager.go_to(SlotsScreen)
                    manager.scene.render(self, screen, events, manager)
                    pygame.display.flip()
                    victory = True


    def update(self):
        pass

    def handle_events(self, events):
        pass