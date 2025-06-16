import pygame
from asteroids.constants import SCREEN_HEIGHT, SCREEN_WIDTH

class Resolution:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    @classmethod
    def info(cls):
        info = pygame.display.Info()
        height = SCREEN_HEIGHT or info.current_h
        width = SCREEN_WIDTH or info.current_w
        return cls(height, width)