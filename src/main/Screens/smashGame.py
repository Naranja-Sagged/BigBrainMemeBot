import pygame

class smashGame(object):
    def __init__(self):
        super(smashGame, self).__init__()

        def render(self, screen, events, manager):
            self.image = pygame.image.load("Assets/Minigame1/Start.png")
            self.image = pygame.transform.scale(self.image, (1200, 600))
            screen.blit(self.image, [0, 0])