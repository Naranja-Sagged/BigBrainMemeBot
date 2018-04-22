import pygame
from src.main.Screens.Scene import Scene
from src.main.Screens.Button import Button
import src.main.Screens.SceneManager

class TitleScene(Scene):
    def __init__(self):
        super(TitleScene, self).__init__()

    def render(self, screen, events, manager):
        self.image = pygame.image.load("Assets/Title.png")
        self.image = pygame.transform.scale(self.image, (1200, 600))

        screen.blit(self.image, [0, 0])

        startButton = Button("Assets/play.png", (727, 50), (400, 125))

        startButton.draw(screen)

        #Checks if the start button was clicked
        if(startButton.event_handler(events)):
            manager.go_to()
            manager.scene.render(screen, events, manager)
            pygame.display.flip()

    def update(self):
         pass

    def handle_events(self, events, scene):
         for e in events:
             if e.type == pygame.MOUSEBUTTONDOWN:
                 if e.button == 1:
                    self.manager.go_to(scene)