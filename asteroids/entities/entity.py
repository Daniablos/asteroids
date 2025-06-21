from typing import Protocol

import pygame

__all__ = ['Drawable', 'Updatable']


class Drawable(Protocol):
    """
    Drawable protocol represents objects that can be drawn on the screen.
    """

    def draw(self, surface: pygame.Surface) -> None:
        """
        Draw the entity on the surface.
        :param surface:
        :return:
        """


class Updatable(Protocol):
    """
    Updatable protocol represents objects that can be updated on the screen.
    """

    def update(self, delta_time: float) -> None:
        """
        Update the entity.
        :param delta_time:
        :return:
        """
