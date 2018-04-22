import pygame
import random

from pygame.locals import *
from src.main.Screens.graphics import *

win = GraphWin()


class SlotWheel:
    # Display 3 rectangles, 200 from edge; 200 in width; 100 in between
    # 50 from top; 350 length; 200 from bottom
    
    rect1 = Rectangle(Point(200, 50), Point(400, 400))
    rect2 = Rectangle(Point(500, 50), Point(700, 400))
    rect3 = Rectangle(Point(800, 50), Point(1000, 400))
    for x in range(0, 3):
        y = random.randint(0, 2)
        if (y % 2==1):
            # Display safety image
            safe = Image("Assets/safety.jpg", (200 + 300 * x, 125), (400 + 300 * x, 325))
            safe.draw(screen)
        else:
            # Display death image
            death = Image("Assets/safety.jpg", (200 + 300 * x, 125), (400 + 300 * x, 325))
            death.draw(screen)
