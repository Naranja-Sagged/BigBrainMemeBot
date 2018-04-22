import pygame


class Button(object):

    def __init__(self, fileLocation, position, size):

        self.image = pygame.image.load(fileLocation)
        self.size = size
        self.image = pygame.transform.scale(self.image, size)
        # get image size and position
        self.position = position
        self.rect = self.image.get_rect()
        x,y = position
        x = x + (self.image.get_width() / 2)
        y = y + (self.image.get_height() / 2)
        self.position = position
        self.rect.center = x,y


    def draw(self, screen):
        # draw selected image
        screen.blit(self.image, self.position)

    def event_handler(self, event):
        for e in event:
             if e.type == pygame.MOUSEBUTTONDOWN:
                 # is some button clicked
                   pos = pygame.mouse.get_pos()
                   if self.rect.collidepoint(pos):  #is mouse over button
                       return True