"""Протоколы для игровых объектов.

Предоставляет два typing.Protocol:
- Drawable — для всего, что умеет рисоваться на pygame.Surface;
- Updatable — для всего, что обновляет своё состояние по delta_time.

Используйте при объявлении компонентов, чтобы не привязываться к конкретным
классам, а проверять только наличие нужных методов (структурная типизация).
"""
from typing import Protocol

import pygame

#pylint: disable=too-few-public-methods

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
