from abc import abstractmethod, ABC

import pygame

__all__ = ['CircleShape']


class CircleShape(pygame.sprite.Sprite, ABC):
    """
    Base class for game objects with bounding circle.
    """
    __slots__ = ['position', 'rotation', 'radius']

    def __init__(self, x: float, y: float, radius: float, *groups: pygame.sprite.Group):
        super().__init__(*groups)

        self.position = pygame.Vector2(x, y)
        """Position of the object"""
        self.rotation = pygame.Vector2(0, 1)
        """Rotation of the object"""
        self.radius = radius
        """Shape size for collision calculation."""

    def collision(self, other: 'CircleShape') -> bool:
        """
        Calculates collision with another circle shape using bounding circle.
        :param other:
        :return:
        """
        return self.position.distance_to(other.position) <= self.radius + other.radius

    @abstractmethod
    def draw(self, screen: pygame.Surface) -> None:
        """
        Draw the shape on the screen.

        :param screen:
        :return:
        """

    @abstractmethod
    def update(self, dt: float) -> None:
        """
        Update the shape.

        :param dt: Delta time in seconds.
        :return:
        """
