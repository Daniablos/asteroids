import pygame

from asteroids.constants import SCREEN_HEIGHT, SCREEN_WIDTH

__all__ = ['Resolution']


class Resolution:
    """
    Window resolution info.
    """
    __slots__ = ['width', 'height']

    def __init__(self, height: int, width: int):
        self.height: int = height
        self.width: int = width

    @property
    def size(self) -> tuple[int, int]:
        """
        Returns the (width, height) of the resolution.
        :return:
        """
        return self.width, self.height

    @classmethod
    def info(cls) -> 'Resolution':
        """
        Calculates windows resolution depending on settings and display info.
        :return:
        """
        info = pygame.display.Info()
        height = SCREEN_HEIGHT or info.current_h
        width = SCREEN_WIDTH or info.current_w

        return cls(height, width)
