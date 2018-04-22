import pygame
from src.main.Screens.Scene import Scene
from src.main.Screens.Button import Button
import src.main.Scenes.SceneManager

class TitleScene(Scene):
    def __init__(self):
        super(TitleScene, self).__init__()

    def render(self, screen, events, manager):
        self.image = pygame.image.load("Assets/Screens/Title.png")
        self.image = pygame.transform.scale(self.image, (1200, 600))

        screen.blit(self.image, [0, 0])