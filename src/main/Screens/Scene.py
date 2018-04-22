import pygame

#Generic scene class
class Scene(object):
    def __init__(self):
        pass

    def render(self, screen, events, manager):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError